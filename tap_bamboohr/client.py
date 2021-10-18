import json
from PyBambooHR import PyBambooHR

class BamboohrClient:
    """Class to make connection to BambooHR using the
    PyBambooHR package to send requests."""

    def fetch_employee_directory(self, subdomain, api_key):
        
        # Instantiate connection object using api_key and subdomain path
        bamboo = PyBambooHR.PyBambooHR(subdomain=config["subdomain"], api_key=config["api_key"])

        # Retrieve json data of Employee Directory using method get_employee_directory()
        tap_data = bamboo.get_employee_directory()
        return tap_data