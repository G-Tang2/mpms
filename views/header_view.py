import tkinter as tk
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from controllers.login_controller import LoginController

class Header(tk.Frame):
    def __init__(self, master: tk.Tk):
        tk.Frame.__init__(self, master)
        # header
        header_frame = tk.LabelFrame(self)
        tk.Button(header_frame, text="   Monash Clinic", relief = 'flat', command = lambda: master.header_controller.return_home(),borderwidth= 0, highlightthickness = 0 , font=('Roboto',38, "bold"), anchor="w", bg="red").pack(side = "left", ipady=5)      
        tk.Button(header_frame, text = "Logout", relief = 'flat', command = lambda: master.header_controller.logout(),borderwidth= 0, highlightthickness = 0 , font=('Roboto',38, "bold"), anchor="w", bg="#99d2f2").pack(side = "right", ipady=5)
        header_frame.pack(fill = 'x')
        # divider
        tk.Frame(self, bg="black", height=2).pack(side = "bottom", fill="x")
        
    
