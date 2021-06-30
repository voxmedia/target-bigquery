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

    Hardcode project and two datasets you want to compare: see comments below.

    Solving 403 access denied error:

        In sandbox subdirectory of target-bigquery, add an sa.json file with GCP credentials.
            See README file of this repo - it has instructions how to get these credentials.

            In sa.json, I use adswerve data transfer development project for this test

            unittestcore.py file will set GOOGLE_APPLICATION_CREDENTIALS env var to the file path

     IMPORTANT: Supply GCP project, dataset 1 and dataset 2 in the unit test

Sources:
    1) Jacob Karcz code
    2) https://cloud.google.com/bigquery/docs/samples/bigquery-list-tables#bigquery_list_tables-python
"""

from tests import unittestcore
from google.cloud import bigquery
import copy
import unittest

from tests.utils import convert_list_of_schema_fields_to_list_of_lists


def create_dict_of_bq_schemas_from_dataset(project_id, dataset_id):
    """input: project id and dataset id

    output: a dictionary containing BigQuery schemas
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

    @unittest.skip("Skipped - additional manual configuration is required - see comments. Enter GCP project and two datasets.")
    def test_if_bq_schemas_match_in_two_datasets(self,
                                                 remove_tables_from_dataset_2_which_are_not_present_in_dataset_1=True,
                                                 compare_in_original_fields_order=False):
        """Compare schemas in two BigQuery datasets

        remove_tables_from_dataset_2_which_are_not_present_in_dataset_1 = True
            it's possible that one dataset has tables which are not present in the other dataset.
            It is expected when the two datasets' reporting periods are different.
            True flag here will exclude those tables from schema comparison.
            False flag would mean a stricter comparison.

         compare_in_original_fields_order=True
            The two datasets may have tables with different fields order.
            True flag will compare the two schemas while taking order into account.
            False flag will skip this step and will only compare sorted schemas.
            True flag would mean a stricter comparison.
        """

        '''*****************************'''
        ''' Configuration Section Start '''
        '''*****************************'''
        GCP_project = 'adswerve-data-transfer-dev'
        dataset_1 = 't_bq_test_recharge_loaded_with_t_bq_master'
        dataset_2 = 't_bq_test_recharge_loaded_with_t_bq_dev'  # matches dataset 1
        '''*****************************'''
        '''  Configuration Section End  '''
        '''*****************************'''

        schemas_dataset_1_dict = create_dict_of_bq_schemas_from_dataset(GCP_project, dataset_1)

        schemas_dataset_2_dict = create_dict_of_bq_schemas_from_dataset(GCP_project, dataset_2)

        if remove_tables_from_dataset_2_which_are_not_present_in_dataset_1:

            for key, value in schemas_dataset_2_dict.items():
                if key not in schemas_dataset_1_dict.keys():
                    # workaround for E RuntimeError: dictionary changed size during iteration
                    schemas_dataset_2_dict = copy.deepcopy(schemas_dataset_2_dict)
                    schemas_dataset_2_dict.pop(key)

        # compare two datasets schemas, but if you want to account for order of columns
        if compare_in_original_fields_order:
            assert schemas_dataset_1_dict == schemas_dataset_2_dict

        # compare two dataset schemas, but ignore order of columns in tables
        schemas_sorted_list_dataset_1 = []
        schemas_sorted_list_dataset_2 = []

        for stream_name, stream_bq_schema in schemas_dataset_1_dict.items():
            stream_bq_schema_sorted = convert_list_of_schema_fields_to_list_of_lists(stream_bq_schema)
            schemas_sorted_list_dataset_1.append(stream_bq_schema_sorted)

        for stream_name, stream_bq_schema in schemas_dataset_2_dict.items():
            stream_bq_schema_sorted = convert_list_of_schema_fields_to_list_of_lists(stream_bq_schema)
            schemas_sorted_list_dataset_2.append(stream_bq_schema_sorted)

        assert schemas_sorted_list_dataset_1 == schemas_sorted_list_dataset_2

    def test_simple_comparison_flags_differences_inside_nested_fields(self):

        """The purpose of this test is to double check:

        if we have two schemas with differences in nested fields - would a simple comparison == catch it?

        change something in the nested field BusinessAddress - the test will fail
        """

        list_a = [['AccountFinancialStatus', 'STRING', 'NULLABLE', (), None],
                  ['AccountLifeCycleStatus', 'STRING', 'NULLABLE', (), None],
                  ['AccountMode', 'STRING', 'NULLABLE', (), None],
                  ['AutoTagType', 'STRING', 'NULLABLE', (), None],
                  ['BackUpPaymentInstrumentId', 'INTEGER', 'NULLABLE', (), None],
                  ['BillToCustomerId', 'INTEGER', 'NULLABLE', (), None],
                  ['BillingThresholdAmount', 'FLOAT', 'NULLABLE', (), None],
                  ['BusinessAddress', 'RECORD', 'NULLABLE',
                   [['BusinessName', 'STRING', 'NULLABLE', (), None], ['City', 'STRING', 'NULLABLE', (), None],
                    ['CountryCode', 'STRING', 'NULLABLE', (), None], ['Id', 'INTEGER', 'NULLABLE', (), None],
                    ['Line1', 'STRING', 'NULLABLE', (), None], ['Line2', 'STRING', 'NULLABLE', (), None],
                    ['Line3', 'STRING', 'NULLABLE', (), None], ['Line4', 'STRING', 'NULLABLE', (), None],
                    ['PostalCode', 'STRING', 'NULLABLE', (), None], ['StateOrProvince', 'STRING', 'NULLABLE', (), None],
                    ['TimeStamp', 'STRING', 'NULLABLE', (), None]], None]
                  ]

        list_b = [['AccountFinancialStatus', 'STRING', 'NULLABLE', (), None],
                  ['AccountLifeCycleStatus', 'STRING', 'NULLABLE', (), None],
                  ['AccountMode', 'STRING', 'NULLABLE', (), None],
                  ['AutoTagType', 'STRING', 'NULLABLE', (), None],
                  ['BackUpPaymentInstrumentId', 'INTEGER', 'NULLABLE', (), None],
                  ['BillToCustomerId', 'INTEGER', 'NULLABLE', (), None],
                  ['BillingThresholdAmount', 'FLOAT', 'NULLABLE', (), None],
                  ['BusinessAddress', 'RECORD', 'NULLABLE',
                   [['BusinessName', 'STRING', 'NULLABLE', (), None], ['City', 'STRING', 'NULLABLE', (), None],
                    ['CountryCode', 'STRING', 'NULLABLE', (), None], ['Id', 'INTEGER', 'NULLABLE', (), None],
                    ['Line1', 'STRING', 'NULLABLE', (), None], ['Line2', 'STRING', 'NULLABLE', (), None],
                    ['Line3', 'STRING', 'NULLABLE', (), None], ['Line4', 'STRING', 'NULLABLE', (), None],
                    ['PostalCode', 'STRING', 'NULLABLE', (), None], ['StateOrProvince', 'STRING', 'NULLABLE', (), None],
                    ['TimeStamp', 'STRING', 'NULLABLE', (), None]], None]
                  ]

        assert list_a == list_b
