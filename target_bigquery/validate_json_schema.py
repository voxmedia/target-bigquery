import re

def validate_json_schema_completeness(schema_input_as_string):
    """
    :param schema_input_as_string: JSON schema formatted as string
    if schema has empty "properties", "type" or "items", fail schema completeness validation check
    """
    # strip spaces from schema file (which is treated as text)
    schema_input_no_spaces = re.sub(' |\n', '', schema_input_as_string)

    completeness_validation_dict = {"properties": re.compile(r'\"properties\"\:\{\}'),
                                    "type": re.compile(r'\"type\"\:\[\]'),
                                    "items": re.compile(r'\"items\"\:\{\}')}
    # if there's empty props, type or items, then schema is incomplete and therefore invalid
    for schema_element, pattern_not_valid in completeness_validation_dict.items():

        if pattern_not_valid.search(schema_input_no_spaces):
            raise ValueError("JSON schema has missing {}".format(schema_element))