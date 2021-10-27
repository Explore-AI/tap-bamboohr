import singer

LOGGER = singer.get_logger()

class Stream:
    """Stream class to create streams source objects."""

    # Create default class variables 
    stream_id = None
    key_properties = []
    replication_method = ""
    valid_replication_keys = []
    replication_key = None
    object_type = ""

    # Create __init__() constructor for class
    def __init__(self, client, state):
        self.client = client
        self.state = state


class EmployeeDirectory(Stream):
    """ Create class for stream EmployeeDirectory from source
    that inherits from Stream class."""

    # Set variable names for stream - modify here if required
    stream_id = "employee_directory"
    key_properties = ["id"]
    object_type = "EMPLOYEE_DIRECTORY"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        employee_directory = self.client.fetch_employee_directory()
        for employeed in employee_directory:
            yield employeed      


class WhosOut(Stream):
    """Create class for stream WhosOut from source
    that inherits from Stream class"""

    # Set variable name for stream - modify here if required
    stream_id = "whos_out"
    key_properties = ["employeeId"]
    object_type = "WHOS_OUT"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["employeeId"]
    replication_key = "employeeId"

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        whos_out = self.client.fetch_whos_out()
        for who_out in whos_out:
            yield who_out


# Dictionary containing all streams available.
STREAMS = {
    "employees": EmployeeDirectory,
    "whos_out": WhosOut
}
