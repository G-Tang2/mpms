import tkinter as tk
from controllers.controller import Controller
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from models.MPMS import MPMS
from views.login_view import LoginView
from models.login import Login
from controllers.login_controller import LoginController

class HeaderController(Controller):
    def __init__(self, master):
        super().__init__(master)
        self.MPMS = MPMS.get_instance()
    
    def return_home(self):
        self.MPMS = MPMS.get_instance()
        if self.MPMS.login is not None:
            if self.MPMS.get_login().is_patient():
                self._master.load_controller(PatientHomeController) 
                print("Patient")
            else:
                self._master.load_controller(AdminHomeController) 
                print("Admin")

    def logout(self):
        self._master.load_controller(LoginController)
        #self.MPMS.set_login(None)
        #self._master.header.update()
        
    def login_status(self):
        self.MPMS = MPMS.get_instance()
        return self.MPMS.get_login()