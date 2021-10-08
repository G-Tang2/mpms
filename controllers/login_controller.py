import tkinter as tk
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from controllers.MPMS import MPMS
from views.login_view import LoginView
from models.login import Login

class LoginController(MPMS):
    def __init__(self,master,view = LoginView):
        MPMS.__init__(self,master,view)

    def login(self, email_address: str, password: str):
        try:
            self._master.login = Login(email_address, password)
            if self._master.login.is_patient():
                self._master.load_controller(PatientHomeController)
            else:
                self._master.load_controller(AdminHomeController)
        except ValueError as m:
            self._view.display_email_error(m)
