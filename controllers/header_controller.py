import tkinter as tk
from controllers.controller import Controller
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from models.MPMS import MPMS
from views.header_view import Header
from views.login_view import LoginView
from models.login import Login
from controllers.login_controller import LoginController

class HeaderController(Controller):
    def __init__(self, master):
        super().__init__(master)
        self._view = Header(master)
        self._load_view()
        self.MPMS = MPMS.get_instance()
    
    def _load_view(self) -> None:
        self._view.pack(fill="x")   

    def return_home(self):
        self.MPMS = MPMS.get_instance()
        if self.MPMS.login is not None:
            if self.MPMS.get_login().is_patient():
                self._master.load_controller(PatientHomeController) 
                print("Patient")
            else:
                self._master.load_controller(AdminHomeController) 
                print("Admin")

    def display_logout(self):
        self._view.pack_forget()
        self._view.display_logout_btn()
        self._view.pack()

    def logout(self):
        self._master.load_controller(LoginController)
        #self.MPMS.set_login(None)
        #self._master.header.update()
        
    def login_status(self):
        self.MPMS = MPMS.get_instance()
        return self.MPMS.get_login()