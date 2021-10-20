import os
import json

# Import streams script from current directory
from .streams import STREAMS 

from singer.schema import Schema
from singer import utils, metadata
from singer.catalog import Catalog, CatalogEntry

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

        meta = metadata.to_list(meta)

        schemas[stream_name] = schema
        schemas_metadata[stream_name] = meta

    return schemas, schemas_metadata

# Tap discovery mode to retrieve schema and metadata info
def discover():
    schemas, schemas_metadata = _get_schemas_meta()


    # try schema_metadata.key_properties print

# def _load_schemas():
#     """ Load schemas from schemas folder """
#     schemas = {}

#     for filename in os.listdir(get_abs_path('schemas')):
#     path = get_abs_path('schemas') + '/' + filename
#     file_raw = filename.replace('.json', '')
#     with open(path) as file:
#         schemas[file_raw] = Schema.from_dict(json.load(file))


# def discover():
#     raw_schemas = load_schemas()
#     print("doing discover")
#     streams = []
#     for stream_id, schema in raw_schemas.items():
#         # TODO: populate any metadata and stream's key properties here..
#         # Need to add something here to get metadata - currently not working
#         stream_metadata = [{'selected': True}]
#         # stream_metadata = get_standard_metadata(schema="",
#         #                                         schema_name=stream_id,
#         #                                         key_properties=["id"],
#         #                                         valid_replication_keys=None,
#         #                                         replication_method=None)
        
#         # Assign the stream key property - primary key
#         key_properties = ['id']
#         streams.append(
#             CatalogEntry(
#                 tap_stream_id=stream_id,
#                 stream=stream_id,
#                 schema=schema,
#                 key_properties=key_properties,
#                 metadata=stream_metadata,
#                 replication_key=None,
#                 is_view=None,
#                 database=None,
#                 table=None,
#                 row_count=None,
#                 stream_alias=None,
#                 replication_method=None,
#             )
#         )
#     return Catalog(streams)