from tests import unittestcore
import singer
from target_bigquery.schema import build_schema, filter

class TestSimpleStream(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestSimpleStream, self).setUp()

    def test_flat_schema(self):
        schema = '{ "type": "SCHEMA", "stream": "simple_stream", "schema": { "properties": { "id": { "type": [ "null", "string" ] }, "name": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "integer" ] }, "ratio": { "type": [ "null", "number" ] }, "timestamp": { "type": "string", "format": "date-time" }, "date": { "type": "string", "format": "date" } }, "type": [ "null", "object" ] }, "key_properties": [ "id" ], "bookmark_properties": [ "date" ] }'

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        for f in schema:
            if f.name == "id":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "name":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "value":
                self.assertEqual(f.field_type.upper(), "INTEGER")

            elif f.name == "ratio":
                self.assertEqual(f.field_type.upper(), "FLOAT")

            elif f.name == "timestamp":
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            elif f.name == "date":
                self.assertEqual(f.field_type.upper(), "DATE")



