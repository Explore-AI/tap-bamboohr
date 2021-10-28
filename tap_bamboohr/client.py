import json
from PyBambooHR import PyBambooHR
import requests
from requests.auth import HTTPBasicAuth

class Client():
    """Class to make connection to BambooHR using the
    PyBambooHR package to send requests."""

    # Constructor for class BamboohrClient
    def __init__(self, api_key, subdomain):
        self._api_key = api_key
        self._subdomain = subdomain

        # Attributes for requests client
        self.timeout = 60
        self.headers = {}
        self.api_version = "v1"
        self.base_url = "https://api.bamboohr.com/api/gateway.php/{0}/{1}/".format(self._subdomain, self.api_version)
        
        # Instantiate connection object using api_key and subdomain path - for PyBambooHR client
        self._client= PyBambooHR.PyBambooHR(api_key=self._api_key, subdomain=self._subdomain)

    def fetch_employee_directory(self):
        # Retrieve json data of Employee Directory using method get_employee_directory()
        tap_data = self._client.get_employee_directory()
        return tap_data

    def fetch_whos_out(self):
        # Retrieve json data of Whos Out using method get_whos_out()
        tap_data = self._client.get_whos_out()
        return tap_data

    def get_time_off_policies(self):
        """
        API method for returning a list of time off policies.
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/meta/time_off/policies/"
        """
        # Set variables for stream API endpoint
        self.data_type = {"Accept": "application/json"}
        url = self.base_url + "meta/time_off/policies"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_time_off_policies(self):
        # Retrieve json data of Whos Out using method get_whos_out()
        tap_data = self.get_time_off_policies()
        return tap_data