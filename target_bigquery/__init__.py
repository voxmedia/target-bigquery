#!/usr/bin/env python3

import argparse
import io
import json
import sys
import traceback

import singer

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.job import persist_lines_job
from target_bigquery.schema import build_schema, filter
from target_bigquery.stream import persist_lines_stream
from target_bigquery.utils import emit_state, ensure_dataset

logger = singer.get_logger()


def main():
    parser = argparse.ArgumentParser()  # argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument("-c", "--config", help="Config file", required=True)
    parser.add_argument("-t", "--tables", help="Table configs file", required=False)
    flags = parser.parse_args()

    with open(flags.config) as f:
        config = json.load(f)

    tables = {}
    if flags.tables is not None:
        with open(flags.tables) as f:
            tables = json.load(f)

    truncate = False
    if config.get("replication_method", "append").lower() == "truncate":
        truncate = True

    table_prefix = config.get("table_prefix", "")
    table_suffix = config.get("table_suffix", "")
    location = config.get("location", "US")
    validate_records = config.get("validate_records", True)
    add_metadata_columns = config.get("add_metadata_columns", True)
    project_id, dataset_id = config["project_id"], config["dataset_id"]

    table_configs = tables.get("streams", {})
    max_cache = config.get("max_cache", 50)
    client, dataset = ensure_dataset(project_id, dataset_id, location)

    input = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")

    try:
        if config.get("stream_data", True):
            raise NotImplementedError("Not yet fully implemented!")
            # state_iterator = persist_lines_stream(
            #     client, dataset, input, validate_records=validate_records,
            # )

        else:
            state_iterator = persist_lines_job(
                client, dataset, input,
                truncate=truncate,
                validate_records=validate_records,
                table_prefix=table_prefix,
                table_suffix=table_suffix,
                add_metadata_columns=add_metadata_columns,
                table_configs=table_configs,
                max_cache=max_cache
            )

        for state in state_iterator:
            emit_state(state)

    except Exception as e:
        # load errors surface here
        logger.critical(e)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        logger.critical(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        return 2  # sys.exit(2)

    return 0  # sys.exit(0)

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
