from controllers.controller import Controller
from models.apppointment_list import AppointmentList
import tkinter as tk
from models.MPMS import MPMS
from views.status_report_view import StatusReportView
from models.report import Report

from tkinter import Toplevel, ttk
from tkinter.constants import E, NO, W

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime

class StatusReportController(Controller):
    def __init__(self,master):
        super().__init__(master)
        self._view = StatusReportView(master, self)
        self._view.render_view()
        self._load_view()

    def get_reason_report(self, start_date, end_date, report_type):
        
        print(start_date)
        # print(type(start_date))
        # try:
        #     test1 = datetime.datetime.strptime(start_date, '%d-%m-%Y')
        #     test2 = datetime.datetime.strptime(end_date, '%d-%m-%Y')
        # except ValueError:
        #     self._view.display_input_error("Incorrect date format input")
        #     return
        
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