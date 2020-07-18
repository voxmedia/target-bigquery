import os
import sys
import unittest
import json
import io
from google.cloud import bigquery



class BaseUnitTest(unittest.TestCase):

    def setUp(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..", "sandbox", "sa.json"))

        self.client = None
        self.project_id = None
        self.dataset_id = None

        sys.stdout = open("stdout.env", "wb")

    def tearDown(self):
        sys.stdout.close()
        os.remove("stdout.env")

    def set_cli_args(self, *args, **kwargs):
        arg = [arg for arg in args]
        for k, v in kwargs.items():
            if k == "stdin":
                sys.stdin = open(v, "r")
                continue

            arg.append("--{}".format(k))
            arg.append("{}".format(v))

        sys.argv[1:] = arg

        if "config" in kwargs:
            c = None
            with open(kwargs["config"], "r") as f:
                c = json.load(f)

            self.project_id = c["project_id"]
            self.dataset_id = c["dataset_id"]
            self.client = bigquery.Client(project=self.project_id)

    def delete_dataset(self):
        self.client.delete_dataset(
            dataset=self.dataset_id,
            delete_contents=True
        )

    def get_state(self):
        state = []
        with open("stdout.env", "rb") as f:
            for line in f:
                state.append(json.load(line))

        return state
