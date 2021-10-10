from controllers.controller import Controller
from views.admin_home_view import AdminHomeView
from controllers.status_report_controller import StatusReportController


class AdminHomeController(Controller):
    def __init__(self,master):
        super().__init__(master)
        self._view = AdminHomeView(master, self)
        self._view.render_view()
        self._load_view()

    def status_report(self):
        self._master.load_controller(StatusReportController)
