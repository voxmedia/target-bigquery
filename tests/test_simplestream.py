from tests import unittestcore


class TestSimpleStream(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/simple_stream.json",
            config="../sandbox/target_config.json"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

    def test_simple_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/simple_stream.json",
            config="../sandbox/target_config.json",
            tables="./rsc/simple_stream_table_config.json"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
