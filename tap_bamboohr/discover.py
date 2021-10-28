import os
import json

# Import streams script from current directory
from .streams import STREAMS 

from singer.schema import Schema
from singer import utils, metadata
from singer.catalog import Catalog

# from singer.metadata import get_standard_metadata

# Retrieve path to schems folder directory
def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

# Load predefined schemas of streams and get metadata
def _get_schemas_meta():
    """ Load schemas from schemas folder """
    schemas = {}
    schemas_metadata = {}

    for stream_name, stream_object in STREAMS.items():
        schema_path = get_abs_path("schemas/{}.json".format(stream_name))
        with open(schema_path) as file:
            schema = json.load(file)
        
        meta = metadata.get_standard_metadata(
            schema=schema,
            key_properties=stream_object.key_properties,
            replication_method=stream_object.replication_method
        )

        meta = metadata.to_map(meta)

        if stream_object.valid_replication_keys:
            meta = metadata.write(meta, (), "valid-replication-keys", stream_object.valid_replication_keys)
        
        if stream_object.replication_key:
            meta = metadata.write(meta, ("properties", stream_object.replication_key), "inclusion", "automatic")
        
        # Add metadata for stream selection - default is false
        if stream_object.selected ==  False:
            meta = metadata.write(meta, (), "selected", stream_object.selected)

        meta = metadata.to_list(meta)

        schemas[stream_name] = schema
        schemas_metadata[stream_name] = meta

    return schemas, schemas_metadata

# Tap discovery mode to retrieve schema and metadata info
def discover():
    schemas, schemas_metadata = _get_schemas_meta()
    streams = []

    # Get each schema and schema_metadata to create Catalog file
    for schema_name, schema in schemas.items():
        schema_meta = schemas_metadata[schema_name]
        
        # Catalog format
        catalog_entry = {
            "stream": schema_name,
            "tap_stream_id": schema_name,
            "schema": schema,
            "metadata":schema_meta
        }

        streams.append(catalog_entry)

    return Catalog.from_dict({"streams": streams})
