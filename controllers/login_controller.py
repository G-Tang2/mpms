from views.login_view import LoginView
import csv

class LoginController():
    # initialise frame dictionary
    def __init__(self, master):
        self._set_controller(master)
        self._load_view(master)

    def _set_controller(self, master):
        master.main_controller = self

    def _load_view(self, master):
        new_frame = LoginView(master)
        if master.main_frame is not None:
            master.main_frame.destroy()
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)

    def login(self, username, password):
        with open("./app_data/accounts.csv", "r", encoding='utf-8') as f:
            f_reader = csv.reader(f)
            # skip header
            next(f_reader, None)
            # iterate through each account details in format - email address | password | type
            for account_details in f_reader:
                if account_details[:2] == [username.get(), password.get()]:
                    print("login successfully")
                    return
        print("Incorrect email and password")

    def registration(self):
        print("Registration page hasn't been implemented!")
