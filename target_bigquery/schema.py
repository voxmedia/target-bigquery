import re

from google.cloud.bigquery import SchemaField

JSON_SCHEMA_LITERALS = {"boolean", "number", "integer", "string"}


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


def define_schema(field, name):
    schema_name = name
    schema_description = None
    schema_fields = ()

    field_type, nullable = get_type(field)

    if field_type == "anyOf":
        nullable = False
        props = field["anyOf"]
        # select first non-null property
        for prop in props:
            prop_type, prop_null = get_type(prop)
            # if any of the properties are nullable
            # they all are
            if prop_null:
                nullable = True

            # take the first property that is not None
            # of the possible types
            if field_type == "anyOf" and prop_type:
                field_type = prop_type

    if field_type == "object":
        schema_type = "RECORD"
        schema_fields = tuple(build_schema(field))
    elif field_type == "array":
        props = field.get("items")
        schema_type, _ = get_type(props)
        schema_mode = "REPEATED"
        return (
            schema_name,
            schema_type,
            schema_mode,
            schema_description,
            () if schema_type != "object" else build_schema(props),
        )
    elif field_type == "string" and "format" in field:
        format = field["format"]
        if format == "date-time":
            schema_type = "timestamp"
        elif format == "date":
            schema_type = "date"
    elif field_type == "number":
        schema_type = "FLOAT"

    schema_mode = "NULLABLE" if nullable else "required"
    if not schema_type:
        schema_type = field_type

    return (schema_name, schema_type, schema_mode, schema_description, schema_fields)


def bigquery_transformed_key(key):
    nodash = re.sub(r"-", "_", key)
    return re.sub(r"^\d+", "_", nodash)


def build_schema(schema):
    SCHEMA = []
    for key in schema["properties"].keys():

        if not (bool(schema["properties"][key])):
            # if we endup with an empty record.
            continue

        (
            schema_name,
            schema_type,
            schema_mode,
            schema_description,
            schema_fields,
        ) = define_schema(schema["properties"][key], bigquery_transformed_key(key))
        SCHEMA.append(
            SchemaField(
                schema_name, schema_type, schema_mode, schema_description, schema_fields
            )
        )

    return SCHEMA
