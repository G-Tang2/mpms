import tkinter as tk
from controllers.controller import Controller
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from models.MPMS import MPMS
from views.login_view import LoginView
from models.login import Login


class LoginController(Controller):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self._view = LoginView(master, self)
        self._view.render_view()
        self._load_view()
        self.MPMS = MPMS.get_instance()

    def login(self, email_address: str, password: str) -> None:
        '''
        Login function loads controller depending on user type
        '''
        try:
            self.MPMS.set_login(Login(email_address, password))
            # Displays logout button when user logs in
            self._master.header_controller.display_logout()
            # Checks user status and loads controllers depending on admin or patient
            if self.MPMS.get_login().is_patient():
                self._master.load_controller(PatientHomeController)
            else:
                self._master.load_controller(AdminHomeController)    
        except ValueError as m:
            self._view.display_email_error(m)

