def get_type(property):
    nullable = False
    prop_type = None

    if "anyOf" in property:
        return "anyOf", nullable
    elif "type" in property:
        prop_type = property["type"]
    else:
        raise ValueError(
            f"'type' or 'anyOf' are required fields in property: {property}"
        )

    if isinstance(prop_type, str):
        return prop_type, nullable

    field_type = None

    if isinstance(prop_type, list):
        for t in prop_type:
            if t.lower() == "null":
                nullable = True
            else:
                field_type = t

    return field_type, nullable


JSON_SCHEMA_LITERALS = {"boolean", "number", "integer", "string"}


def filter(schema, record):
    field_type, _ = get_type(schema)

    # return literals without checking
    if field_type in JSON_SCHEMA_LITERALS:
        return record
    elif field_type == "anyOf":
        for prop in schema["anyOf"]:
            prop_type, _ = get_type(prop)

            if prop_type == "null":
                continue

            # anyOf can be an array of properties, the choice here
            # is to ignore the case where anyOf is two types (not including "null")
            # and simply choose the first one. This might bite us.
            return filter(prop, record)

    elif field_type == "object":
        props = schema.get("properties", {})
        obj_results = {}
        for key, prop_schema in props.items():
            if key not in record:
                continue

            obj_results[key] = filter(prop_schema, record[key])

        return obj_results
    elif field_type == "array":
        props = schema.get("items", {})

        prop_type, _ = get_type(props)

        # array can contain either an object or literals
        # - if it contains literals, simply return those
        if prop_type != "object":
            return record

        arr_result = []
        for obj in record:
            arr_result.append(filter(props, obj))

        return arr_result
    else:
        raise ValueError(f"type {field_type} is unknown")


if __name__ == "__main__":
    schema = {
        "type": ["null", "object"],
        "properties": {
            "field1": {"type": ["string", "null"]},
            "an_object": {
                "anyOf": [
                    {"type": "object", "properties": {"k1": {"type": "string"}}},
                    {"type": "null"},
                ]
            },
        },
    }

    records = [
        {"field1": "yes!", "an_object": {"k2": "no!", "k1": "yes!"}, "field2": "no"},
        {"field1": "yes!", "field2": "no!"},
        {"field1": "yes!", "field2": "no!"},
    ]
    for record in records:
        print(filter(schema, record))

    schema = {
        "type": "array",
        "items": {
            "type": ["null", "object"],
            "properties": {"field1": {"type": ["string", "null"]}},
        },
    }
    records = [
        {"field1": "yes!", "field2": "no!"},
        {"field1": "yes!", "field2": "no!"},
        {"field1": "yes!", "field2": "no!"},
    ]
    print(filter(schema, records))
