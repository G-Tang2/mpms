import tkinter as tk
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from controllers.controller import Controller
from views.login_view import LoginView
import csv

class LoginController(Controller):
    def __init__(self,master,view = LoginView):
        Controller.__init__(self,master,view)

    def login(self, email_address: str, password: str):
        with open("./app_data/accounts.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.reader(f)
            header = next(f_reader, None)

            # find index of email address and password in header
            email_address_index = header.index("email_address")
            password_index = header.index("password")
            type_index = header.index("type")

            for account_details in f_reader:
                # extract account email address and password
                account_email_address = account_details[email_address_index]
                account_password = account_details[password_index]
                account_type = account_details[type_index]
                # check if account details matches user login input
                if account_email_address == email_address and account_password == password:
                    if account_type == 'administrator':
                        self._master.load_controller(AdminHomeController)
                        print("login successfully")
                    elif account_type == 'patient':
                        self._master.load_controller(PatientHomeController)
                        print("login successfully")
                    return

        # TODO: Implement error feedback in view
        print("Incorrect email and password")

    def registration(self):
        print("Registration page hasn't been implemented!")
