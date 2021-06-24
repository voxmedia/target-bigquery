from tests import unittestcore
from google.cloud.bigquery import SchemaField
import json

class TestComplexStreamLoadJob(unittestcore.BaseUnitTest):

    def test_klaviyo_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/klaviyo_stream.json",
            config="../sandbox/target-config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_recharge_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/recharge_stream.json",
            config="../sandbox/target-config.json",
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
            stdin="./rsc/data/bing_ads_stream.json",
            config="../sandbox/target-config.json",
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
            stdin="./rsc/data/bing_ads_stream_schema_vs_data_have_diff_data_types.json",
            config="../sandbox/target-config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")


    def test_complex_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/facebook_stream.json",
            config="../sandbox/target-config.json",
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

    def test_complex_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/facebook_stream.json",
            config="../sandbox/target-config.json",
            tables="./rsc/config/facebook_stream_tables_config.json",
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
        target_config_file = json.load(open("rsc/config/facebook_stream_tables_config.json"))

        assert target_config_file['streams']['ads_insights_age_and_gender']['force_fields']['date_start']['type'] == 'DATE'
        assert target_config_file['streams']['ads_insights_age_and_gender']['force_fields']['date_start']['mode'] == 'NULLABLE'

        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/facebook_stream_date_start_is_required_string.json",
            config="../sandbox/target-config.json",
            tables="./rsc/config/facebook_stream_tables_config.json",
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
        print("finished running")


    def test_misformed_complex_stream(self):
        """
        Note that the config's "validate_records" flag should be set to False
        """
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/facebook_stream.json",
            config="../sandbox/malformed_target_config.json",
            processhandler="load-job",
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

##TODO: start here.
## fix directories
## document set up
## or maybe have 3 locations: sample_config (README), sandbox and rsc. Explain this in README

