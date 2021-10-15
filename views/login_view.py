import tkinter as tk

from controllers.login_controller import LoginController

class LoginView(tk.Frame):
    def __init__(self, master: tk.Tk, controller: LoginController) -> None:
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller

    def render_view(self) -> None:
        '''
        Create UI components to be displayed
        '''
        # declare variables
        email_address = tk.StringVar()
        password = tk.StringVar()

        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        # page title
        tk.Label(outer_label_frame, text="Log In", font=('Roboto',28, "bold"), bg="white").pack(pady=(50, 60))

        # wrapper for login details
        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")

        # email detail
        tk.Label(inner_label_frame, text = "Email", font=('Roboto',12), anchor="w", bg="white").pack(padx=25, fill="x")
        tk.Entry(inner_label_frame, borderwidth=2, relief="solid", textvariable = email_address).pack(padx=25, fill="x")

        # password detail
        tk.Label(inner_label_frame, text = "Password", font=('Roboto',12), anchor="w", bg="white").pack(padx=25, pady=(15, 0), fill="x")
        tk.Entry(inner_label_frame, show="*", borderwidth=2, relief="solid", textvariable = password).pack(padx=25, fill="x")
        
        # login button
        tk.Button(inner_label_frame, text = "Log In", borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0",
            command = lambda: self.controller.login(email_address.get(), password.get())).pack(ipadx=10, pady=(35, 45))

        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

    def display_email_error(self, message: str) -> None:
        '''
        Displays error message
        '''
        tk.messagebox.showerror("Error", message)