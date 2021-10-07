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
        
    def get_report_statistic(self, start_date, end_date,report_type,  info=None):
        report = Report("reason")
        return report.get_statistic(start_date, end_date, report_type)

    # def get_appointments(self):
    #     appointment_list = []
    #     for branch in self.get_list_of_branches().get_branch_list():
    #         branch_appointments = branch.get_appointments()
    #         appointment_list += branch_appointments.get_appointment_list()
    #     return appointment_list

    # def get_appointment_reasons(self):
    #     # get appointment reason's reason (may have to rename)
    #     appointment_reason_list = []
    #     for appointment in self.get_appointments():
    #         appointment_reason_list.append(appointment.get_appointment_reason().get_reason())
    #     return appointment_reason_list

    
    def display_reason_report(self, start_date, end_date, report_type):
        
        if start_date >= end_date:
            tk.messagebox.showerror("Error", "Start date should be earlier than end date")
            return None

        reason_dict = self.get_report_statistic(start_date,end_date,report_type)

        if len(reason_dict) == 0:
            tk.messagebox.showerror("Error", "No appointments within this period")
            return

        report = Toplevel(self._view)
        report.title("Reason Report")
        report.geometry("700x700")
        
        tk.Label(report,text = "Reason Pie Chart").pack()
        f = Figure(figsize=(5,4), dpi= 100)
        a = f.add_subplot(111)
        labels = reason_dict.keys()
        sizes = reason_dict.values()
        a.pie(sizes, labels = labels)
        canvas = FigureCanvasTkAgg(f,report)
        canvas.get_tk_widget().pack(fill=tk.BOTH)
    
        # Add reason table
        reason_table = ttk.Treeview(report, height = len(reason_dict))
        reason_table['columns'] = ("Reason","Occurences")

        reason_table.column("#0",width=0,stretch=NO)
        reason_table.column("Reason",anchor=W, width = 120)
        reason_table.column("Occurences",anchor=E, width=120)

        reason_table.heading("#0", text = '', anchor=W)
        reason_table.heading("Reason", text = 'Reason', anchor=W)
        reason_table.heading("Occurences", text = 'Occurence Percentage (%)', anchor=E)
    
        table_iid = 0
        for key,value in reason_dict.items():
            reason_table.insert(parent='',index='end',iid=table_iid,text="",values=(key,round(value,2)))
            table_iid += 1
        reason_table.pack(fill=tk.BOTH)

    def get_reason_report(self, start_date, end_date, report_type):
        
        if start_date >= end_date:
            self._view.display_input_error("Start date should be earlier than end date")
           
        reason_dict = self.get_report_statistic(start_date,end_date,report_type)

        if len(reason_dict) == 0:
            self._view.display_input_error("No appointments within this period")
        
        self._view.display_reason_report(reason_dict)