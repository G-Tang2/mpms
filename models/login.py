import csv
import json
from models.patient import Patient

class Login():
    def __init__(self, email_address: str, password: str) -> None:
        self.user = self.load_user(email_address, password)
        
    def load_user(self, email_address: str, password: str) -> "User":
        validation = self.valid_credentials(email_address, password)
        if validation["is_valid"]:
            if validation["account_type"] == "administrator":
                pass
            elif validation["account_type"] == "patient":
                return Patient(validation["user_detail"])
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
                # check if account details matches user login input
                if account_email_address == email_address and account_password == password:
                    return {"is_valid": True, "account_type": account_type, "user_detail": json.loads(account_user_detail)}
            return {"is_valid": False, "account_type": None, "user_detail": None}

    def is_patient(self):
        return isinstance(self.user, Patient)