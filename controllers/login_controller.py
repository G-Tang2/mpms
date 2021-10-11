import tkinter as tk
from controllers.controller import Controller
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from models.MPMS import MPMS
from views.login_view import LoginView
from models.login import Login


class LoginController(Controller):
    def __init__(self, master):
        super().__init__(master)
        self._view = LoginView(master, self)
        self._view.render_view()
        self._load_view()
        self.MPMS = MPMS.get_instance()

    def login(self, email_address: str, password: str):
        try:
            self.MPMS.set_login(Login(email_address, password))
            self._master.header_controller.display_logout()
            if self.MPMS.get_login().is_patient():
                self._master.load_controller(PatientHomeController)
                #self._master.header.refresh()
                self._master.login = True
                # self._master.header.update()
                
            else:
                self._master.load_controller(AdminHomeController)
                #self._master.header.refresh()
                self._master.login = True
                self._master.header.update()
                
        except ValueError as m:
            self._view.display_email_error(m)

