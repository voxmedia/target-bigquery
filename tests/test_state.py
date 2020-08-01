from tests import unittestcore
from target_bigquery.state import State

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
