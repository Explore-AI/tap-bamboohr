import singer

LOGGER = singer.get_logger()

## For Employees_Directory
# endpoint = https://api.bamboohr.com/api/gateway.php/{{CompanyDomain}}/v1/employees/directory
# CompanyDomain = dcin42
# no query paramaters
# primary key = "id"
# metadata  = ???

class Stream:
    """Stream class to create streams source objects."""

    # Create default class variables 
    stream_id = None
    key_properties = []
    replication_method = ""
    valid_replication_keys =[]
    replication_key = None
    object_type = ""

    # Create __init__() constructor for class
    # Check if possible config required
    def __init__(self, client, state):
        self.client = client
        self.state = state


class EmployeeDirectory(Stream):
    """ Create class for stream EmployeeDirectory from source
    that inherits from Stream class."""

    # Set variable names for stream
    stream_id = "employee_directory"
    key_properties = ["id"]
    object_type = "EMPLOYEE_DIRECTORY"
    replication_method = "FULL_TABLE"

    # Define sync function to get stream data
    def sync(self, *args, **kwargs):
        response = self.client.fetch_employee_directory()



