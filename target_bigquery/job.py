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
    if truncate:
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
        init_state=None,
        truncate=False,
        validate_records=True,
        table_prefix=None,
        table_suffix=None,
        add_metadata_columns=True,
        table_configs=None,
        max_cache=50
):
    emitted_state = init_state or {}
    table_prefix = table_prefix or ""
    table_suffix = table_suffix or ""
    table_configs = table_configs or {}
    max_cache = 1024 * 1024 * max_cache

    state = {}
    schemas = {}
    key_properties = {}
    tables = {}
    rows = {}
    errors = {}
    truncate_tables = set()

    use_partial_loads = False  # only if tap uses bookmark version of state

    yield emitted_state  # yield init state, so even if there is an exception right after we get proper state emitted

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
                msg.record["_time_extracted"] = msg.time_extracted.isoformat() if msg.time_extracted else datetime.utcnow().isoformat()
                msg.record["_time_loaded"] = datetime.utcnow().isoformat()

            new_rec = filter(schema, msg.record)

            data = bytes(json.dumps(new_rec, cls=DecimalEncoder) + "\n", "UTF-8")
            rows[stream].write(data)

        elif isinstance(msg, singer.StateMessage):
            logger.info("updating state with {}".format(msg.value))

            if not use_partial_loads and "bookmarks" in msg.value:
                use_partial_loads = True
                if "bookmarks" not in emitted_state:
                    emitted_state["bookmarks"] = {}

            if "bookmarks" in msg.value:
                state["bookmarks"] = {
                    **emitted_state.get("bookmarks", {}),
                    **state.get("bookmarks", {}),
                    **msg.value["bookmarks"]
                }

            else:
                state = {**emitted_state, **state.get, **msg.value}

            if use_partial_loads and sum([rows[s].tell() for s in rows.keys()]) > max_cache:
                logger.info("partial load initiated...")

                for stream in rows.keys():
                    if rows[stream].tell() == 0:
                        continue

                    logger.info(f"partial load for {stream}")

                    load_to_bq(
                        client=client,
                        dataset=dataset,
                        table_name=tables[stream],
                        table_schema=schemas[stream],
                        table_config=table_configs.get(stream, {}),
                        key_props=key_properties[stream],
                        metadata_columns=add_metadata_columns,
                        truncate=truncate if stream not in truncate_tables else False,
                        rows=rows[stream]
                    )

                    # emit state of a partial load just for that stream
                    tmp = {**state}; tmp.pop("bookmarks", None)
                    emitted_state["bookmarks"][stream] = state["bookmarks"][stream]
                    emitted_state.update(tmp)

                    yield emitted_state

                    truncate_tables.add(stream)
                    rows[stream].close()  # erase the file
                    rows[stream] = TemporaryFile(mode="w+b")

        elif isinstance(msg, singer.SchemaMessage):
            stream = msg.stream
            table_name = table_prefix + msg.stream + table_suffix

            logger.info(msg.schema)

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

    # if partial loads enabled, this shouldn't load anything assuming the last message for each stream is the state
    for stream in rows.keys():
        if rows[stream].tell() > 0:
            logger.info(f"final load initiated for {stream}")

            load_to_bq(
                client=client,
                dataset=dataset,
                table_name=tables[stream],
                table_schema=schemas[stream],
                table_config=table_configs.get(stream, {}),
                key_props=key_properties[stream],
                metadata_columns=add_metadata_columns,
                truncate=truncate if stream not in truncate_tables else False,
                rows=rows[stream]
            )
            rows[stream].close()

            # emit state of a partial load just for that stream
            if use_partial_loads:
                tmp = {**state}; tmp.pop("bookmarks", None)
                emitted_state["bookmarks"][stream] = state["bookmarks"][stream]
                emitted_state.update(tmp)

                yield emitted_state

    if not use_partial_loads:
        yield state
