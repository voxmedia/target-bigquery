"""Setup:
    - Add the following files into sandbox directory under project root directory:
            - sa.json with GCP credential
            - target-config.json:
                {
                    "project_id": "{your-project-id}",
                    "dataset_id": "{your_dataset_id}"
                }
"""
from tests import unittestcore
from google.cloud.bigquery import SchemaField
import json
import os


class TestComplexStreamLoadJob(unittestcore.BaseUnitTest):

    def test_klaviyo_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'klaviyo_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_klaviyo_stream_load_job_should_fail_due_to_dupes_in_fiels_names(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'klaviyo_stream_contains_dupe_fields.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()

        self.assertEqual(ret, 2, msg="Exit code is not 2!")  # expected exit code is 2 - serious problem

    def test_recharge_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'recharge_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_bing_ads_stream(self):
        """
        data vs schema match here
        """
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'bing_ads_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_bing_ads_stream_data_vs_schema_dont_match(self):
        """
        This test succeeds

        It tests if we overcame the following error in Tap Bing Ads

        JSON schema library validator flags a mismatch in data type between data and schema.

        CRITICAL 123456 is not of type 'null', 'string'

        Failed validating 'type' in schema['properties']['BillToCustomerId']:
            {'type': ['null', 'string']}

        On instance['BillToCustomerId']:
            123456

        """

        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'bing_ads_stream_schema_vs_data_have_diff_data_types.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_complex_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'facebook_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        # self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})
        #
        # table = self.client.get_table("{}.simple_stream_dev".format(self.dataset_id))
        # self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        # self.assertIsNone(table.clustering_fields)
        # self.assertIsNone(table.partitioning_type)

    def test_complex_stream_decimal_schema_valid(self):
        file = os.path.join(os.path.join(
            os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
            'data'), 'facebook_stream_decimal_test_schema_valid.json')

        data = []
        with open(file) as f:
            for line in f:
                data.append(json.loads(line))

        assert data[0]['schema']['properties']["budget_remaining"]["multipleOf"] == 1e-03
        assert data[1]['record']["budget_remaining"] == 5000000.1
        assert data[2]['record']["budget_remaining"] == 5000000.12
        assert data[3]['record']["budget_remaining"] == 57573500.123

        from target_bigquery import main

        self.set_cli_args(
            stdin=file,
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_complex_stream_decimal_schema_invalid(self):
        file = os.path.join(os.path.join(
            os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
            'data'), 'facebook_stream_decimal_test_schema_invalid.json')

        data = []
        with open(file) as f:
            for line in f:
                data.append(json.loads(line))

        assert data[0]['schema']['properties']["budget_remaining"]["multipleOf"] == 1e-02
        assert data[1]['record']["budget_remaining"] == 5000000.1
        assert data[2]['record']["budget_remaining"] == 5000000.12
        assert data[3]['record']["budget_remaining"] == 57573500.123

        from target_bigquery import main

        self.set_cli_args(
            stdin=file,
            config=os.path.join(
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                'target-config.json'),
            processhandler="load-job"
        )
        ret = main()
        self.assertEqual(ret, 2, msg="Exit code is not 2!")  # load must fail
        # weird error: Failed validating 'type' in schema['properties']['daily_budget']:
        # I changed nothing about daily_budget, I made budget_remaining invalid

    def test_complex_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'facebook_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            tables=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'config'), 'facebook_stream_tables_config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        # self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})
        #
        # table = self.client.get_table("{}.simple_stream_dev".format(self.dataset_id))
        # self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        # self.assertIsNotNone(table.clustering_fields)
        # self.assertIsNotNone(table.partitioning_type)

    def test_complex_stream_with_tables_config_force_field(self):
        """
        the purpose of this test is to make sure that if you supply date_start field
            in Facebook ads_insights_age_and_gender streams
            as a required string,
            build_schema function will force this field to NULLABLE DATE, according to target tables config file
        """
        target_config_file = json.load(open(os.path.join(os.path.join(
            os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
            'config'), 'facebook_stream_tables_config.json')))

        assert target_config_file['streams']['ads_insights_age_and_gender']['force_fields']['date_start'][
                   'type'] == 'DATE'
        assert target_config_file['streams']['ads_insights_age_and_gender']['force_fields']['date_start'][
                   'mode'] == 'NULLABLE'

        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'facebook_stream_date_start_is_required_string.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            tables=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'config'), 'facebook_stream_tables_config.json'),
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        # self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.ads_insights_age_and_gender".format(self.dataset_id))
        self.assertEqual(15, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

        actual = table.schema[42]

        expected = SchemaField(name='date_start',
                               field_type='DATE',
                               mode='NULLABLE',
                               description=None,
                               fields=(),
                               policy_tags=None)

        assert actual == expected

    def test_misformed_complex_stream(self):
        """
        Note that the target config's "validate_records" flag should be set to False

        sandbox/malformed_target_config.json:

            {
                "project_id": "{your-project-id}",
                "dataset_id": "{your_dataset_id}",
                "validate_records":  false
            }

        """
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'data'), 'facebook_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'malformed_target_config.json'),
            processhandler="load-job",
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
