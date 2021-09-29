import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.__render_view(master)

    def __render_view(self, master: tk.Tk) -> None:
        # TODO: Include styling
        # declare variables
        email_address = tk.StringVar()
        password = tk.StringVar()

        # header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        # page title
        tk.Label(self, text="Log In").pack()
        tk.Label(self, text = "").pack()

        # email detail
        tk.Label(self, text = "Email").pack()
        tk.Entry(self, textvariable = email_address).pack()

        # password detail
        tk.Label(self, text = "Password").pack()
        tk.Entry(self, textvariable = password).pack()
        tk.Label(self, text = "").pack()
        
        # login button
        tk.Button(self, text = "Login", width=10, height=1, command = lambda: master.main_controller.login(email_address.get(), password.get())).pack()

    def display_email_error(self):
        tk.messagebox.showerror("Error", "Invalid email address or password")