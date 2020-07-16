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


def persist_lines_job(
    client,
    dataset,
    lines=None,
    truncate=False,
    forced_fulltables=[],
    validate_records=True,
    table_suffix=None,
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
                validate(msg.record, schema)  # I'm not sure if this is actually implemented

            if table_configs.get(table_name, {}).get("add_metadata_columns", True):
                msg.record["_time_extracted"] = msg.time_extracted.strftime("%Y-%m-%d %H:%M:%S.%f %Z")
                msg.record["_time_loaded"] = datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S.%f %Z")

            new_rec = filter(schema, msg.record)

            # NEWLINE_DELIMITED_JSON expects literal JSON formatted data, with a newline character splitting each row.
            data = bytes(json.dumps(new_rec, cls=DecimalEncoder) + "\n", "UTF-8")

            rows[table_name].write(data)

            # state = None  # why would you do this?!?!

        elif isinstance(msg, singer.StateMessage):
            logger.debug("Setting state to {}".format(msg.value))
            try:
                if "bookmarks" in msg.value:
                    state["bookmarks"] = {**state.get("bookmarks", {}), **msg.value["bookmarks"]}
                else:
                    state = {**state, **msg.value}
            except Exception as e:
                pass

        elif isinstance(msg, singer.SchemaMessage):
            # if we got a schema message, we're either on the first stream or moving onto the next stream
            schema_table_name = msg.stream + table_suffix

            if schema_table_name not in schemas and table_name in rows :
                # we've already grabbed this schema so we must be moving on, so do the data transfer here
                table_config = table_configs.get(table_name.replace(table_suffix, ""), {}) if table_suffix else table_configs.get(table_name, {})
                partition_field = table_config.get("partition_field", False)
                cluster_fields = table_config.get("cluster_fields", False)

                key_props = key_properties[table_name]
                schema = build_schema(schemas[table_name], key_properties=key_props, add_metadata=table_config.get("add_metadata_columns", True))
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

                try:
                    load_job = client.load_table_from_file(
                        rows[table_name], dataset.table(table_name), job_config=load_config, rewind=True
                    )
                    logger.info("loading job {}".format(load_job.job_id))
                    logger.info(load_job.result())
                    rows[table_name] = TemporaryFile(mode="w+b")  # erase the file
                except google_exceptions.BadRequest as err:
                    logger.error(
                        "failed to load table {} from file: {}".format(table_name, str(err))
                    )
                    if load_job.errors:
                        messages = [
                            f"reason: {err['reason']}, message: {err['message']}, job: {str(load_job)}"
                            for err in load_job.errors
                        ]
                        logger.error("errors:\n{}".format("\n".join(messages)))
                    raise

                if len(state["bookmarks"]) > 0:
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
        table_config = table_configs.get(table.replace(table_suffix, ""), {}) if table_suffix else table_configs.get(table, {})
        partition_field = table_config.get("partition_field", False)
        cluster_fields = table_config.get("cluster_fields", False)

        key_props = key_properties[table]
        schema = build_schema(schemas[table], key_properties=key_props, add_metadata=table_config.get("add_metadata_columns", True))
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
        if truncate or (table in forced_fulltables):
            logger.info(f"Load {table} by FULL_TABLE")
            load_config.write_disposition = WriteDisposition.WRITE_TRUNCATE
        else:
            load_config.write_disposition = WriteDisposition.WRITE_APPEND

        logger.info("loading {} to Bigquery.\n".format(table))

        try:
            load_job = client.load_table_from_file(
                rows[table], dataset.table(table), job_config=load_config, rewind=True
            )
            logger.info("loading job {}".format(load_job.job_id))
            logger.info(load_job.result())
        except google_exceptions.BadRequest as err:
            logger.error(
                "failed to load table {} from file: {}".format(table, str(err))
            )
            if load_job.errors:
                messages = [
                    f"reason: {err['reason']}, message: {err['message']}, job: {str(load_job)}"
                    for err in load_job.errors
                ]
                logger.error("errors:\n{}".format("\n".join(messages)))
            raise

    yield state
