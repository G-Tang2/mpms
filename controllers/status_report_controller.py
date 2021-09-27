from models.apppointment_list import AppointmentList
import tkinter as tk
from controllers.MPMS import MPMS
from views.status_report_view import StatusReportView
from models.report import Report

class StatusReportController(MPMS):
    def __init__(self,master,view = StatusReportView):
        MPMS.__init__(self,master,view)
        #self.load_appointment_reasons()
        
    def get_report_statistic(self, start_date = None, end_date = None, info=None):
        report = Report("reason")
        return report.get_statistic()

    
    def get_appointments(self):
        appointment_list = []
        for branch in self.get_list_of_branches().get_branch_list():
            branch_appointments = branch.get_appointments()
            appointment_list += branch_appointments.get_appointment_list()
        return appointment_list

    def get_appointment_reasons(self):
        # get appointment reason's reason (may have to rename)
        appointment_reason_list = []
        for appointment in self.get_appointments():
            appointment_reason_list.append(appointment.get_appointment_reason().get_reason())
        return appointment_reason_list

    def load_appointment_reasons(self):
        appointment_reason = self.get_appointment_reasons()
        self.__view.display_appointment_reasons(appointment_reason)