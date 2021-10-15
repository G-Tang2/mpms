from controllers.controller import Controller
from views.admin_home_view import AdminHomeView
from controllers.status_report_controller import StatusReportController
from models.MPMS import MPMS


class AdminHomeController(Controller):
    def __init__(self,master) -> None:
        super().__init__(master)
        self.MPMS = MPMS.get_instance()
        self._view = AdminHomeView(master, self)
        self._initialise_view()
        self._load_view()

    def _initialise_view(self) -> None:
        login = self.MPMS.get_login()
        user_name = login.get_user_name()
        self._view.render_view(user_name)

    def status_report(self) -> None:
        self._master.load_controller(StatusReportController)
