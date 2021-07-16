import pytest
import simplejson
import singer
import json

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from testfixtures import log_capture

from tests import unittestcore

from target_bigquery.validate_json_schema import validate_json_schema_completeness, check_stream_for_dupes_in_field_names

from tests.rsc.schemas.input_json_schemas import *

from tests.rsc.schemas.input_json_schemas_shopify import *

from tests.rsc.schemas.input_json_schemas_invalid import *

list_of_schema_inputs = [test_schema_collection_anyOf_problem_column,
                         schema_nested_1,
                         schema_nested_1_subset_items_problem,
                         schema_nested_2,
                         schema_nested_3_shopify,
                         shopify_orders_fixed,
                         shopify_customers,  # old schema.py fails on this in my test. New one works
                         shopify_custom_collections,
                         shopify_abandoned_checkouts_fixed,  # old schema.py fails on this in my test. New one works
                         shopify_products,
                         shopify_transactions,
                         # shopify_metafields_malformed, # not valid schema
                         shopify_metafields_fixed,
                         shopify_order_refunds,
                         shopify_collects
                         ]


class TestSchemaValidation(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestSchemaValidation, self).setUp()

    def test_schema_invalid_json(self):
        """
        supply invalid json file
        raises JSONDecodeError

        If you supply a valid json, such  as schema_nested_1:
            this will fail the test: Failed: DID NOT RAISE <class 'simplejson.scanner.JSONDecodeError'>
        """
        schema_0_input = schema_nested_2_invalid_JSON

        # if you uncomment this line:
        # schema_0_input = schema_nested_2
        # this will fail the test: Failed: DID NOT RAISE <class 'simplejson.scanner.JSONDecodeError'>
        # because this is a valid schema

        with pytest.raises(simplejson.scanner.JSONDecodeError):
            msg = singer.parse_message(schema_0_input)

    def test_schema_completeness_validation_valid_input(self):
        """"if you uncomment shopify_metafields_malformed in list_of_schema_inputs,
            this test will fail"""
        for complete_schema in list_of_schema_inputs:
            validate_json_schema_completeness(complete_schema)

        assert True

    def test_schema_completeness_validation_empty_props(self):
        invalid_schemas = [invalild_schema_top_field_empty_props,
                           invalid_schema_subfield_empty_props,
                           invalid_schema_under_anyOf_empty_props_example_1,
                           invalid_schema_under_anyOf_deep_nested_empty_props,
                           shopify_metafields_malformed,
                           shopify_abandoned_checkouts_malformed,
                           shopify_orders_malformed]

        for incomplete_schema in invalid_schemas:
            with pytest.raises(ValueError, match="JSON schema is invalid/incomplete. It has empty properties"):
                validate_json_schema_completeness(incomplete_schema)

    def test_schema_completeness_validation_empty_type(self):
        invalid_schemas = [invalild_schema_top_field_empty_type,
                           invalid_schema_subfield_empty_type,
                           invalid_schema_under_anyOf_deep_nested_empty_type,
                           invalid_schema_anyOf_discount_codes_empty_type
                           ]

        for incomplete_schema in invalid_schemas:
            with pytest.raises(ValueError, match="JSON schema is invalid/incomplete. It has empty type"):
                validate_json_schema_completeness(incomplete_schema)

    @log_capture()
    def test_schema_completeness_validation_empty_dictionary_not_pros_not_type_not_items(self, logcapture):
        invalid_schemas = [invalid_salesforce_schema]

        for incomplete_schema in invalid_schemas:
            validate_json_schema_completeness(incomplete_schema)

            expected_log = ('root', 'WARNING', "the pipeline might fail because of undefined fields: {}")

            logcapture.check(expected_log, )

    @log_capture()
    def test_several_nested_schemas_mailchimp_validate_completenes(self, logcapture):
        catalog = json.load(open("rsc/schemas/input_json_schemas_mailchimp_invalid_incomplete.json"))

        for next_schema_input in catalog['streams']:
            logcapture.records = []
            if next_schema_input['tap_stream_id'] in ['list_segment_members', 'list_members', 'unsubscribes']:
                validate_json_schema_completeness(next_schema_input)

                expected_log = ('root', 'WARNING', "the pipeline might fail because of undefined fields: {}")

                logcapture.check(expected_log, )


    def test_check_for_dupes_in_field_names(self):
        """
        this should raise an error: it has a dupe at the bottom level: "NAME"
        """
        catalog = json.load(open(
            "rsc/schemas/input_json_schemas_klaviyo_dupe_field_names_short_1_dupe_at_nested_level.json"))

        for next_schema_input in catalog['streams']:
            validate_json_schema_completeness(next_schema_input)

            check_stream_for_dupes_in_field_names(next_schema_input)

    def test_check_for_dupes_in_field_names_2(self):
        """
        this should raise an error: it has a dupe at the top level: "_ID"
        """
        catalog = json.load(open(
            "rsc/schemas/input_json_schemas_klaviyo_dupe_field_names_short_2_dupe_at_top_level.json"))

        for next_schema_input in catalog['streams']:
            validate_json_schema_completeness(next_schema_input)
            # check_stream_for_dupes_in_field_names(next_schema_input)
            with pytest.raises(ValueError): #TODO: check for exact error msg
                check_stream_for_dupes_in_field_names(next_schema_input)

    def test_check_for_dupes_in_field_names_input_fixed(self):
        """
        """
        catalog = json.load(open("rsc/schemas/input_json_schemas_klaviyo_no_dupe_field_names.json"))

        for next_schema_input in catalog['streams']:
            validate_json_schema_completeness(next_schema_input)

            check_stream_for_dupes_in_field_names(next_schema_input)

            assert True

