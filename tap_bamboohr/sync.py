import singer
from singer.schema import Schema

# Import client script from current directory
from .client import BamboohrClient
# Import streams script from current directory
from .streams import STREAMS

from singer import metadata

LOGGER = singer.get_logger()

def sync(config, state, catalog):
    """
    Method to sync data from tap source.
    """

    # Call client script file to create client to submit request for data to source BambooHR
    client = BamboohrClient(api_key=config["api_key"], subdomain=config["subdomain"])
    print("retrieved client")

    # Loop over selected streams in catalog
    print('here 3 - running sync')
    for stream in catalog.get_selected_streams(state):
        tap_stream_id = stream.tap_stream_id
        stream_obj = STREAMS[tap_stream_id](client, state)
        print(stream_obj)
        print(stream_obj.key_properties)
        replication_key = stream_obj = stream_obj.replication_key
        stream_schema = stream.schema.to_dict()
        stream_metadata = metadata.to_map(stream.metadata)
        # print("5", stream_metadata[()]["selected"])

        LOGGER.info("Syncing stream:" + stream.tap_stream_id)

        # Get info from state.json file and write state message - as stdout
        state = singer.set_currently_syncing(state, tap_stream_id)
        singer.write_state(state)

        # Write schema message - as stdoud       
        singer.write_schema(
            tap_stream_id,
            stream_schema,
            stream_obj.key_properties,
            stream.replication_key
        )
        exit()
        for record in stream_obj.sync():
            print("end")


# def sync(config, state, catalog):
#     """ Sync data from tap source """
    
#     # Call client script file to create client to submit request for data to source BambooHR
#     client = BamboohrClient(api_key=config["api_key"], subdomain=config["subdomain"])
#     print("retrieved client")
     
#     # Loop over selected streams in catalog
#     print('here 3 - running sync')
#     for stream in catalog.get_selected_streams(state):
#         print('here 4')
#         LOGGER.info("Syncing stream:" + stream.tap_stream_id)

#         bookmark_column = stream.replication_key
#         is_sorted = True  # TODO: indicate whether data is sorted ascending on bookmark value

#         # singer.write_schema(
#         #     stream_name=stream.tap_stream_id,
#         #     schema=stream.schema,
#         #     key_properties=stream.key_properties,
#         # )

#         # # TODO: delete and replace this inline function with your own data retrieval process:
#         # tap_data = lambda: [{"id": x, "name": "row${x}"} for x in range(1000)]

#         # Instantiate connection object using api_key and subdomain path
#         bamboo = PyBambooHR.PyBambooHR(subdomain=config["subdomain"], api_key=config["api_key"])
        
#         # Retrieve json data of Employee Directory using method get_employee_directory()
#         tap_data = bamboo.get_employee_directory()

#         max_bookmark = None
#         for row in tap_data:
#             # TODO: place type conversions or transformations here

#             # write one or more rows to the stream:
#             singer.write_records(stream.tap_stream_id, [row])
#             if bookmark_column:
#                 if is_sorted:
#                     # update bookmark to latest value
#                     singer.write_state({stream.tap_stream_id: row[bookmark_column]})
#                 else:
#                     # if data unsorted, save max value until end of writes
#                     max_bookmark = max(max_bookmark, row[bookmark_column])
#         if bookmark_column and not is_sorted:
#             singer.write_state({stream.tap_stream_id: max_bookmark})
    # return