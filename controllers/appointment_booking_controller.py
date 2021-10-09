import copy
import datetime
import tkinter as tk
from controllers.MPMS import MPMS
from views.appointment_view import AppointmentView
from views.appointment_detail_view import AppointmentDetailView
from models.branch_list import BranchList
from models.appointment import Appointment
from models.questionnaire import Questionnaire
from models.appointment_reason import AppointmentReason
from models.appointment_reason_list import AppointmentReasonList
from models.apppointment_list import AppointmentList
from models.gp import GP
import csv
from datetime import timedelta
from views.questionnaire_view import QuestionnaireView


class AppointmentBookingController(MPMS):
    def __init__(self, master: tk.Tk) -> None:
        self.container_frame = tk.Frame(master)
        self.branch = 'None'
        self.view = AppointmentView(self.container_frame, self)
        self.views_stack = [self.view]
        self.__create_data(master)
        self.appointments = AppointmentList([])
        self.list_of_reasons = AppointmentReasonList.create_from_csv()
        self._master = master
        self.list_of_branches = BranchList.create_from_csv()
        self.__load_view(master)
        self.list_of_gps = []
        self.questionnaire = Questionnaire.create_from_csv()
        self.patient = master.login.get_user()
        # list_of_appointments = self.__fetch_appointment_list()

    def __load_view(self, master: tk.Tk) -> None:
        # remove frame if tk instance has a frame
        if master.body_frame is not None:
            master.body_frame.destroy()
        # assign new frame to tk instance
        self.view.grid(row=0, column=0)
        master.body_frame = self.container_frame
        master.body_frame.pack()

    def __create_data(self, master: tk.Tk):
        # self.patient = Patient('patient@monash.edu', 'Monash1234', 'Tom', 'T', '012345678', '01/01/1990', 'Male')
        self.appointment_reason = AppointmentReason('long', 15)

    def sort_branches(self):
        # new: sort branch list based on branch name (alphabetical order)
        self.list_of_branches = BranchList.create_from_csv()

        sorted_branches = []
        for branch in self.list_of_branches.get_branch_list():
            sorted_branches.append(branch.get_name())

        # sorted_branches = self.selection_sort(sorted_branches)
        sorted_branches.sort()

        return sorted_branches

    def display_gp_view(self, master: tk.Tk, branch) -> None:
        self.branch = branch

        view = AppointmentDetailView(self.container_frame, self)
        self.views_stack.append(view)

        for branch in self.list_of_branches.get_branch_list():
            if self.branch == branch.get_name():
                self.appointments = branch.get_appointments()
                self.list_of_gps = branch.get_gps()
                break

        view.render_view(self.container_frame, self.list_of_gps)
        # master.body_frame.destroy()
        view.grid(row=0, column=0)
        view.tkraise()

    def back(self):
        current_frame = self.views_stack.pop()
        current_frame.destroy()
        previous_view = self.views_stack[-1]
        previous_view.tkraise()

    def get_branch(self):
        return self.branch

    def show_info(self, branch):
        for each_branch in self.list_of_branches.get_branch_list():
            if branch == each_branch.get_name():
                self._view.show_branch_info(each_branch)

    def find_gp_with_least_appointment(self):
        appointments = []
        gps = []
        for each_branch in self.list_of_branches.get_branch_list():
            if self.branch == each_branch.get_name():
                gps = each_branch.get_gps()
                appointments = each_branch.get_appointments()

        gp_dict = {}

        for gp in gps.get_gps():
            gp_dict[gp.get_full_name()] = 0

        for appointment in appointments.get_appointment_list():
            gp_dict[appointment.get_gp().get_full_name()] += 1

        sorted_gp = [v for v in sorted(gp_dict.values())]

        for key in gp_dict.keys():
            if sorted_gp[0] == gp_dict[key]:
                return key

    def write_appointment(self, patient_status, gp, date, time, reason):
        headers = ['appointments']
        appointment_gp = self.find_gp(gp)
        appointment_reason = self.find_reason(reason)
        appointment_date = datetime.datetime(year=int(date[0:2]), month=int(date[3:5]), day=int(date[6:8]),
                                             hour=int(time[0:2]), minute=int(time[3:5]))
        new_appointment = Appointment(patient_status, appointment_date, self.patient, appointment_gp,
                                      appointment_reason, self.questionnaire)

        self.appointments.add_appointment(new_appointment)
        with open("./app_data/appointments.csv", "w") as f:
            f_csv_w = csv.writer(f)
            f_csv_w.writerow(headers)
            f_csv_w.writerow([self.appointments.to_JSON()])

    def get_days(self):
        day = timedelta(days=1)
        today = datetime.date.today()
        days = []
        for i in range(7):
            today = today + day
            today_str = today.strftime('%y-%m-%d')
            days.append(today_str)

        return days

    def get_time(self, reason):
        duration = 1
        for each_reason in self.list_of_reasons.get_resaon_list():
            if each_reason.get_reason() == reason:
                duration = each_reason.get_duration()

        minute = timedelta(minutes=int(duration))
        open_hour = datetime.datetime(year=2021, month=1, day=1, hour=9, minute=0, second=0)
        close_hour = datetime.datetime(year=2021, month=1, day=1, hour=17, minute=0, second=0)
        open_hour = open_hour - minute
        times = []

        while open_hour < close_hour - minute:
            open_hour = open_hour + minute
            now_str = open_hour.strftime('%H:%M')
            times.append(now_str)

        return times

    def get_reason_list(self):
        reasons = []
        for reason in self.list_of_reasons.get_resaon_list():
            reasons.append(reason.get_reason())
        return reasons

    def display_questionnaire_view(self, master: tk.Tk, gp, reason, patient_status, date, time) -> None:

        view = QuestionnaireView(self.container_frame, self)
        self.views_stack.append(view)

        view.render_view(self.container_frame, gp, reason, patient_status, self.questionnaire, date, time)
        # master.body_frame.destroy()
        view.grid(row=0, column=0)
        view.tkraise()

    def find_gp(self, gp):
        for each_gp in self.list_of_gps.get_gps():
            if gp == each_gp.get_full_name():
                return each_gp

    def find_reason(self, reason):
        for each_reason in self.list_of_reasons.get_resaon_list():
            if reason == each_reason.get_reason():
                return each_reason