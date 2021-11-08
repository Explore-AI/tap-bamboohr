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

    def fetch_employee_id(self):
        # Retrieve json data of Employee for specified id using method get_employee()
        tap_data = self._client.get_employee(60)
        return tap_data

    # def fetch_all_employees(self):
    #     self.employee_fields = {
    #         "address1": ("text", "The employee's first address line"),
    #         "address2": ("text", "The employee's second address line"),
    #         "age": ("integer", "The employee's age. Not editable. To change update dateOfBirth, instead."),
    #         "bestEmail": ("email", "The employee's work email if set, otherwise their home email"),
    #         "birthday": ("text", "The employee's month and day of birth. Not editable. To change update dateOfBirth, instead."),
    #         "city": ("text", "The employee's city"),
    #         "country": ("country", "The employee's country"),
    #         "dateOfBirth": ("date", "The date the employee was born"),
    #         "department": ("list", "The employee's CURRENT department."),
    #         "division": ("list", "The employee's CURRENT division"),
    #         "eeo": ("list", "The employee's EEO job category. These are defined by the U.S. Equal Employment Opportunity Commission"),
    #         "employeeNumber": ("text", "Employee number (assigned by your company)"),
    #         "employmentStatus": ("status", "DEPRECATED. Please use 'status' instead. The employee's employee status (Active,Inactive)"),
    #         "employmentHistoryStatus": ("list", "The employee's CURRENT employment status. Options are customized by account."),
    #         "ethnicity": ("list", "The employee's ethnicity"),
    #         "exempt": ("list", "The FLSA employee exemption code (Exempt or Non-exempt)"),
    #         "firstName": ("text", "The employee's first name"),
    #         "flsaCode": ("list", "The employee's FLSA code. Ie: 'Exempt', 'Non-excempt'"),
    #         "fullName1": ("text", "Employee's first and last name. Example: John Doe. Ready only."),
    #         "fullName2": ("text", "Employee's last and first name. Example: Doe, John. Read only."),
    #         "fullName3": ("text", "Employee's full name with nickname. Example: Doe, John Quentin (JDog). Read only."),
    #         "fullName4": ("text", "employee's full name without nickname. Last name first. Example: Doe, John Quentin. Read only"),
    #         "fullName5": ("text", "employee's full name without nickname. First name first. Example: John Quentin Doe. Read only"),
    #         "displayName": ("text", "employee's name displayed in a format configured by the user. Read only"),
    #         "gender": ("gender", "The employee's gender. Legal values are 'Male', 'Female'"),
    #         "hireDate": ("date", "The date the employee was hired"),
    #         "homeEmail": ("email", "The employee's home email address"),
    #         "homePhone": ("phone", "The employee's home phone number"),
    #         "id": ("integer", "Employee id (automatically assigned by BambooHR). Not editable."),
    #         "jobTitle": ("list", "The CURRENT value of the employee's job title, updating this field will create a new row in position history"),
    #         "lastChanged": ("timestamp", "The date and time that the employee record was last changed"),
    #         "lastName": ("text", "The employee's last name"),
    #         "location": ("list", "The employee's CURRENT location"),
    #         "maritalStatus": ("list", "The employee's marital status ('Single' or 'Married')"),
    #         "middleName": ("text", "The employee's middle name"),
    #         "mobilePhone": ("phone", "The employee's mobile phone number"),
    #         "nickname": ("text", "The employee's nickname"),
    #         "payChangeReason": ("list", "The reason for the employee's last pay rate change."),
    #         "payGroup": ("list", "The custom pay group that the employee belongs to."),
    #         "payGroupId": ("integer", "The id value corresponding to the pay group that an employee belongs to"),
    #         "payRate": ("currency", "The employee's CURRENT pay rate. ie: $8.25"),
    #         "payRateEffectiveDate": ("date", "The date most recent change was made."),
    #         "payType": ("pay_type", "The employee's CURRENT pay type. ie: 'hourly','salary','commission','exception hourly','monthly','piece rate','contract','daily'"),
    #         "preferredName": ("text", "The employee's preferred name."),
    #         "ssn": ("ssn", "The employee's social security number"),
    #         "sin": ("sin", "The employee's Canadian Social Insurance Number"),
    #         "state": ("state", "The employee's state/province"),
    #         "stateCode": ("text", "The 2 character abbreviation for the employee's state (US only). Not editable."),
    #         "status": ("status", "'status' indicates whether you are using BambooHR to track data about this employee. Valid values are 'Active', 'Inactive'."),
    #         "supervisor": ("employee", "The emloyee’s CURRENT supervisor. Not editable."),
    #         "supervisorId": ("integer", "The 'employeeNumber' of the employee's CURRENT supervisor. Not editable."),
    #         "supervisorEId": ("integer", "The 'id' of the employee's CURRENT supervisor. Not editable."),
    #         "terminationDate": ("date", "The date the employee was terminated"),
    #         "workEmail": ("email", "The employee's work email address"),
    #         "workPhone": ("phone", "The employee's work phone number, without extension"),
    #         "workPhonePlusExtension": ("text", "The employee's work phone and extension. Not editable."),
    #         "workPhoneExtension": ("text", "The employees work phone extension (if any)"),
    #         "zipcode": ("text", "The employee's zipcode"),
    #         "photoUploaded": ("bool", "The employee has uploaded a photo"),
    #         "isPhotoUploaded": ("bool", "The employee has uploaded a photo"),
    #         "rehireDate": ("date", "The date the employee was rehired"),
    #         "adpCompanyCode": ("list", ""),
    #         "adpFileNumber": ("text", ""),
    #         "standardHoursPerWeek": ("integer", ""),
    #         "earningsDate": ("date", ""),
    #         "earningsPriorYear": ("currency", ""),
    #         "bonusDate": ("date", ""),
    #         "bonusAmount": ("currency", ""),
    #         "bonusReason": ("list", ""),
    #         "bonusComment": ("text", ""),
    #         "commisionDate": ("date", ""),
    #         "commissionAmount": ("currency", ""),
    #         "commissionComment": ("text", ""),
    #         "commissionComment": ("text", ""),
    #         "benefitClassDate": ("date", ""),
    #         "benefitClassClass": ("list", ""),
    #         "benefitClassChangeReason": ("list", ""),
    #     }
    #     # Retrieve json data of all Employees with selected fields using method get_all_employees()
    #     tap_data = self._client.get_all_employees(field_list=self.employee_fields)
    #     return tap_data

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