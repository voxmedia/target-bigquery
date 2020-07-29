from tests import unittestcore


class TestPartialLoads(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/simple_stream.json",
            config="../sandbox/target_config_cache.json"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

    def test_two_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams.json",
            config="../sandbox/target_config_cache.json"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

    def test_interlaced_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/interlaced_streams.json",
            config="../sandbox/target_config_cache.json"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

    def test_two_streams_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams_error.json",
            config="../sandbox/target_config_cache.json"
        )

        ret = main()
        print(self.get_state())

        self.assertEqual(ret, 2, msg="Exit code is not 2!")

        self.delete_dataset()

    def test_two_streams_one_state_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams_one_state_error.json",
            config="../sandbox/target_config_cache.json"
        )

        ret = main()
        print(self.get_state())

        self.assertEqual(ret, 2, msg="Exit code is not 2!")

        self.delete_dataset()

