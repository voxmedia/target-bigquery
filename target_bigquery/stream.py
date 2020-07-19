import json
import logging

import singer
from google.api_core import exceptions
from google.cloud import bigquery
from jsonschema import validate

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.schema import build_schema, filter

logger = singer.get_logger()


def persist_lines_stream(client, dataset, lines=None, validate_records=True):
    state = None
    schemas = {}
    key_properties = {}
    tables = {}
    rows = {}
    errors = {}

    for line in lines:
        try:
            msg = singer.parse_message(line)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(line))
            raise

        if isinstance(msg, singer.RecordMessage):
            if msg.stream not in schemas:
                raise Exception(
                    "A record for stream {} was encountered before a corresponding schema".format(
                        msg.stream
                    )
                )

            schema = schemas[msg.stream]

            if validate_records:
                validate(msg.record, schema)

            new_rec = filter(schema, msg.record)  # adswerve fix

            new_rec = json.loads(json.dumps(new_rec, cls=DecimalEncoder))  # adswerve fix

            err = None
            try:
                err = client.insert_rows_json(tables[msg.stream], [new_rec])
                if err != []:  # adswerve fix
                    logging.error(
                        f"failed to insert rows for {tables[msg.stream]}: {str(err)}\n{msg.record}\nnew_rec: {new_rec}")  # adswerve fix
                    raise Exception(err)  # adswerve fix
            except Exception as exc:
                logger.error(
                    f"failed to insert rows for {tables[msg.stream]}: {str(exc)}\n{msg.record}\nnew_rec: {new_rec}"
                )
                raise

            errors[msg.stream] = err
            rows[msg.stream] += 1

            state = None

        elif isinstance(msg, singer.StateMessage):
            logger.debug("Setting state to {}".format(msg.value))
            state = msg.value

        elif isinstance(msg, singer.SchemaMessage):
            table = msg.stream
            schemas[table] = msg.schema
            key_properties[table] = msg.key_properties
            tables[table] = bigquery.Table(
                dataset.table(table), schema=build_schema(schemas[table])
            )
            # logging.info(f"Creating table {table} with schema: {build_schema(schemas[table])}")
            rows[table] = 0
            errors[table] = None
            try:
                tables[table] = client.create_table(tables[table])
            except exceptions.Conflict:
                pass

        elif isinstance(msg, singer.ActivateVersionMessage):
            # This is experimental and won't be used yet
            pass

        else:
            raise Exception("Unrecognized message {}".format(msg))

    for table in errors.keys():
        if not errors[table]:
            logging.info(
                "Loaded {} row(s) from {} into {}:{}".format(
                    rows[table], dataset.dataset_id, table, tables[table].path
                )
            )
            yield state
        else:
            logging.error("Errors (%s): %s", table, errors[table])
