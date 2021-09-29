import tkinter as tk
from controllers.MPMS import MPMS
from views.admin_home_view import AdminHomeView
from controllers.status_report_controller import StatusReportController


class AdminHomeController(MPMS):
    def __init__(self,master,view = AdminHomeView):
        MPMS.__init__(self,master,view)

    def status_report(self):
        self._master.load_controller(StatusReportController)
