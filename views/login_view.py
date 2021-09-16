import tkinter as tk
import csv

class LoginView(tk.Frame):
    def __init__(self, master):
        # initialise frame and set controller
        tk.Frame.__init__(self, master, width=1200, height=800)

        # declare variables
        username = tk.StringVar()
        password = tk.StringVar()

        # page title
        tk.Label(self, text="Log In").pack()
        tk.Label(self, text = "").pack()

        # email detail
        tk.Label(self, text = "Email").pack()
        tk.Entry(self, textvariable = username).pack()

        # password detail
        tk.Label(self, text = "Password").pack()
        tk.Entry(self, textvariable = password).pack()
        tk.Label(self, text = "").pack()
        # login button
        tk.Button(self, text = "Login", width=10, height=1, command = lambda: self.login(username, password)).pack()

        # sign up button
        tk.Button(self, text = "Sign Up", width=10, height=1, command = self.registration).pack()

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