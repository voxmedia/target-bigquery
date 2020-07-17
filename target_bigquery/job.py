import sys
import logging
import json
import pytz
from datetime import datetime
from tempfile import TemporaryFile

from google.cloud import bigquery
from google.cloud.bigquery.job import SourceFormat
from google.cloud.bigquery import WriteDisposition
from google.cloud.bigquery import LoadJobConfig
from google.api_core import exceptions as google_exceptions

import singer
from jsonschema import validate

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.schema import build_schema, filter

logging.getLogger("googleapiclient.discovery_cache").setLevel(logging.ERROR)
logger = singer.get_logger()

def load_to_bq(client,
               dataset,
               table_name,
               table_schema,
               table_config,
               key_props,
               metadata_columns,
               truncate,
               forced_fulltables,
               rows):
    partition_field = table_config.get("partition_field", False)
    cluster_fields = table_config.get("cluster_fields", False)

    schema = build_schema(table_schema, key_properties=key_props, add_metadata=metadata_columns)
    load_config = LoadJobConfig()
    load_config.schema = schema
    if partition_field:
        load_config.time_partitioning = bigquery.table.TimePartitioning(
            type_=bigquery.table.TimePartitioningType.DAY,
            field=partition_field,
        )
    if cluster_fields:
        load_config.clustering_fields = cluster_fields
    load_config.source_format = SourceFormat.NEWLINE_DELIMITED_JSON
    if truncate or (table_name in forced_fulltables):
        logger.info(f"Load {table_name} by FULL_TABLE")
        load_config.write_disposition = WriteDisposition.WRITE_TRUNCATE
    else:
        load_config.write_disposition = WriteDisposition.WRITE_APPEND

    logger.info("loading {} to Bigquery.\n".format(table_name))

    load_job = False
    try:
        load_job = client.load_table_from_file(
            rows, dataset.table(table_name), job_config=load_config, rewind=True
        )
        logger.info("loading job {}".format(load_job.job_id))
        logger.info(load_job.result())
    except google_exceptions.BadRequest as err:
        logger.error(
            "failed to load table {} from file: {}".format(table_name, str(err))
        )
        if load_job and load_job.errors:
            reason = err.errors[0]["reason"]
            messages = [f"{err['message']}" for err in load_job.errors]
            logger.error("reason: {reason}, errors:\n{e}".format(reason=reason, e="\n".join(messages)))
            err.message = f"reason: {reason}, errors: {';'.join(messages)}"
        raise err


def persist_lines_job(
    client,
    dataset,
    lines=None,
    truncate=False,
    forced_fulltables=[],
    validate_records=True,
    table_suffix=None,
    add_metadata_columns=True,
    table_configs={}
):
    state = {}
    schemas = {}
    key_properties = {}
    rows = {}
    errors = {}
    table_suffix = table_suffix or ""
    current_stream = False

    for line in lines:
        try:
            msg = singer.parse_message(line)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(line))
            raise

        if not current_stream and msg.stream and current_stream != msg.stream:
            current_stream = msg.stream
            logger.info(f"collecting data from stream: {current_stream}")

        if isinstance(msg, singer.RecordMessage):
            table_name = msg.stream + table_suffix

            if table_name not in schemas:
                raise Exception(f"A record for stream {msg.stream} was encountered before a corresponding schema")

            schema = schemas[table_name]

            if validate_records:
                validate(msg.record, schema)

            if add_metadata_columns:
                msg.record["_time_extracted"] = msg.time_extracted.strftime("%Y-%m-%d %H:%M:%S.%f %Z")
                msg.record["_time_loaded"] = datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S.%f %Z")

            new_rec = filter(schema, msg.record)

            # NEWLINE_DELIMITED_JSON expects literal JSON formatted data, with a newline character splitting each row.
            data = bytes(json.dumps(new_rec, cls=DecimalEncoder) + "\n", "UTF-8")

            rows[table_name].write(data)

        elif isinstance(msg, singer.StateMessage):
            logger.debug("updating state with {}".format(msg.value))
            if "bookmarks" in msg.value:
                state["bookmarks"] = {**state.get("bookmarks", {}), **msg.value["bookmarks"]}
            else:
                state = {**state, **msg.value}

            for table in rows.keys():  # TODO: ensure that state and bq data are in sync while handling the case when
                                        # (a) we iterate through all the records of a stream first
                                        # or (b) records are not collected in sequence and streamed one by one
                load_rows = rows[table]
                if load_rows.tell() > 1024*1024*50:  # load every 50MB
                    table_config = table_configs.get(table.replace(table_suffix, ""), {}) if table_suffix else table_configs.get(table, {})
                    key_props = key_properties[table]
                    table_schema = schemas[table]
                    load_to_bq(client=client, dataset=dataset, table_name=table,
                               table_schema=table_schema, table_config=table_config,
                               key_props=key_props, metadata_columns=add_metadata_columns,
                               truncate=truncate, forced_fulltables=forced_fulltables, rows=load_rows)
                    rows[table] = TemporaryFile(mode="w+b")  # erase the file

                    if len(state.get("bookmarks", state)) > 0:
                        yield state

        elif isinstance(msg, singer.SchemaMessage):
            table_name = msg.stream + table_suffix

            if table_name in rows:
                continue

            schemas[table_name] = msg.schema
            key_properties[table_name] = msg.key_properties
            rows[table_name] = TemporaryFile(mode="w+b")
            errors[table_name] = None

        elif isinstance(msg, singer.ActivateVersionMessage):
            # This is experimental and won't be used yet
            pass

        else:
            raise Exception("Unrecognized message {}".format(msg))

    # get the last table loaded, and any stragglers.
    for table in rows.keys():
        table_config = table_configs.get(table.replace(table_suffix, ""), {}) if table_suffix else table_configs.get(table, {})
        key_props = key_properties[table]
        table_schema = schemas[table]
        load_rows = rows[table]
        load_to_bq(client=client, dataset=dataset, table_name=table,
                   table_schema=table_schema, table_config=table_config,
                   key_props=key_props, metadata_columns=add_metadata_columns,
                   truncate=truncate, forced_fulltables=forced_fulltables, rows=load_rows)
        rows[table] = TemporaryFile(mode="w+b")  # erase the file
    yield state
