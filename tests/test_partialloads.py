"""Setup:

    - Add the following files into sandbox directory under project root directory:
    
            - sa.json with GCP credential
            
            - target_config_cache.json:
                    
                    {
                        "project_id": "{your-project-id}",
                        "dataset_id": "{your_dataset_id}"
                        "replication_method": "truncate",
                        "max_cache": 0
                    }
                    
            - target_config_cache_append.json:
            
                {
                    "project_id": "{your-project-id}",
                    "dataset_id": "{your_dataset_id}"
                    "replication_method": "append",
                    "max_cache": 0
                }
                
                OR
                
                {
                    "project_id": "{your-project-id}",
                    "dataset_id": "{your_dataset_id}"
                    "max_cache": 0
                }
"""

from tests import unittestcore
import os


class TestPartialLoadsPartialLoadJob(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'simple_stream.json'),
            # 
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(4, len(state))  # 3 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_starting_state(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'simple_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            state=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'state.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(5, len(state))  # first + 3 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_table_configs(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'simple_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            tables=os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                       'tests'), 'rsc'), 'config'), 'simple_stream_table_config.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(4, len(state))  # 3 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

    def test_two_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(7, len(state))  # 6 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_not_full(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams_not_full_state.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  #

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_interlaced_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'interlaced_streams.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 2 states + last emit

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams_error.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(5, len(state))  # 5 states + last

        self.assertEqual(ret, 2, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-10T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(2, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_one_state_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams_one_state_error.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        try:
            state = self.get_state()
        except:
            state = []

        self.assertEqual(0, len(state))

        self.assertEqual(ret, 2, msg="Exit code is not 0!")

        try:
            table = self.client.get_table("{}.stream_one".format(self.dataset_id))
            self.assertEqual(False, True)
        except:
            pass

        try:
            table = self.client.get_table("{}.stream_two".format(self.dataset_id))
            self.assertEqual(False, True)
        except:
            pass

    def test_simple_stream_load_twice_truncate(self):
        """
        test config:
            supply a target_config_cache.json file. Example:
                {
                    "project_id": "your_GCP_project",
                    "dataset_id": "your_BigQuery_dataset",
                    "replication_method": "truncate"
                }
        """

        from target_bigquery import main

        for i in range(2):  # two truncate loops
            self.set_cli_args(
                stdin=os.path.join(os.path.join(
                    os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'),
                                 'rsc'),
                    'partial_load_streams'), 'simple_stream.json'),
                config=os.path.join(
                    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                    'target_config_cache.json'),
                processhandler="partial-load-job",
                ds_delete=i == 0
            )

            ret = main()
            state = self.get_state()
            # counts the number of state emits
            self.assertEqual(4, len(state))  # initial emit + 3 states

            self.assertEqual(ret, 0, msg="Exit code is not 0!")
            self.assertDictEqual(state[-1],
                                 {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

            table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
            # it'll load 3 rows x times, but row number will  remain 3
            self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
            self.assertIsNone(table.clustering_fields)
            self.assertIsNone(table.partitioning_type)
            self.delete_temp_state()

    def test_simple_stream_load_twice_append(self):

        from target_bigquery import main

        for i in range(2):  # two append loops
            self.set_cli_args(
                stdin=os.path.join(os.path.join(
                    os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'),
                                 'rsc'),
                    'partial_load_streams'), 'simple_stream.json'),
                config=os.path.join(
                    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                    'target_config_cache_append.json'),
                processhandler="partial-load-job",
                ds_delete=i == 0
            )

            ret = main()
            state = self.get_state()
            self.assertEqual(4, len(state))  # initial emit + 3 states

            self.assertEqual(ret, 0, msg="Exit code is not 0!")
            self.assertDictEqual(state[-1],
                                 {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

            table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
            # it'll load 3 rows x times, the number of rows will be 3 * x
            self.assertEqual(3 * (i + 1), table.num_rows, msg="Number of rows mismatch")
            self.assertIsNone(table.clustering_fields)
            self.assertIsNone(table.partitioning_type)
            self.delete_temp_state()


class TestPartialLoadsBookmarksPartialLoadJob(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'simple_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(4, len(state))  # 3 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_table_configs(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'simple_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            tables=os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                       'tests'), 'rsc'), 'config'), 'simple_stream_table_config.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(4, len(state))  # 3 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

    def test_two_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(7, len(state))  # 6 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_interlaced_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'interlaced_streams.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 2 states + last

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams_error.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(5, len(state))  # 5 states + last

        self.assertEqual(ret, 2, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-10T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(2, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_one_state_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'two_streams_one_state_error.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(1, len(state))  # 1 last

        self.assertEqual(ret, 2, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        try:
            table = self.client.get_table("{}.stream_two".format(self.dataset_id))
            self.assertEqual(False, True)
        except:
            pass
