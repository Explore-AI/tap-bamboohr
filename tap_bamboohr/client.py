import json

from requests.api import head
from PyBambooHR import PyBambooHR
import requests

class Client():
    """Class to make connection to BambooHR using the
    PyBambooHR package to send requests."""

    # Constructor for class BamboohrClient
    def __init__(self, api_key, subdomain):
        self._api_key = api_key
        self._subdomain = subdomain

        # Attributes for requests client
        self.data_type = {"Accept": "application/json"}
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

    def fetch_all_employees(self):
        custom_fields = {
            "employeeNumber": "",
            "firstName": "",
            "lastName": "",
            "jobTitle": "",
            "department": "",
            "location": "",
            "division": "",
            "supervisor": "",
            "age": "",
            "gender": "",
            "hireDate": "",
            "terminationDate": "",
            "employeeStatusDate": "",
            "employmentHistoryStatus": "",
            "4313": "",
            "4314": "",
            "payRate": "",
            "payPer": "",
            "paySchedule": "",
            "payChangeReason": "",
            "4045": "",
            "ethnicity": ""
        }

        add_fields = {
            "employeeStatusDate": ("date", "The date the employee was hired"),
            "4313": ("text", "Termination type of employee"),
            "4314": ("text", "Termination reason of employee"),
            "payPer": ("text", "Pay per time"),
            "paySchedule": ("text", "Pay schedule of employee, frequency"),
            "4045": ("text", "Employee compensation comments")
        }

        self._client.employee_fields.update(add_fields)
        
        # Retrieve json data of all Employees with selected fields using method get_all_employees()
        tap_data = self._client.get_all_employees(field_list=custom_fields, disabledUsers=True, reloadEmployees=True)
        return tap_data

    def fetch_whos_out(self):
        # Retrieve json data of Whos Out using method get_whos_out()
        tap_data = self._client.get_whos_out()
        return tap_data

    def fetch_meta_fields(self):
        # Retrieve json data of Meta Fields using method get_meta_fields()
        tap_data = self._client.get_meta_fields()
        return tap_data

    def get_time_off_policies(self):
        """
        API method for returning a list of time off policies.
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/meta/time_off/policies/"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "meta/time_off/policies"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_time_off_policies(self):
        # Retrieve json data of Time Off Policies using method get_time_off_policies()
        tap_data = self.get_time_off_policies()
        return tap_data

    def get_benefit_deduc_types(self):
        """
        API method for returning a list of benefit deduction types
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefits/settings/deduction_types/all"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefits/settings/deduction_types/all"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_deduc_types(self):
        # Retrieve json data of Benefit Deduction Types using method get_benefit_deduc_types()
        tap_data = self.get_benefit_deduc_types()
        return tap_data

    def get_benefit_coverages(self):
        """
        API method for returning a list of benefit coverages
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefitcoverages"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefitcoverages"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_coverages(self):
        # Retrieve json data of Benefit Coverages using method get_benefit_coverages()
        tap_data = self.get_benefit_coverages()
        return tap_data

    def get_empl_dependents(self):
        """
        API method for returning a list of all employee dependents
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/employeedependents"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "employeedependents"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_empl_dependents(self):
        # Retrieve json data of Employee Dependents using method get_empl_dependents()
        tap_data = self.get_empl_dependents()
        return tap_data 

    def get_benefit_plans(self):
        """
        API method for returning a list of all benefit plans
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefitplans"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefitplans"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_plans(self):
        # Retrieve json data of Benefits Plans using method get_benefit_plans()
        tap_data = self.get_benefit_plans()
        return tap_data

    def get_benefit_groups(self):
        """
        API method for returning a list of all benefit groups
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefitgroups"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefitgroups"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_groups(self):
        # Retrieve json data of Benefits Groups using method get_benefit_groups()
        tap_data = self.get_benefit_groups()
        return tap_data

    def get_benefit_group_empls(self):
        """
        API method for returning a list of all benefit group employees
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefitgroupemployees"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefitgroupemployees"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_group_empls(self):
        # Retrieve json data of Benefit Group Employees using method get_benefit_group_empls()
        tap_data = self.get_benefit_group_empls()
        return tap_data

    def get_benefit_group_plans(self):
        """
        API method for returning a list of all benefit group plans
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefitgroupplans"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefitgroupplans"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_group_plans(self):
        # Retrieve json data of Benefit Group Plans using method get_benefit_group_plans()
        tap_data = self.get_benefit_group_plans()
        return tap_data

    def get_benefit_costs(self):
        """
        API method for returning a list of all benefit group plan costs
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/benefitgroupplancosts"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "benefitgroupplancosts"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_benefit_costs(self):
        # Retrieve json data of Benefit Group Plan Costs using method get_benefit_costs()
        tap_data = self.get_benefit_costs()
        return tap_data

    def get_training_types(self):
        """
        API method for returning a list of training types
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/training/type"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "training/type"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_training_types(self):
        # Retrieve json data of Training Types using method get_training_types()
        tap_data = self.get_training_types()
        return tap_data      

    def get_training_categories(self):
        """
        API method for returning a list of training categories
        "https://api.bamboohr.com/api/gateway.php/companyDomain/v1/training/category"
        """
        # Set variables for stream API endpoint
        url = self.base_url + "training/category"
        self.headers.update(self.data_type)

        r = requests.get(url, timeout=self.timeout, headers=self.headers, auth=(self._api_key, ""))
        r.raise_for_status()
        data = r.json()
        return data

    def fetch_training_categories(self):
        # Retrieve json data of Training Categories using method get_training_categories()
        tap_data = self.get_training_categories()
        return tap_data