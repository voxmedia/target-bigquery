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


def filter(schema, record):
    field_type, _ = get_type(schema)

    # return literals without checking
    if field_type in {"boolean", "number", "integer", "string"}:
        return record

    elif field_type == "object":
        properties = schema.get("properties", {})
        obj_results = {}
        for key, prop_schema in properties.items():
            if key not in record:
                continue

            prop_type, _ = get_type(prop_schema)

            # return literals without checking
            if prop_type in {"boolean", "number", "integer", "string"}:
                obj_results[key] = record[key]
            else:
                obj_results[key] = filter(prop_schema, record[key])

        return obj_results

    elif field_type == "array":
        prop_schema = schema["items"]

        prop_type, _ = get_type(prop_schema)

        # if type is a literal, return list of literals
        # without further consideration
        if prop_type != "object":
            return record

        arr_result = []
        for obj in record:
            arr_result.append(filter(prop_schema, obj))

        return arr_result
    else:
        raise ValueError("type is neither object or array")


if __name__ == "__main__":
    schema = {
        "type": ["null", "object"],
        "properties": {"field1": {"type": ["string", "null"]}},
    }

    records = [
        {"field1": "yes!", "field2": "no!"},
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

