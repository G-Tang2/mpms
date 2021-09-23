import tkinter as tk
from controllers.controller import Controller
from views.admin_home_view import AdminHomeView
from controllers.status_report_controller import StatusReportController


class AdminHomeController(Controller):
    def __init__(self,master,view = AdminHomeView):
        Controller.__init__(self,master,view)

    def status_report(self):
        self._master.load_controller(StatusReportController)
