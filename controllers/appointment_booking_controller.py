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


class AppointmentBookingController(MPMS):
    def __init__(self, master: tk.Tk) -> None:
        MPMS.__init__(self, master, AppointmentView)

        self.branch = 'None'

        self.__create_data(master)
        self.appointments = AppointmentList([])
        self.list_of_reasons = AppointmentReasonList.create_from_csv()

    def __create_data(self, master: tk.Tk):
        # self.patient = Patient('patient@monash.edu', 'Monash1234', 'Tom', 'T', '012345678', '01/01/1990', 'Male')
        self.patient = master.login.get_user()
        self.gp = GP('Alice', 'Brown', '012345678', [], [])
        self.date = datetime.datetime(2010, 1, 1)
        self.appointment_reason = AppointmentReason('long', 15)
        self.questionnaire = Questionnaire()

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

        self._view = AppointmentDetailView(master, self)

        new_frame = AppointmentDetailView(master, self)

        list_of_gps = []
        for branch in self.list_of_branches.get_branch_list():
            if self.branch == branch.get_name():
                self.appointments = branch.get_appointments()
                list_of_gps = branch.get_gps()
                break

        new_frame.render_view(master, list_of_gps)

        if master.body_frame is not None:
            master.body_frame.destroy()

        master.body_frame = new_frame
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)

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

    def write_appointment(self):
        headers = ['appointments']
        new_appointment = Appointment(True, self.date, self.patient, self.gp,
                                      self.appointment_reason, self.questionnaire)

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
        now = datetime.datetime(year=2021, month=1, day=1, hour=9, minute=0, second=0)
        now = now - minute
        times = []
        # TODO: change it to the while loop
        for i in range(20):
            now = now + minute
            now_str = now.strftime('%H:%M')
            times.append(now_str)

        return times

    def get_reason_list(self):
        reasons = []
        for reason in self.list_of_reasons.get_resaon_list():
            reasons.append(reason.get_reason())
        return reasons