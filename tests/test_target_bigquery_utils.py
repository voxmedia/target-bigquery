import os
import json
from google.cloud.bigquery import Dataset

from tests import unittestcore

from target_bigquery.utils import ensure_dataset

from google.cloud import bigquery

class TestTargetBigQueryUtils(unittestcore.BaseUnitTest):

    def setUp(self):


        self.config_file = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                   'target-config.json')

        config = json.load(open(self.config_file))

        self.project_id = config["project_id"]

        self.dataset_id = "target_bigquery_unit_test_ensure_dataset_function" # config["dataset_id"]

        self.location = config.get("location", "US")

        self.client = bigquery.Client(project=self.project_id)

    def test_ensure_dataset(self):
        """
        the purpose of this test is to show that the dataset is obtained, if it already exists
        if it doesn't exist then it's created and then it is obtained
        """


        # PART 1
        # create dataset and get dataset
        client_1, dataset_newly_created = ensure_dataset(project_id=self.project_id,
                                         dataset_id=self.dataset_id,
                                         location=self.location)


        # PART 2 (identical code to part 1, but now the dataset already exists)
        # get dataset if dataset already exists
        client_2, dataset_already_exists = ensure_dataset(project_id=self.project_id,
                                         dataset_id=self.dataset_id,
                                         location=self.location)
        # PART 3: checks
        dataset_list = [dataset_newly_created, dataset_already_exists]

        for next_dataset in dataset_list:
            dataset_dict = next_dataset.__dict__

            assert type(next_dataset) == Dataset
            assert dataset_dict["_properties"]["datasetReference"]["projectId"] == self.project_id
            assert dataset_dict["_properties"]["datasetReference"]["datasetId"] == self.dataset_id


    def tearDown(self):
        self.delete_dataset()

    def delete_dataset(self):
        try:
            self.client.delete_dataset(
                dataset=self.dataset_id,
                delete_contents=True
            )
        except Exception as e:
            print(e)
            pass

