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
from datetime import datetime
import datetime

class StatusReportController(Controller):
    def __init__(self,master):
        super().__init__(master)
        self._view = StatusReportView(master, self)
        self._view.render_view()
        self._load_view()

    def get_reason_report(self, start_date, end_date, report_type):
        
        print(start_date)
        print(type(start_date))
        try:
            start_date_check = datetime.datetime.strptime(start_date, '%d/%m/%Y')
            end_date_check = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        except ValueError:
            self._view.display_input_error("Incorrect date format input (Use DD/MM/YYYY)")
            return
        
        if start_date >= end_date:
            self._view.display_input_error("Start date should be earlier than end date")
            return
           
        reason_dict = self.return_statistic(start_date,end_date,report_type)

        if len(reason_dict) == 0:
            self._view.display_input_error("No appointments within this period")
            return
        
        self._view.display_reason_report(reason_dict)

    # Move to MPMS
    def return_statistic(self, start_date, end_date, report_type, info = None):
        self.statistic = {}

        mpms_instance = MPMS.get_instance()
        branch_list= mpms_instance.get_list_of_branches()
        list_of_branches = branch_list.get_branch_list()

        if report_type.lower() == "reason":
            
            start_date = datetime.datetime.strptime(str(start_date), '%d/%m/%Y')
            end_date = datetime.datetime.strptime(str(end_date), '%d/%m/%Y')

            total_reasons = 0
            for branch in list_of_branches:
                appointment_list = branch.get_appointments()
                appointment_list = appointment_list.get_appointment_list()
                # Filter between time periods
                for appointment in appointment_list:
                    # Filter between time periods
                    appointment_date = appointment.get_appointment_datetime()
                    if start_date <  appointment_date < end_date:
                        total_reasons += 1
                        appointment_reason_object = appointment.get_appointment_reason()
                        appointment_reason = appointment_reason_object.get_reason()
                        if appointment_reason not in self.statistic:
                            self.statistic[appointment_reason] = 1
                        else:
                            self.statistic[appointment_reason] += 1
            for key,value in self.statistic.items():
                self.statistic[key] = (value/total_reasons) * 100
            return self.statistic