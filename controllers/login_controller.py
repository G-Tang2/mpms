from views.login_view import LoginView
import csv

class LoginController():
    def __init__(self, master):
        # master is an tk instance
        self._set_controller(master)
        self._load_view(master)

    def _set_controller(self, master):
        # set controller in tk instance
        master.main_controller = self

    def _load_view(self, master):
        # create new view
        new_frame = LoginView(master)
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)

    def login(self, email_address, password):
        with open("./app_data/accounts.csv", "r", encoding='utf-8') as f:
            f_reader = csv.reader(f)
            # skip header
            header = next(f_reader, None)
            # iterate through each account details in format - email address | password | type
            for account_details in f_reader:
                if account_details[:2] == [email_address.get(), password.get()]:
                    print("login successfully")
                    return
        print("Incorrect email and password")

    def registration(self):
        print("Registration page hasn't been implemented!")
