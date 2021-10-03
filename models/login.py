import csv
import json
from models.user import User
from models.patient import Patient
from models.admin import Admin

class Login():
    def __init__(self, email_address: str, password: str) -> None:
        self.user = self.load_user(email_address, password)
        
    def load_user(self, email_address: str, password: str) -> User:
        res = self.valid_credentials(email_address, password)
        if res["is_valid"]:
            if res["account_type"] == "administrator":
                return Admin(res["user_details"])
            elif res["account_type"] == "patient":
                return Patient(res["user_details"])
            else:
                # TODO: Throw error
                print("Invalid account type")
        else:
            raise ValueError("Invalid email address or password")

    def valid_credentials(self, email_address: str, password: str) -> bool:
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
                account_type = account_details[type_index]
                account_user_detail = account_details[user_detail_index]

                # pack email address and password into user details
                user_details = json.loads(account_user_detail)
                user_details["email_address"] = email_address
                user_details["password"] = password

                # check if account details matches user login input
                if account_email_address == email_address and account_password == password:
                    return_dict = {
                        "is_valid": True,
                        "account_type": account_type,
                        "user_details": user_details
                    }
                    return return_dict
            return_dict = {
                "is_valid": False,
                "account_type": None,
                "user_detail": None
            }
            return return_dict

    def is_patient(self):
        return isinstance(self.user, Patient)