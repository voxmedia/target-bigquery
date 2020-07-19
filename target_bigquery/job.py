import json
from datetime import datetime
from tempfile import TemporaryFile

import pytz
import singer
from google.api_core import exceptions as google_exceptions
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import WriteDisposition
from google.cloud.bigquery.job import SourceFormat
from jsonschema import validate

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.schema import build_schema, filter

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
    partition_field = table_config.get("partition_field", None)
    cluster_fields = table_config.get("cluster_fields", None)

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

    load_job = None
    try:
        load_job = client.load_table_from_file(
            rows, dataset.table(table_name), job_config=load_config, rewind=True
        )
        logger.info("loading job {}".format(load_job.job_id))
        job = load_job.result()
        logger.info(job._properties)
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
    table_name = ""

    for line in lines:
        try:
            msg = singer.parse_message(line)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(line))
            raise

        if isinstance(msg, singer.RecordMessage):
            table_name = msg.stream + table_suffix

            if table_name not in schemas:
                raise Exception(
                    "A record for stream {} was encountered before a corresponding schema".format(
                        table_name
                    )
                )

            schema = schemas[table_name]

            if validate_records:
                validate(msg.record, schema)

            if add_metadata_columns:
                msg.record["_time_extracted"] = msg.time_extracted.isoformat()
                msg.record["_time_loaded"] = datetime.utcnow().isoformat()

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

        elif isinstance(msg, singer.SchemaMessage):
            schema_table_name = msg.stream + table_suffix

            if schema_table_name not in schemas and table_name in rows:  # maybe do this based on bytes in files
                table_config = table_configs.get(table_name.replace(table_suffix, ""),
                                                 {}) if table_suffix else table_configs.get(table_name, {})
                key_props = key_properties[table_name]
                table_schema = schemas[table_name]
                load_rows = rows[table_name]
                load_to_bq(client=client, dataset=dataset, table_name=table_name,
                           table_schema=table_schema, table_config=table_config,
                           key_props=key_props, metadata_columns=add_metadata_columns,
                           truncate=truncate, forced_fulltables=forced_fulltables, rows=load_rows)
                rows[table_name] = TemporaryFile(mode="w+b")  # erase the file

                if len(state.get("bookmarks", state)) > 0:
                    yield state

            table_name = schema_table_name

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
        table_config = table_configs.get(table.replace(table_suffix, ""), {}) if table_suffix else table_configs.get(
            table, {})
        key_props = key_properties[table]
        table_schema = schemas[table]
        load_rows = rows[table]
        load_to_bq(client=client, dataset=dataset, table_name=table,
                   table_schema=table_schema, table_config=table_config,
                   key_props=key_props, metadata_columns=add_metadata_columns,
                   truncate=truncate, forced_fulltables=forced_fulltables, rows=load_rows)
        rows[table] = TemporaryFile(mode="w+b")  # erase the file
    yield state
