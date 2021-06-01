import pytest
import simplejson
import singer
import json
import copy

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from testfixtures import log_capture

from target_bigquery.schema import build_schema, prioritize_one_data_type_from_multiple_ones_in_anyOf, convert_field_type

from tests.schema_old import build_schema_old

from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore

from tests.utils import convert_list_of_schema_fields_to_list_of_lists

from target_bigquery.validate_json_schema import validate_json_schema_completeness

from tests.rsc.input_json_schemas import *

from tests.rsc.input_json_schemas_recharge import *

from tests.rsc.input_json_schemas_amazon import *

from tests.rsc.input_json_schemas_asana import *

from tests.rsc.input_json_schemas_bing_ads import *

from tests.rsc.input_json_schemas_klaviyo import *

from tests.rsc.input_json_schemas_facebook import *

from tests.rsc.input_json_schemas_hubspot import *

from tests.rsc.input_json_schemas_shopify import *

from tests.rsc.input_json_schemas_invalid import *

list_of_schema_inputs = [test_schema_collection_anyOf_problem_column,
                         schema_nested_1,
                         schema_nested_1_subset_items_problem,
                         schema_nested_2,
                         schema_nested_3_shopify,
                         shopify_orders_fixed,
                         # shopify_customers, #old schema.py fails on this in my test. New one works
                         shopify_custom_collections,
                         # shopify_abandoned_checkouts_fixed, #old schema.py fails on this in my test. New one works
                         shopify_products,
                         shopify_transactions,
                         # shopify_metafields_malformed, # not valid schema
                         shopify_metafields_fixed,
                         shopify_order_refunds,
                         shopify_collects
                         ]


class TestStream(unittestcore.BaseUnitTest):

    # TODO: reduce repetition in this script. Specifically, for the unit tests of schema conversion

    def setUp(self):
        super(TestStream, self).setUp()

    def test_flat_schema(self):

        schema_0_input = schema_simple_1

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical?

        # assert schema_2_built_new_method == schema_3_built_old_method

        for f in schema_2_built_new_method:
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

            elif f.name == "geo":
                self.assertEqual(f.field_type.upper(), "GEOGRAPHY")

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf_string(self):

        test_input = {
                'anyOf': [
                    {
                        'type': [
                            'integer',
                            'null'
                        ]
                    },
                    {
                        'type': [
                            'boolean',
                            'null'
                        ]
                    },
                    {
                        'type': [
                            'string',
                            'null'
                        ]
                    }
                    ,
                    {
                        'type': [
                            'number',
                            'null'
                        ]
                    }
                ]
            }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "string"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "STRING"

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf_float(self):


        test_input = {
            'anyOf': [
                {
                    'type': [
                        'number',
                        'null'
                    ]
                },
                {
                    'type': [
                        'integer',
                        'null'
                    ]
                }
                ,
                {
                    'type': [
                        'boolean',
                        'null'
                    ]
                }
            ]
        }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "number"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "FLOAT"

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf_integer(self):

        test_input = {
            'anyOf': [

                {
                    'type': [
                        'integer',
                        'null'
                    ]
                }
                ,
                {
                    'type': [
                        'boolean',
                        'null'
                    ]
                }
            ]
        }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "integer"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "INTEGER"


    def test_one_nested_schema_1(self):

        schema_0_input = schema_nested_1

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical?
        assert schema_2_built_new_method == schema_3_built_old_method

        for f in schema_2_built_new_method:
            if f.name in ("date_start", "date_stop"):
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

    def test_one_nested_schema_2(self):

        schema_0_input = schema_nested_2

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns and case
        schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

        schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

        assert schema_built_new_method_sorted == schema_built_old_method_sorted


    def test_several_nested_schemas(self):

        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types


    def test_several_nested_schemas_amazon(self):

        list_of_schema_inputs_amazon = [amazon_orders, amazon_inventory, amazon_products]

        for next_schema_input in list_of_schema_inputs_amazon:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types


    def test_several_nested_schemas_asana_only_new_method(self):

        list_of_schema_inputs_asana = [ asana_users,
                                        asana_projects,
                                        asana_workspaces, # old schema conversion fails here
                                        asana_stories,
                                        asana_sections,
                                        asana_teams,
                                        asana_tasks,
                                        asana_tags]

        for next_schema_input in list_of_schema_inputs_asana:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            assert schema_2_built_new_method

    def test_several_nested_schemas_asana(self):

        list_of_schema_inputs_asana = [ asana_users,
                                        asana_projects,
                                        # asana_workspaces, # old schema conversion fails here
                                        asana_stories,
                                        asana_sections,
                                        asana_teams,
                                        asana_tasks,
                                        asana_tags]

        for next_schema_input in list_of_schema_inputs_asana:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types

    def test_several_nested_schemas_bing_ads(self):

        list_of_schema_inputs_bing_ads = [bing_ads_accounts,
                                          bing_ads_campaigns,
                                          bing_ads_ad_groups,
                                          bing_ads_ads,
                                          bing_ads_ad_extension_detail_report,
                                          bing_ads_ad_group_performance_report,
                                          bing_ads_ad_performance_report,
                                          bing_ads_age_gender_audience_report,
                                          bing_ads_audience_performance_report,
                                          bing_ads_campaign_performance_report,
                                          bing_ads_geographic_performance_report,
                                          bing_ads_goals_and_funnels_report,
                                          bing_ads_keyword_performance_report,
                                          bing_ads_search_query_performance_report
             ]

        for next_schema_input in list_of_schema_inputs_bing_ads:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types

    def test_several_nested_schemas_facebook(self):

        list_of_schema_inputs_facebook = [facebook_adcreative,
                                          facebook_ads,
                                          facebook_adsets,
                                          facebook_campaigns,
                                          facebook_ads_insights,
                                          facebook_ads_insights_age_and_gender,
                                          facebook_ads_insights_country,
                                          facebook_ads_insights_platform_and_device,
                                          facebook_ads_insights_region,
                                          facebook_ads_insights_dma
        ]

        for next_schema_input in list_of_schema_inputs_facebook:

            schema_0_input = next_schema_input

            schema_0_input = json.loads(schema_0_input)

            schema_0_input.update({"key_properties": "Id"})

            schema_0_input.update({"type": "SCHEMA"})

            schema_0_input = str(schema_0_input)

            schema_0_input = schema_0_input.replace("\'", "\"").replace("True","true").replace("False","false")

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types


    def test_several_nested_schemas_google_search_console(self):

        catalog = json.load(open("./rsc/input_json_schemas_google_search_console.json"))

        for next_schema_input in catalog['streams']:

            schema_0_input = copy.deepcopy(next_schema_input)

            schema_0_input.update({"type": "SCHEMA"})

            schema_0_input = str(schema_0_input)

            schema_0_input = schema_0_input.replace("\'", "\"").replace("True","true").replace("False","false")

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted


    def test_several_nested_schemas_hubspot(self):

        list_of_schema_inputs_hubspot = [hubspot_campaigns,
                                         hubspot_companies,
                                         hubspot_contact_lists,
                                         hubspot_contacts,
                                         hubspot_contacts_by_company,
                                         hubspot_deal_pipelines,
                                         hubspot_deals,
                                         hubspot_email_events,
                                         hubspot_engagements,
                                         hubspot_forms,
                                         hubspot_owners,
                                         hubspot_subscription_changes,
                                         hubspot_workflows
        ]

        for next_schema_input in list_of_schema_inputs_hubspot:

            schema_0_input = next_schema_input

            schema_0_input = json.loads(schema_0_input)

            # hubspot schemas are missing required key "key_properties"
            schema_0_input.update({"key_properties": "Id"})

            schema_0_input.update({"type": "SCHEMA"})

            schema_0_input = str(schema_0_input)

            schema_0_input = schema_0_input.replace("\'", "\"").replace("True","true").replace("False","false")

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types

    def test_several_nested_schemas_klaviyo(self):

        list_of_schema_inputs_amazon = [klaviyo_bounce,
                                        klaviyo_click,
                                        klaviyo_email,
                                        klaviyo_mark_as_spam,
                                        klaviyo_open,
                                        klaviyo_receive,
                                        klaviyo_subscribe_list,
                                        klaviyo_unsubscribe,
                                        klaviyo_unsub_list,
                                        klaviyo_update_email_preferences,
                                        klaviyo_global_exclusions,
                                        klaviyo_lists
                                        ]

        for next_schema_input in list_of_schema_inputs_amazon:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types


    @log_capture()
    def test_several_nested_schemas_mailchimp_validate_completeness_1(self, logcapture):

        catalog = json.load(open("./rsc/input_json_schemas_mailchimp.json"))

        for next_schema_input in catalog['streams']:
            logcapture.records = []
            if next_schema_input['tap_stream_id'] in ['list_segment_members', 'list_members', 'unsubscribes']:

                validate_json_schema_completeness(next_schema_input)

                expected_log = ('root', 'WARNING', "the pipeline might fail because of undefined fields: {}")

                logcapture.check(expected_log,)


    def test_several_nested_schemas_mailchimp(self):

        catalog = json.load(open("./rsc/input_json_schemas_mailchimp.json"))

        for next_schema_input in catalog['streams']:

            validate_json_schema_completeness(next_schema_input)
            # mailchimp catalog we use has four empty fields {}
            #     "merge_fields":{}
            #     "interests":{}
            # they are in 3 streams:
            # list_segment_members
            # list_members
            # unsubscribes

            #  #TODO: what do we do about {} in mailchimp? these tests fail
            # if next_schema_input['tap_stream_id'] in ['list_segment_members', 'list_members', 'unsubscribes']:
            #     continue

            schema_0_input = copy.deepcopy(next_schema_input)

            schema_0_input.update({"type": "SCHEMA"})

            schema_0_input = str(schema_0_input)

            schema_0_input = schema_0_input.replace("\'", "\"").replace("True","true").replace("False","false")

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted


    def test_several_nested_schemas_recharge(self):

        """
        for some reason recharge product stream schema conversion fails on the old schema.py
        works with the new schema conversion
        """

        list_of_schema_inputs_recharge = [recharge_addresses,
                                          recharge_charges,
                                          recharge_collections,
                                          recharge_customers,
                                          recharge_discounts,
                                          recharge_metafields_store,
                                          recharge_metafields_customer,
                                          recharge_metafields_subscription,
                                          recharge_onetimes,
                                          recharge_orders,
                                          # recharge_products, # for some reason recharge products conversion fails on the old schema.py
                                          recharge_shop,
                                          recharge_subscriptions
                                          ]

        for next_schema_input in list_of_schema_inputs_recharge:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types


    def test_several_nested_schemas_shopify(self):

        catalog = json.load(open("./rsc/input_json_schemas_shopify.json"))

        for next_schema_input in catalog['streams']:

            validate_json_schema_completeness(next_schema_input)

            schema_0_input = copy.deepcopy(next_schema_input)

            schema_0_input.update({"type": "SCHEMA"})

            schema_0_input = str(schema_0_input)

            schema_0_input = schema_0_input.replace("\'", "\"").replace("True","true").replace("False","false")

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted


    def test_shopify_orders_malformed_schema_old_conversion(self):

        """Schema conversion succeeds. Desired behaviour: raise an exception, say that this is incomplete schema"""

        list_of_schema_inputs = [shopify_orders_malformed
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            assert schema_3_built_old_method

    def test_shopify_orders_do_results_match_fix_vs_malformed(self):

        msg_malformed = singer.parse_message(shopify_orders_malformed)

        schema_malformed_built_old_method = build_schema_old(msg_malformed.schema,
                                                             key_properties=msg_malformed.key_properties,
                                                             add_metadata=True)

        msg_fixed = singer.parse_message(shopify_orders_fixed)

        schema_malformed_built_old_method = build_schema_old(msg_fixed.schema, key_properties=msg_fixed.key_properties,
                                                             add_metadata=True)

        assert schema_malformed_built_old_method == schema_malformed_built_old_method

    def test_shopify_orders_fixed_schema_old_and_new_conversion(self):

        """Schema conversion succeeds. Desired behaviour: raise an exception, say that this is incomplete schema
        this test compares:

        Shopify orders table - fixed vs malformed

        malformed schema converted using the old method

        fixed schema converted with the new method

        fixed schema converted with the new method

        the purpose is to check 2 things:

       1) it's okay to remove this from schema

        ,
                    {
                      "properties": {},
                      "type": [
                        "null",
                        "object"
                      ]
                    }


        2) new schema conversion is returning the same result as the old schema conversion. Specifically, it handles mode
        (REQUIRED vs NULL) correctly

        """

        schema_input_1 = shopify_orders_fixed

        schema_input_2 = shopify_orders_malformed

        msg_fixed = singer.parse_message(schema_input_1)

        schema_3_fixed_simplified = simplify(msg_fixed.schema)

        schema_4_fixed_built_new_method = build_schema(schema_3_fixed_simplified, key_properties=msg_fixed.key_properties,
                                                     add_metadata=True)

        schema_5_fixed_built_old_method = build_schema_old(msg_fixed.schema, key_properties=msg_fixed.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns and case
        schema_6_fixed_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_4_fixed_built_new_method)

        schema_7_fixed_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_5_fixed_built_old_method)

        msg_malformed = singer.parse_message(schema_input_2)

        schema_8_malformed_built_old_method = build_schema_old(msg_malformed.schema, key_properties=msg_malformed.key_properties,
                                                     add_metadata=True)

        schema_9_malformed_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_8_malformed_built_old_method)

        assert schema_6_fixed_built_new_method_sorted == schema_7_fixed_built_old_method_sorted == schema_9_malformed_built_old_method_sorted



    def test_shopify_orders_malformed_schema_new_conversion(self):

        """Test succeeds. This is malformed schema.
        subfields are not working correctly
        TODO: Desired behaviour: give a better error message. raise an exception, say that this is incomplete schema.
        Do schema validation in the very beginning
        """

        list_of_schema_inputs = [shopify_orders_malformed
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            assert schema_2_built_new_method

    def test_shopify_orders_fixed_schema_new_conversion(self):

        """succeeds"""

        list_of_schema_inputs = [shopify_orders_fixed
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            assert schema_2_built_new_method

    def test_shopify_customers_new_conversion(self):

        "succeeds"

        list_of_schema_inputs = [shopify_customers
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)
            assert schema_2_built_new_method


    def test_shopify_customers_old_conversion(self):

        """strangely, this test fails, which is odd, the pipeline with this old schema conversion and with this schema should be running fine

        This doesn't impact new t-bq release, as new schema.py handles it.

        Old conversion test appears to be failing at this anyOf column:

             "accepts_marketing_updated_at": {
        "anyOf": [
          {
            "type": "string",
            "format": "date-time"
          },
          {
            "type": "string"
          },
          {
            "type": "null"
          }
        ]
      }

        """

        list_of_schema_inputs = [shopify_customers
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)


            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties,
                                                         add_metadata=True)


            assert schema_3_built_old_method



    def test_shopify_custom_collection_new_conversion(self):

        "succeeds"

        list_of_schema_inputs = [shopify_custom_collections
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)
            assert schema_2_built_new_method



    def test_shopify_custom_collections_old_conversion(self):

        """succeeds"""

        list_of_schema_inputs = [shopify_custom_collections
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)


            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties,
                                                         add_metadata=True)

            assert schema_3_built_old_method


    def test_shopify_abandoned_checkouts_fixed_new_conversion(self):

        """
        succeeds

        removed this :

        ,
                    {
                      "properties": {},
                      "type": [
                        "null",
                        "object"
                      ]
                    }

        """

        list_of_schema_inputs = [shopify_abandoned_checkouts_fixed
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)
            assert schema_2_built_new_method


    def test_shopify_products_new_conversion(self):

        """success"""

        list_of_schema_inputs = [shopify_products
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)
            assert schema_2_built_new_method


    def test_shopify_transactions_new_conversion(self):

        list_of_schema_inputs = [shopify_transactions
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)
            assert schema_2_built_new_method


    def test_shopify_metafields_malformed_new_conversion(self):

        """
        this column causes it to break

          "value": {
                "type": [
                    "null",
                    "integer",
                    "object",
                    "string"
                ],
                "properties": {}
            }

        error:

                prioritization_dict = {"string": 1,
                               "number": 2,
                               "integer": 3,
                               "boolean": 4}

        anyOf_data_types = {}

        for i in range(0, len(field_property['anyOf'])):

            data_type = field_property['anyOf'][i]['type'][0]

>           anyOf_data_types.update({data_type: prioritization_dict[data_type]})
E           KeyError: 'object'


        2 things:

        # added "object" to prioritization?? - done

        TODO: this schema needs to trigger an "invalid/incomplete schema" exception
        """

        list_of_schema_inputs = [shopify_metafields_malformed
                                 ]
        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            assert schema_2_built_new_method



    def test_shopify_metafields_malformed_old_conversion(self):
        list_of_schema_inputs = [shopify_metafields_malformed
                                 ]
        for next_schema_input in list_of_schema_inputs:
            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties,
                                                         add_metadata=True)

            assert schema_3_built_old_method

    def test_shopify_metafields_do_results_match_fix_vs_malformed(self):

        msg_malformed = singer.parse_message(shopify_metafields_malformed)

        schema_malformed_built_old_method = build_schema_old(msg_malformed.schema, key_properties=msg_malformed.key_properties,
                                                     add_metadata=True)

        msg_fixed = singer.parse_message(shopify_metafields_fixed)

        schema_malformed_built_old_method = build_schema_old(msg_fixed.schema, key_properties=msg_fixed.key_properties,
                                                             add_metadata=True)

        assert schema_malformed_built_old_method == schema_malformed_built_old_method


    def test_shopify_metafields_do_results_match_old_vs_new_schema_translation(self):
        list_of_schema_inputs = [shopify_metafields_malformed, shopify_metafields_fixed
                                 ]

        for next_schema_input in list_of_schema_inputs:
            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties,
                                                         add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types

    def test_shopify_metafields_fixed_new_conversion(self):

        """
        replaced this :
            "value": {
                "type": [
                    "null",
                    "integer",
                    "object",
                    "string"
                ],
                "properties": {}
            }


        with this:
            "value": {
                "type": [
                    "null",
                    "integer",
                    "object",
                    "string"
                ]
            }


            removed "properties": {}

            still fails with this same error as above

            error:

            prioritization_dict = {"string": 1,
                       "number": 2,
                       "integer": 3,
                       "boolean": 4}

            anyOf_data_types = {}

        for i in range(0, len(field_property['anyOf'])):

            data_type = field_property['anyOf'][i]['type'][0]

>           anyOf_data_types.update({data_type: prioritization_dict[data_type]})
E           KeyError: 'object'


            succeeds if I add object and array to prioritization dict
                prioritization_dict = {"object": 0,
                           "array": 1,
                            "string": 2,
                           "number": 3,
                           "integer": 4,
                           "boolean": 5,
                           }


        """

        list_of_schema_inputs = [shopify_metafields_fixed
                                 ]
        for next_schema_input in list_of_schema_inputs:
            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)
            assert schema_2_built_new_method

    def test_shopify_order_refunds_new_conversion(self):

        """success"""

        list_of_schema_inputs = [shopify_order_refunds
                                 ]
        for next_schema_input in list_of_schema_inputs:
            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)
            assert schema_2_built_new_method


    def test_shopify_collects_new_conversion(self):

        """success"""

        list_of_schema_inputs = [shopify_collects
                                 ]
        for next_schema_input in list_of_schema_inputs:
            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)
            assert schema_2_built_new_method


    def test_schema_invalid_JSON(self):
        """
        supply invalid json file
        raises JSONDecodeError
        """
        schema_0_input = schema_nested_2_invalid_JSON

        # if you uncomment this line:
        # schema_0_input = schema_nested_2
        # this will fail the test: Failed: DID NOT RAISE <class 'simplejson.scanner.JSONDecodeError'>
        # because this is a valid schema

        with pytest.raises(simplejson.scanner.JSONDecodeError):
            msg = singer.parse_message(schema_0_input)

    def test_schema_completeness_validation_valid_input(self):

        for complete_schema in list_of_schema_inputs:

            validate_json_schema_completeness(complete_schema)

        assert True

    def test_schema_completeness_validation_empty_props(self):

        invalid_schemas = [invalild_schema_top_field_empty_props,
                           invalid_schema_subfield_empty_props,
                           invalid_schema_under_anyOf_empty_props_example_1,
                           invalid_schema_under_anyOf_deep_nested_empty_props,
                           shopify_metafields_malformed,
                           shopify_abandoned_checkouts_malformed]

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

            logcapture.check(expected_log,)
