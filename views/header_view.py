import tkinter as tk
from models.MPMS import MPMS
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from controllers.login_controller import LoginController

class Header(tk.Frame):
    def __init__(self, master: tk.Tk):
        tk.Frame.__init__(self, master)
        self.logout_image = tk.PhotoImage(file = 'images/download.png')
        # header
        self.header_frame = tk.Frame(self,bg='white')
        tk.Button(self.header_frame, text="   Monash Clinic", relief = 'flat',borderwidth= 0, highlightthickness = 0 , font=('Roboto',38, "bold"), anchor="w", bg="white",
            command = lambda: master.header_controller.return_home()).pack(side = "left", ipady=5)
        self.header_frame.pack(fill = 'x')

        # divider
        tk.Frame(self, bg="black", height=2).pack(side = "bottom", fill="x")

        # logout button
        self.logout_btn = tk.Button(self.header_frame, image = self.logout_image, relief = 'flat', 
            command = lambda: master.header_controller.logout(),borderwidth= 0, highlightthickness = 0 , height = 5, anchor="w", bg="#99d2f2")
    
    def display_logout_btn(self):
        self.logout_btn.pack(fill = 'x',side = "right", ipady=5, padx = 10) 
    
    def hide_logout_btn(self):
        self.logout_btn.pack_forget()

    def return_confirmation(self):
        confirmation = tk.messagebox.askyesno(title='Confirmation', message='Leave and Discard Changes?')
        return confirmation

        #self.header_frame.pack_forget()
        #tk.Button(self.header_frame, image = self.logout_image, relief = 'flat', 
         #   command = lambda: self.master.header_controller.logout(),borderwidth= 0, highlightthickness = 0 , height = 5, anchor="w", bg="#99d2f2").pack(side = "right", ipady=5)
        #self.header_frame.pack(fill = 'x')

    
