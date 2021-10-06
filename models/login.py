import csv
import json
from datetime import datetime
from models.user import User
from models.patient import Patient
from models.admin import Admin

class Login():
    def __init__(self, email_address: str, password: str) -> None:
        self.user = self._load_user(email_address, password)
        
    def _load_user(self, email_address: str, password: str) -> User:
        is_valid_user, account_type, account_details = self._valid_credentials(email_address, password)
        if is_valid_user:
            if account_type == "administrator":
                return Admin.create_from_json(account_details)
            elif account_type == "patient":
                return Patient.create_from_json(account_details)
            else:
                ValueError("Invalid user. You are not an administrator or a patient.")
        else:
            raise ValueError("Invalid email address or password.")

    def _valid_credentials(self, email_address: str, password: str) -> bool:
        # default values
        is_valid_user = False
        account_type = None
        account_details = None
        with open("./app_data/accounts.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.DictReader(f)
            for user in f_reader:
                if user["email_address"] == email_address and user["password"] == password:
                    is_valid_user = True
                    account_type = user["type"]
                    account_user_detail = user["user_details"]

                    # pack email address and password into user details and format date of birth
                    account_details = json.loads(account_user_detail)
                    account_details["email_address"] = email_address
                    account_details["password"] = password
                    if "date_of_birth" in account_details:
                        account_details["date_of_birth"] = datetime.strptime(account_details["date_of_birth"], "%d/%m/%Y").date()
                    break
            
            return is_valid_user, account_type, account_details

    def is_patient(self):
        return isinstance(self.user, Patient)