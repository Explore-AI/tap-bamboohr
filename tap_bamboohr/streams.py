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
    selected = False

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
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        whos_out = self.client.fetch_whos_out()
        for who_out in whos_out:
            yield who_out


class TimeOffPolicies(Stream):
    """Create class for stream TimeOffPolicies from source
    that inherits from Stream class"""

    # Set variable name for stream - modify here if required
    stream_id = "time_off_policies"
    key_properties = ["id"]
    object_type = "TIME_OFF_POLICIES"
    replication_method = "FULL_TABLE"
    valid_replication_keys = ["id"]
    replication_key = "id"
    selected = False

    # Define sync function to get stream data per line
    def sync(self, *args, **kwargs):
        time_off_policies = self.client.fetch_time_off_policies()
        for time_off_policiy in time_off_policies:
            yield time_off_policiy           


# Dictionary containing all streams available.
STREAMS = {
    "employees": EmployeeDirectory,
    "whos_out": WhosOut,
    "time_off_policies": TimeOffPolicies
}
