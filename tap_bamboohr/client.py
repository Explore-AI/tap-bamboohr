import json
from PyBambooHR import PyBambooHR

class BamboohrClient:
    """Class to make connection to BambooHR using the
    PyBambooHR package to send requests."""

    # Constructor for class BamboohrClient
    def __init__(self, api_key, subdomain):
        self._api_key = api_key
        self._subdomain = subdomain
        # Instantiate connection object using api_key and subdomain path
        self._client = PyBambooHR.PyBambooHR(api_key=self._api_key, subdomain=self._subdomain)

    def fetch_employee_directory(self):
        # Retrieve json data of Employee Directory using method get_employee_directory()
        tap_data = self._client.get_employee_directory()
        return tap_data

    def fetch_whos_out(self):
        # Retrieve json data of Whos Out using method get_whos_out()
        tap_data = self._client.get_whos_out()
        return tap_data