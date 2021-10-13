from controllers.controller import Controller
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from models.MPMS import MPMS
from views.header_view import Header
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
            if self._view.return_confirmation():
                if self.MPMS.login is not None:
                    if self.MPMS.get_login().is_patient():
                        self._master.load_controller(PatientHomeController) 
                    else:
                        self._master.load_controller(AdminHomeController)

    def display_logout(self):
        self._view.display_logout_btn()
        
    def logout(self):
        if type(self._master.main_controller) is not LoginController:
            if type(self._master.main_controller) not in (AdminHomeController,PatientHomeController):
                if not self._view.return_confirmation():
                    return
            self._master.load_controller(LoginController)
            self.MPMS.set_login(None)
            self._view.hide_logout_btn()
