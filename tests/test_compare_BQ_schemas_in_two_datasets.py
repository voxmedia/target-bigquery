"""
Purpose:
    If you have two datasets (let's say you loaded one with the master t-bq branch and the other with dvelopment branch),
        you can compare their schemas to make sure they're identical

Input:
    Supply name of GCP project below
    Supply names of two BQ datasets

Output:
    test passes if BQ schemas in two datasets are identical

Test config:
    solving 403 access denied error:

        In sandbox subdirectory of target-bigquery, add an sa.json file with GCP credentials.
            See README file of this repo - it has instructions how to get these credentials.

            unittestcore.py file will set GOOGLE_APPLICATION_CREDENTIALS env var to the file path

     IMPORTANT: Supply GCP project, dataset 1 and dataset 2 in the unit test

Sources:
    1) Jacob Karcz code
    2) https://cloud.google.com/bigquery/docs/samples/bigquery-list-tables#bigquery_list_tables-python
"""

from tests import unittestcore
from google.cloud import bigquery

def create_dict_of_BQ_schemas_from_dataset(project_id, dataset_id):

    """input: project id and dataset id

    output: a dictionary containing BigQuery scheams
    """

    # Construct a BigQuery client object.
    bq_client = bigquery.Client()
    bq_schemas_dict = {}

    # Make an API request.
    tables_http_iterator = bq_client.list_tables(project_id + '.' + dataset_id)

    for table_list_item in tables_http_iterator:
        print("{}.{}.{}".format(table_list_item.project, table_list_item.dataset_id, table_list_item.table_id))
        table = bq_client.get_table(
            f"{table_list_item.project}.{table_list_item.dataset_id}.{table_list_item.table_id}")

        bq_schemas_dict.update({table.table_id: table.schema})

    return bq_schemas_dict


class TestIfBiigQuerySchemasInTwoDatasetsMatch(unittestcore.BaseUnitTest):

    def test_if_bq_schemas_match_in_two_datasets(self):
        """Compare schemas in two BigQuery datasets"""

        # TODO (developer): enter your GCP project, dataset 1 and dataset 2
        # GCP_project = 'my_GCP_project'
        # dataset_1 = 'my_bigquery_dataset_1'
        # dataset_2 = 'my_bigquery_dataset_2'

        schemas_dataset_1 = create_dict_of_BQ_schemas_from_dataset(GCP_project, dataset_1)

        schemas_dataset_2 = create_dict_of_BQ_schemas_from_dataset(GCP_project, dataset_2)

        assert schemas_dataset_1 == schemas_dataset_2
