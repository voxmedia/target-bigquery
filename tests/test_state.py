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
"""

from tests import unittestcore
from target_bigquery.state import State
import os


class TestSimpleStream(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestSimpleStream, self).setUp()

    def test_init(self):
        s = State(**{"a": 1})
        print(s)

    def test_flat_schema(self):
        state = State()
        state.merge(
            {"bookmarks": {"stream_one": {"timestamp": "2020-01-10T00:00:00.000000Z"}}}
        )
        print(state)

        state.merge(
            {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"}}}
        )
        print(state)

        state.merge(
            {"bookmarks": {"stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}}
        )
        print(state)

    def test_state_but_no_data(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'no_data_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(2, len(state))  # initial emit + end state emit
        # TODO: fails: Expected: 2  Actual: 1

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

    def test_state_but_no_data_bookmarks_load(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'partial_load_streams'), 'no_data_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target_config_cache.json'),
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(2, len(state))  # initial emit + end state emit
        # TODO: fails: Expected: 2  Actual: 1

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})
