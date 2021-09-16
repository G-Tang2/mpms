import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, master):
        # initialise frame and set controller
        tk.Frame.__init__(self, master, width=1200, height=800)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)

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
        tk.Button(self, text = "Login", width=10, height=1, command = lambda: master.main_controller.login(username, password)).pack()

        # sign up button
        tk.Button(self, text = "Sign Up", width=10, height=1, command = master.main_controller.registration).pack()

    