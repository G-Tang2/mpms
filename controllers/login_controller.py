import tkinter as tk
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from controllers.controller import Controller
from views.login_view import LoginView
import csv

class LoginController(Controller):
    def __init__(self,master):
        Controller.__init__(self,master,LoginView)

    def login(self, email_address: str, password: str):
        with open("./app_data/accounts.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.reader(f)
            header = next(f_reader, None)
            # find index of email address and password in header
            email_address_index = header.index("email_address")
            password_index = header.index("password")
            for account_details in f_reader:
                # extract account email address and password
                account_email_address = account_details[email_address_index]
                account_password = account_details[password_index]
                # check if account details matches user login input
                if account_email_address == email_address and account_password == password:
                    print("login successfully")
                    #self.__master.load_controller(PatientHomeController)
                    return
        # TODO: Implement error feedback in view
        print("Incorrect email and password")

    def registration(self):
        print("Registration page hasn't been implemented!")
