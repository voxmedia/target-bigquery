#!/usr/bin/env python3

import argparse
import io
import json
import sys
import traceback

import singer
from google.api_core import exceptions
from google.cloud import bigquery
from google.cloud.bigquery import Dataset

from target_bigquery.encoders import DecimalEncoder
from target_bigquery.job import persist_lines_job
from target_bigquery.schema import build_schema, filter
from target_bigquery.stream import persist_lines_stream
from target_bigquery.utils import emit_state

logger = singer.get_logger()


def main():
    parser = argparse.ArgumentParser()  # argparse.ArgumentParser(parents=[tools.argparser])
    parser.add_argument("-c", "--config", help="Config file", required=True)
    parser.add_argument("-t", "--tables", help="Table configs file", required=False)
    flags = parser.parse_args()

    with open(flags.config) as input:
        config = json.load(input)

    if flags.tables is not None:
        with open(flags.tables) as input:
            tables = json.load(input)
    else:
        tables = {}

    if config.get("replication_method") == "FULL_TABLE":
        truncate = True
    else:
        truncate = False

    forced_fulltables = config.get("forced_fulltables", [])

    table_suffix = config.get("table_suffix")

    location = config.get("location", "US")

    validate_records = config.get("validate_records", True)

    add_metadata_columns = config.get("add_metadata_columns", True)

    input = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")

    project_id, dataset_id = config["project_id"], config["dataset_id"]

    table_configs = tables.get("streams", {})

    client, dataset = ensure_dataset(project_id, dataset_id, location)

    try:
        if config.get("stream_data", True):
            state_iterator = persist_lines_stream(
                client, dataset, input, validate_records=validate_records,
            )

        else:
            state_iterator = persist_lines_job(
                client, dataset, input,
                truncate=truncate,
                forced_fulltables=forced_fulltables,
                validate_records=validate_records,
                table_suffix=table_suffix,
                add_metadata_columns=add_metadata_columns,
                table_configs=table_configs
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


def ensure_dataset(project_id, dataset_id, location):
    from google.cloud.bigquery import DatasetReference
    client = bigquery.Client(project=project_id, location=location)

    dataset_ref = DatasetReference(project_id, dataset_id)
    try:
        client.create_dataset(dataset_ref)
    except exceptions.GoogleAPICallError as e:
        if e.response.status_code == 409:  # dataset exists
            pass
        else:
            logger.critical(f"unable to create dataset {dataset_id} in project {project_id}; Exception {e}")
            return 2  # sys.exit(2)

    return client, Dataset(dataset_ref)


if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
