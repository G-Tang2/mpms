import tkinter as tk
from controllers.MPMS import MPMS
from views.status_report_view import StatusReportView
from models.report import Report

class StatusReportController(MPMS):
    def __init__(self,master,view = StatusReportView):
        MPMS.__init__(self,master,view)

    #def status_report():

    def get_statistic(self, start_date, end_date, info=None):
        report = Report("reason", start_date, end_date)
        return report.get_statistic()