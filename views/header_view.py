import tkinter as tk
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController

class Header(tk.Frame):
    def __init__(self, master: tk.Tk):
        tk.Frame.__init__(self, master)
        # header
        tk.Button(self, text="   Monash Clinic", relief = 'flat', command = lambda: self.return_home(),borderwidth= 0, font=('Roboto',38, "bold"), anchor="w", bg="#FFFFFF").pack(ipady=10, fill="x")      
        # divider
        tk.Frame(self, bg="black", height=2).pack(fill="x")
        

    def return_home(self):
        if self.master.login.is_patient():
            self.master.load_controller(PatientHomeController) 
            print("Patient")
        else:
            self.master.load_controller(AdminHomeController) 
            print("Admin")