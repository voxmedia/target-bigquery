from tests import unittestcore

"""Setup:
    - Add the following files into sandbox directory under project root directory:
    
            - sa.json with GCP credential
            
            - target-config.json:
                {
                    "project_id": "{your-project-id}",
                    "dataset_id": "{your_dataset_id}"
                }
                
            - target_config_contains_target_tables_config.json:    
                  {
                    "project_id": "{your-project-id}",
                    "dataset_id": "{your_dataset_id}"
                    "table_config": "rsc/config/simple_stream_table_config.json"
                  }      
              
            - malformed_target_config.json:
            
                {
                    "project_id": "{your-project-id}",
                    "dataset_id": "{your_dataset_id}"
                    "validate_records":  false
                }
              
"""

"""
Job load tests create a dataset in BQ and load a table into it. When the test finishes, the dataset gets deleted. 
    At the end of the test, case.py file in the unittest library gets invoked. 
    self._callTearDown() method runs, and it deletes the BQ dataset. 
    
If you want test BQ dataset to persist after your unit test, then manually create a BQ dataset with the same name
    as in your target-config file before running your unit test.    
    
"""

class TestSimpleStreamLoadJob(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target-config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target-config.json",
            tables="./rsc/config/simple_stream_table_config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)


    def test_simple_stream_with_tables_config_passed_inside_target_config_file(self):

        """
        Purpose:
            test a feature discussed here:
                https://github.com/adswerve/target-bigquery/issues/15

        Feature:
            Passing target tables config file (contains partitioning and clustering info) inside target config file.
        """
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target_config_contains_target_tables_config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

    def test_salesforce_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/salesforce_stream.json",
            config="../sandbox/target-config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_salesforce_stream_incomplete_this_test_should_fail(self):

        """
        This test fails, and that's desired behavior

        - test fails, because schema is invalid/incomplete

        - warning is given to user:
            WARNING the pipeline might fail because of undefined fields: {}

        """
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/salesforce_stream_incomplete.json",
            config="../sandbox/target-config.json",
            processhandler="load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")

    def test_misformed_simple_stream(self):
        """
        Note that the config's "validate_records" flag should be set to False
        """
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream_malformed.json",
            config="../sandbox/malformed_target_config.json",
            processhandler="load-job",
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)


class TestSimpleStreamPartialLoadJob(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target-config.json",
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target-config.json",
            tables="./rsc/config/simple_stream_table_config.json",
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)


class TestSimpleStreamBookmarksPartialLoadJob(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target-config.json",
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/data/simple_stream.json",
            config="../sandbox/target-config.json",
            tables="./rsc/config/simple_stream_table_config.json",
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()[-1]
        print(state)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state, {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

