import tkinter as tk
from controllers.MPMS import MPMS
from views.status_report_view import StatusReportView

class StatusReportController(MPMS):
    def __init__(self,master,view = StatusReportView):
        MPMS.__init__(self,master,view)

    #def status_report():