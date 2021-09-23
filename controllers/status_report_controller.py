import tkinter as tk
from controllers.controller import Controller
from views.status_report_view import StatusReportView

class StatusReportController(Controller):
    def __init__(self,master,view = StatusReportView):
        Controller.__init__(self,master,view)

    #def status_report():