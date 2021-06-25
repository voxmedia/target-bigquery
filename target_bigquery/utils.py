import json
import os
import sys

import singer
from google.api_core import exceptions
from google.cloud import bigquery
from google.cloud.bigquery import Dataset

logger = singer.get_logger()


def emit_state(state):
    """
    Given a state, writes the state to a state file (e.g., state.json.tmp)

    :param state: state with bookmarks dictionary. State
    """
    if state is not None:
        line = json.dumps(state)
        logger.debug("Emitting state {}".format(line))
        sys.stdout.write("{}\n".format(line))
        sys.stdout.flush()

        if os.environ.get("TARGET_BIGQUERY_STATE_FILE", None):
            fn = os.environ.get("TARGET_BIGQUERY_STATE_FILE", None)
            with open(fn, "a") as f:
                f.write("{}\n".format(line))


def ensure_dataset(project_id, dataset_id, location):
    """
    Given a project id, dataset id and location, creates BigQuery dataset

    https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html

    :param project_id: GCP project id from target config file. Passed to bigquery.Client(). str
    :param dataset_id: BigQuery dataset id from target config file. str
    :param location: location for the dataset (US). Passed to bigquery.Client(). str
    :return: client (BigQuery Client Object) and Dataset (BigQuery dataset)
    """
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
