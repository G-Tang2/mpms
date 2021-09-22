import tkinter as tk
from controllers.patient_home_controller import PatientHomeController
from views.login_view import LoginView
import csv
from controllers.patient_home_controller import PatientHomeController

class LoginController():
    def __init__(self, master: tk.Tk) -> None:
        # master is an tk instance
        self.__set_controller(master)
        self.__load_view(master)
        self.__master = master

    def __set_controller(self, master: tk.Tk) -> None:
        # set controller in tk instance
        master.main_controller = self

    def __load_view(self, master: tk.Tk) -> None:
        # create new view
        new_frame = LoginView(master)
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)

    def __load_controller(self, controller):
        controller(self.__master)

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
                if account_email_address == email_address.get() and account_password == password.get():
                    print("login successfully")
                    self.__load_controller(PatientHomeController)
                    return
        # TODO: Implement error feedback in view
        print("Incorrect email and password")

    def registration(self):
        print("Registration page hasn't been implemented!")
