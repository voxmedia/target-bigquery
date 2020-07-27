import copy
import json
import re
import pytz
from datetime import datetime
from tempfile import TemporaryFile

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

MAX_TABLE_CACHE = 1024 * 1024 * 50  # load every 50MB TODO: add this as an option to the config file


def update_state(last_emitted_state, new_state, updated_table):
    last_table_state = last_emitted_state.get("bookmarks", last_emitted_state).get(updated_table)
    new_table_state = new_state.get("bookmarks", new_state).get(updated_table)
    if 'bookmarks' in last_emitted_state:
        last_emitted_state['bookmarks'][updated_table] = new_table_state
    else:
        last_emitted_state[updated_table] = new_table_state

    return last_emitted_state


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
        logger.info(f"Load {table_name} by FULL_TABLE (truncate)")
        load_config.write_disposition = WriteDisposition.WRITE_TRUNCATE
    else:
        logger.info(f"Appending to {table_name}")
        load_config.write_disposition = WriteDisposition.WRITE_APPEND

    logger.info("loading {} to BigQuery".format(table_name))

    load_job = None
    try:
        load_job = client.load_table_from_file(
            rows, dataset.table(table_name), job_config=load_config, rewind=True
        )
        logger.info("loading job {}".format(load_job.job_id))
        job = load_job.result()
        logger.info(job._properties)

        return job

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
        table_prefix=None,
        table_suffix=None,
        add_metadata_columns=True,
        table_configs={}
):
    state = {}
    last_emitted_state = {}
    schemas = {}
    key_properties = {}
    tables = {}
    rows = {}
    errors = {}
    table_prefix = table_prefix or ""
    table_suffix = table_suffix or ""
    first_run_time = datetime.utcnow().isoformat()
    first_run = True  # False once rows are loaded to bq
    emit_first_state = False  # True if rows are successfully loaded to bq
    truncate_tables = set()

    for line in lines:
        try:
            msg = singer.parse_message(line)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(line))
            raise

        if isinstance(msg, singer.RecordMessage):
            stream = msg.stream

            if stream not in schemas:
                raise Exception(f"A record for stream {msg.stream} was encountered before a corresponding schema")

            schema = schemas[stream]

            if validate_records:
                validate(msg.record, schema)

            if add_metadata_columns:
                msg.record["_time_extracted"] = msg.time_extracted.isoformat()
                msg.record["_time_loaded"] = first_run_time if first_run else datetime.utcnow().isoformat()
                # TODO: Would be useful to set _time_loaded when the load happens so that all rows have the same timestamp which could also be load id

            new_rec = filter(schema, msg.record)

            # NEWLINE_DELIMITED_JSON expects literal JSON formatted data, with a newline character splitting each row.
            data = bytes(json.dumps(new_rec, cls=DecimalEncoder) + "\n", "UTF-8")

            rows[stream].write(data)

        elif isinstance(msg, singer.StateMessage):
            logger.debug("updating state with {}".format(msg.value))

            if len(last_emitted_state) == 0:
                state = {**state, **msg.value}
                last_emitted_state = copy.deepcopy(state)

            elif "bookmarks" in msg.value:
                state["bookmarks"] = {**state.get("bookmarks", {}), **msg.value["bookmarks"]}

            else:
                state = {**state, **msg.value}

            for stream in rows.keys():
                load_rows = rows[stream]
                if (load_rows.tell() > MAX_TABLE_CACHE) or (first_run and load_rows.tell() > 0):
                    if first_run:
                        logger.info(f"first run, exporting data from stream: {stream}; _time_loaded: {first_run_time}; table state: {last_emitted_state.get('bookmarks', last_emitted_state).get(stream)}")
                    else:
                        logger.info(f"exporting data from stream: {stream}")
                    load_to_bq(
                        client=client,
                        dataset=dataset,
                        table_name=tables[stream],
                        table_schema=schemas[stream],
                        table_config=table_configs.get(stream, {}),
                        key_props=key_properties[stream],
                        metadata_columns=add_metadata_columns,
                        truncate=truncate if stream not in truncate_tables else False,
                        forced_fulltables=forced_fulltables,
                        rows=load_rows
                    )
                    truncate_tables.add(stream)
                    rows[stream] = TemporaryFile(mode="w+b")  # erase the file

                    last_emitted_state = update_state(last_emitted_state, state, stream)
                    emit_first_state = True

                    if not first_run:
                        yield last_emitted_state

            if emit_first_state and first_run:
                first_run = emit_first_state = False
                yield last_emitted_state

        elif isinstance(msg, singer.SchemaMessage):
            stream = msg.stream
            table_name = table_prefix + msg.stream + table_suffix

            if stream in rows:
                continue

            tables[stream] = table_name
            schemas[stream] = msg.schema
            key_properties[stream] = msg.key_properties
            rows[stream] = TemporaryFile(mode="w+b")
            errors[stream] = None

        elif isinstance(msg, singer.ActivateVersionMessage):
            # This is experimental and won't be used yet
            pass

        else:
            raise Exception("Unrecognized message {}".format(msg))

    # get the last table loaded, and any stragglers.
    for stream in rows.keys():
        logger.info(f"exporting data from stream: {stream}")
        load_to_bq(
            client=client,
            dataset=dataset,
            table_name=tables[stream],
            table_schema=schemas[stream],
            table_config=table_configs.get(stream, {}),
            key_props=key_properties[stream],
            metadata_columns=add_metadata_columns,
            truncate=truncate if stream not in truncate_tables else False,
            forced_fulltables=forced_fulltables,
            rows=rows[stream]
        )
        rows[stream] = TemporaryFile(mode="w+b")  # erase the file

        last_emitted_state = update_state(last_emitted_state, state, stream)

        yield last_emitted_state
