import singer
from singer.schema import Schema

# Import client script from current directory
from .client import Client
# Import streams script from current directory
from .streams import STREAMS

from singer import Transformer, metadata

LOGGER = singer.get_logger()

def sync(config, state, catalog):
    """
    Method to sync data from tap source.
    """

    # Call client script file to create client to submit request for data to source BambooHR
    client = Client(api_key=config["api_key"], subdomain=config["subdomain"])
 
    # Singer tool - Applies schema (and integer_datetime_fmt, if supplied) to data, transforming
    # each field in data to the type specified in schema. If no type matches a
    # data field, this throws an Exception.
    with Transformer() as transformer:
        for stream in catalog.get_selected_streams(state):
            tap_stream_id = stream.tap_stream_id
            stream_obj = STREAMS[tap_stream_id](client, state)
            replication_key = stream_obj.replication_key
            stream_schema = stream.schema.to_dict()
            stream_metadata = metadata.to_map(stream.metadata)
            # print("5", stream_metadata[()]["selected"])

            LOGGER.info("Syncing stream:" + stream.tap_stream_id)

            # Get info from state.json file and write state message - as stdout
            state = singer.set_currently_syncing(state, tap_stream_id)
            singer.write_state(state)

            # Write schema message - as stdout   
            singer.write_schema(
                tap_stream_id,
                stream_schema,
                stream_obj.key_properties,
                stream.replication_key
            )

            for record in stream_obj.sync():
                # Get correct format as per singer specs
                transformed_record = transformer.transform(record, stream_schema, stream_metadata)

                LOGGER.info(f"Writing record: {transformed_record}")
                
                # Write record message - as stdout
                singer.write_record(
                    tap_stream_id,
                    transformed_record
                )

            # Singer tool to remove bookmark state and update state
            state = singer.clear_bookmark(state, tap_stream_id, "cursor")
            singer.write_state(state)
    
    # Sync with updated state file and write final state message
    state = singer.set_currently_syncing(state, None)
    singer.write_state(state)
                