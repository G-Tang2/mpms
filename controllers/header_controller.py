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
        if type(self._master.main_controller) not in (AdminHomeController,PatientHomeController,LoginController):
            tk.messagebox.askquestion(title='Confirmation', message='Return to Home Page and Discard Changes?')
            if self.MPMS.login is not None:
                if self.MPMS.get_login().is_patient():
                    self._master.load_controller(PatientHomeController) 
                else:
                    self._master.load_controller(AdminHomeController)

    def display_logout(self):
        self._view.pack_forget()
        self._view.display_logout_btn()
        self._view.pack()

    def logout(self):
        if type(self._master.main_controller) not in (AdminHomeController,PatientHomeController,LoginController):
            confirmation = tk.messagebox.askquestion(title='Confirmation', message='Return to Login Page and Discard Changes?')
            if not confirmation:
                return
        self._master.load_controller(LoginController)
        self.MPMS.set_login(None)
        self._view.hide_logout_btn()
        
    def login_status(self):
        self.MPMS = MPMS.get_instance()
        return self.MPMS.get_login()