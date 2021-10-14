from controllers.controller import Controller
from controllers.patient_home_controller import PatientHomeController
from controllers.admin_home_controller import AdminHomeController
from models.MPMS import MPMS
from views.header_view import HeaderView
from controllers.login_controller import LoginController

class HeaderController(Controller):
    def __init__(self, master):
        super().__init__(master)
        self._view = HeaderView(master)
        self._load_view()
        self.MPMS = MPMS.get_instance()
    
    def _load_view(self) -> None:
        '''
        Overrides the Controller class _load_view function to load own view
        '''
        self._view.pack(fill="x")   

    def return_home(self):
        '''
        Return to home page function
        '''
        # Determines if user is not in login or home page
        if type(self._master.main_controller) not in (AdminHomeController,PatientHomeController,LoginController):
            # Function requesting for confirmation to leave to home page
            if self._view.return_confirmation():
                # Determines account status and loads corresponding controller
                if self.MPMS.login is not None:
                    if self.MPMS.get_login().is_patient():
                        self._master.load_controller(PatientHomeController) 
                    else:
                        self._master.load_controller(AdminHomeController)

    def display_logout(self):
        '''
        Display logout button
        '''
        self._view.display_logout_btn()
        
    def logout(self):
        '''
        Logout from account function
        '''
        # Determines if user not in login page
        if type(self._master.main_controller) is not LoginController:
            # Request confirmation for logout if user is using a functional page
            if type(self._master.main_controller) not in (AdminHomeController,PatientHomeController):
                if not self._view.return_confirmation():
                    return
            # Returns to login page with login controller
            self._master.load_controller(LoginController)
            self.MPMS.set_login(None)
            # Call view function to hide logout button
            self._view.hide_logout_btn()

    def return_home_patient(self):
        self._master.load_controller(PatientHomeController)
