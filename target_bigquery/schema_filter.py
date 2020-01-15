def get_type(property):
    nullable = False

    if "type" not in property:
        raise ValueError(f"type not in property: {property}")

    prop_type = property["type"]

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
            "an_object": {"type": "object", "properties": {"k1": {"type": "string"}}},
        },
    }

    records = [
        {"field1": "yes!", "an_object": {"k2": "no!", "k1": "yes!"}},
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
