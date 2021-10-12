import datetime
import tkinter as tk
import pandas as pd
from models.MPMS import MPMS
from controllers.controller import Controller
from views.branch_view import BranchView
from views.appointment_detail_view import AppointmentDetailView
from models.appointment import Appointment
from models.apppointment_list import AppointmentList
from datetime import timedelta
from views.questionnaire_view import QuestionnaireView


class AppointmentBookingController(Controller):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.MPMS = MPMS.get_instance()
        self.patient = self.MPMS.get_login().get_user()
        self.branch = 'None'

        # Fetch these data from self.MPMS
        self.branch = 'None'
        self.appointments = AppointmentList([])
        self.list_of_gps = []
        self.__create_data()
        self.gp, self.reason, self.patient_status, self.date, self.time = [None, None, None, None, None]

        self.container_frame = tk.Frame(master,  bg="#c1e4f7")
        self.container_frame.columnconfigure(index=0, weight=1)
        self.container_frame.columnconfigure(index=2, weight=1)
        self._display_branch_view(master)

    def _display_branch_view(self, master):
        self._view = BranchView(self.container_frame, self)
        self._view.render_view(master, self.sort_branches())
        self._view.grid(row=0, column=1, sticky="ns")
        # self._view.grid(row=0, column=0)
        self.views_stack = [self._view]
        self._load_view()

    def _load_view(self) -> None:
        # remove frame if tk instance has a frame
        if self._master.body_frame is not None:
            self._master.body_frame.destroy()
        # assign new frame to tk instance
        self._master.body_frame = self.container_frame
        self._master.body_frame.grid_propagate(False)
        self._master.body_frame.pack(side="top", fill="both", expand=True)  

    def __create_data(self):
        self.gp = 'gp'
        self.reason = 'reason'
        self.patient_status = 'status'
        self.date = 'date'
        self.time = 'time'

    # For AppointmentView: sort branch list based on branch name (alphabetical order)
    def sort_branches(self):
        sorted_branches = []
        for branch in self.MPMS.get_list_of_branches().get_branch_list():
            sorted_branches.append(branch.get_name())

        # sorted_branches = self.selection_sort(sorted_branches)
        sorted_branches.sort()

        return sorted_branches

    # For AppointmentView: display next view
    def display_gp_view(self, master: tk.Tk, branch) -> None:
        self.branch = branch

        view = AppointmentDetailView(self.container_frame, self)
        self.views_stack.append(view)

        self.appointments = self.MPMS.get_branch(branch).get_appointments()
        self.list_of_gps = self.MPMS.get_branch(branch).get_gps()


        view.render_view(self.container_frame, self.list_of_gps)
        # master.body_frame.destroy()
        view.grid(row=0, column=1, sticky="ns")

        view.tkraise()
        self._view = view

    # For AppointmentDetailView: back to the previous view
    def back(self):
        # destroy current frame and load the previous frame
        current_frame = self.views_stack.pop()
        current_frame.destroy()
        previous_view = self.views_stack[-1]
        previous_view.reload_values()
        previous_view.tkraise()
        self._view = previous_view

    # For AppointmentView: display the info of the selected branch
    def show_info(self, branch):
        self._view.show_branch_info(self.MPMS.get_branch(branch))

    # For AppointmentDetailView: if user do not select a GP, this method will find the GP with least appointments
    def find_gp_with_least_appointment(self) -> str:
        appointments = []

        gps = self.MPMS.get_branch(self.branch).get_gps() # GPList
        appointments = self.MPMS.get_branch(self.branch).get_appointments() # AppointmentList

        gp_dict = {}

        for gp in gps.get_gps():
            gp_dict[gp.get_full_name()] = 0

        for appointment in appointments.get_appointment_list():
            gp_dict[appointment.get_gp().get_full_name()] += 1

        sorted_gp = sorted(gp_dict.items(), key=lambda item: item[1])
        gp_name = sorted_gp[0][0]

        return gp_name

    # For AppointmentDetailView: offer day list to the date choosen box
    def get_days(self):
        day = timedelta(days=1)
        today = datetime.date.today()
        days = []
        for i in range(7):
            today = today + day
            today_str = today.strftime('%y-%m-%d')
            days.append(today_str)

        return days

    # For AppointmentDetailView: offer time list to the date choosen box based on the reason
    def get_time(self, reason):
        duration = 1
        for each_reason in self.MPMS.get_list_of_reasons().get_resaon_list():
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

    # For AppointmentDetailView: offer reason list to the reason choosen box
    def get_reason_list(self):
        reasons = []
        for reason in self.MPMS.get_list_of_reasons().get_resaon_list():
            reasons.append(reason.get_reason())
        return reasons

    # For AppointmentDetailView: display the questionnaire view after all the details completed
    def display_questionnaire_view(self, master: tk.Tk, gp, reason, patient_status, date, time) -> None:

        self.gp = gp
        self.reason = reason
        self.patient_status = patient_status
        self.date = date
        self.time = time

        view = QuestionnaireView(self.container_frame, self)
        self.views_stack.append(view)

        view.render_view(self.container_frame, self.MPMS.get_questionnaire().get_question_list(), self.get_data(), self.branch)
        # master.body_frame.destroy()
        view.grid(row=0, column=1, sticky="ns")
        view.tkraise()

    # For this controller : find the GP object based on the GP name
    def find_gp(self, gp):
        for each_gp in self.list_of_gps.get_gps():
            if gp == each_gp.get_full_name():
                return each_gp

    # For this controller : find the AppointmentReason object based on the reason
    def find_reason(self, reason):
        for each_reason in self.MPMS.get_list_of_reasons().get_resaon_list():
            if reason == each_reason.get_reason():
                return each_reason

    def get_data(self):
        return [self.gp, self.reason, self.patient_status, self.date, self.time]

    # For QuestionnaireView: write the appointment info to file after confirmation
    def write_appointment(self):
        branch_id = 0
        for branch in self.MPMS.get_list_of_branches().get_branch_list():
            if self.branch == branch.get_name():
                branch_id = branch.get_id()
                break

        appointment_gp = self.find_gp(self.gp)
        appointment_reason = self.find_reason(self.reason)
        # date = self.date.strftime('%y-%m-%d')
        date = self.date.strftime("%Y-%m-%d")
        # appointment_date = datetime.datetime(year=int(date[0:2])+2000, month=int(date[3:5]), day=int(date[6:8]), hour=int(self.time[0:2]), minute=int(self.time[3:5]))
        appointment_date = datetime.datetime.strptime(date + 'T' + self.time, "%Y-%m-%dT%H:%M")
        new_appointment = Appointment(self.patient_status, appointment_date, self.patient, appointment_gp,
                                      appointment_reason, self.MPMS.get_questionnaire())

        self.appointments.add_appointment(new_appointment)
        dt = pd.read_csv("./app_data/branches.csv")
        # dt_copy['appointments'].loc[int(branch_id) - 1] = self.appointments.to_JSON()

        dt.loc[int(branch_id) - 1, ('appointments')] = self.appointments.to_JSON()
        dt.to_csv("./app_data/test.csv", index=False)