from models.apppointment_list import AppointmentList
import tkinter as tk
from controllers.MPMS import MPMS
from views.status_report_view import StatusReportView
from models.report import Report

from tkinter import Toplevel, ttk
from tkinter.constants import E, NO, W

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StatusReportController(MPMS):
    def __init__(self,master,view = StatusReportView):
        MPMS.__init__(self,master,view)

    def get_reason_report(self, start_date, end_date, report_type):
        if start_date >= end_date:
            self._view.display_input_error("Start date should be earlier than end date")
            return
           
        reason_dict = self.get_report_statistic(start_date,end_date,report_type)

        if len(reason_dict) == 0:
            self._view.display_input_error("No appointments within this period")
            return
        
        self._view.display_reason_report(reason_dict)

    def get_report_statistic(self, start_date, end_date,report_type):
        report = Report(report_type)
        return report.get_statistic(start_date, end_date, report_type)