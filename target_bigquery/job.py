import logging
import json
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
):
    state = None
    schemas = {}
    key_properties = {}
    rows = {}
    errors = {}
    table_suffix = table_suffix or ""

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

            new_rec = filter(schema, msg.record)

            # NEWLINE_DELIMITED_JSON expects literal JSON formatted data, with a newline character splitting each row.
            data = bytes(json.dumps(new_rec, cls=DecimalEncoder) + "\n", "UTF-8")

            rows[table_name].write(data)

            state = None

        elif isinstance(msg, singer.StateMessage):
            logger.debug("Setting state to {}".format(msg.value))
            state = msg.value

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

    for table in rows.keys():
        key_props = key_properties[table]
        SCHEMA = build_schema(schemas[table], key_properties=key_props)
        load_config = LoadJobConfig()
        load_config.schema = SCHEMA
        load_config.source_format = SourceFormat.NEWLINE_DELIMITED_JSON

        if truncate or (table in forced_fulltables):
            logger.info(f"Load {table} by FULL_TABLE")
            load_config.write_disposition = WriteDisposition.WRITE_TRUNCATE

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
