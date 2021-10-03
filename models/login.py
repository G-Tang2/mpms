import csv
import json
from datetime import datetime
from models.user import User
from models.patient import Patient
from models.admin import Admin

class Login():
    def __init__(self, email_address: str, password: str) -> None:
        self.user = self.load_user(email_address, password)
        
    def load_user(self, email_address: str, password: str) -> User:
        is_valid_user, account_type, account_details = self.valid_credentials(email_address, password)
        if is_valid_user:
            if account_type == "administrator":
                return Admin(account_details)
            elif account_type == "patient":
                return Patient(account_details)
            else:
                ValueError("Invalid user. You are not an administrator or a patient.")
        else:
            raise ValueError("Invalid email address or password.")

    def valid_credentials(self, email_address: str, password: str) -> bool:
        # default values
        is_valid_user = False
        account_type = None
        account_details = None
        with open("./app_data/accounts.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.reader(f)
            header = next(f_reader, None)

            # find index of email address and password in header
            email_address_index = header.index("email_address")
            password_index = header.index("password")
            type_index = header.index("type")
            user_detail_index = header.index("user")

            for account_details in f_reader:
                # extract account email address and password
                account_email_address = account_details[email_address_index]
                account_password = account_details[password_index]

                # check if account details matches user login input
                if account_email_address == email_address and account_password == password:
                    is_valid_user = True
                    account_type = account_details[type_index]
                    account_user_detail = account_details[user_detail_index]

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