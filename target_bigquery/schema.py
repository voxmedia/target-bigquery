import re

from google.cloud.bigquery import SchemaField

def defineArrayType(field, name):
    schema_type = field.get("items").get("type")
    schema_mode = "REPEATED"
    schema_description = None
    schema_fields = ()
    if schema_type == "array":
        return defineArrayType(field["items"], name)
    if isinstance(schema_type, list):
        if "array" in schema_type:
            return defineArrayType(field["items"], name)

        if "null" in schema_type and schema_type.index("null") != 0:
            schema_type.remove("null")
            schema_type.insert(0, "null")
            schema_type = schema_type[-1]
        else:
            schema_type = schema_type[-1]

    if schema_type == "object":
        schema_type = "RECORD"
        schema_fields = tuple(build_schema(field.get("items")))

    return (name, schema_type, schema_mode, schema_description, schema_fields)


def define_schema(field, name):
    schema_name = name
    schema_type = "STRING"
    schema_mode = "NULLABLE"
    schema_description = None
    schema_fields = ()

    if "type" not in field and "anyOf" in field:
        for types in field["anyOf"]:
            if types["type"] == "null":
                schema_mode = "NULLABLE"
            else:
                field = types

    if isinstance(field["type"], list):
        types = set(field["type"])
        if "null" in types:
            schema_mode = "NULLABLE"
            types.remove("null")
        else:
            schema_mode = "required"
        single_type = list(types)
        schema_type = single_type[-1]
    else:
        schema_type = field["type"]

    if schema_type == "object":
        schema_type = "RECORD"
        schema_fields = tuple(build_schema(field))

    if schema_type == "string":
        if "format" in field:
            if field["format"] == "date-time":
                schema_type = "timestamp"
            if field["format"] == "date":
                schema_type = "date"

    if schema_type == "number":
        schema_type = "FLOAT"

    if schema_type == "array":
        return defineArrayType(field, name)

    return (schema_name, schema_type, schema_mode, schema_description, schema_fields)


def bigquery_transformed_key(key):
    if re.search(r"\.|-", key):
        return re.sub(r"\.|-", "_", key)
    elif re.search(r"^\d", key):
        return re.sub(r"^\d.+", f"_{key}", key)
    else:
        return key


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
