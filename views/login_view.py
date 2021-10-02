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
        tk.Label(self, text="Monash Clinic", font=('Roboto',38, "bold"), anchor="w").pack(padx=100, pady=15, fill="x")

        # page title
        tk.Label(self, text="Log In", font=('Roboto',28, "bold")).pack(pady=(100, 60))

        frame1 = tk.LabelFrame(self, relief="flat")

        # email detail
        tk.Label(frame1, text = "Email", anchor="w").pack(padx=25, fill="x")
        tk.Entry(frame1, font=('Roboto',14), textvariable = email_address).pack(padx=25, fill="x")

        # password detail
        tk.Label(frame1, text = "Password", anchor="w").pack(padx=25, pady=(15, 0), fill="x")
        tk.Entry(frame1, font=('Roboto',14), textvariable = password).pack(padx=25, fill="x")
        
        # login button
        tk.Button(frame1, text = "Login", width=10, height=1, command = lambda: master.main_controller.login(email_address.get(), password.get())).pack(pady=25)

        frame1.pack(padx=450, fill="x")

    def display_email_error(self, message: str):
        tk.messagebox.showerror("Error", message)