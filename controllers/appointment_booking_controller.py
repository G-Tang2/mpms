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
        # get a MPMS instance
        self.MPMS = MPMS.get_instance()
        # get user from the login
        self.patient = self.MPMS.get_login().get_user()

        # create initial data
        self.branch = 'None'
        self.appointments = AppointmentList([])
        self.list_of_gps = []
        self.gp, self.reason, self.patient_status, self.date, self.time = [None, None, None, None, None]

        # create contain frame
        self.container_frame = tk.Frame(master,  bg="#c1e4f7")
        self.container_frame.columnconfigure(index=0, weight=1)
        self.container_frame.columnconfigure(index=2, weight=1)
        self.display_branch_view(master)

        ##################  Branch View  #######################
    def display_branch_view(self, master):
        '''
        display branch view
        '''

        self._view = BranchView(self.container_frame, self)
        self._view.render_view(master, self.sort_branches())
        self._view.grid(row=0, column=1, sticky="ns")
        # self._view.grid(row=0, column=0)
        self.views_stack = [self._view]
        self._load_view()

    def _load_view(self) -> None:
        '''
        load body frame as container frame
        '''
        # remove frame if tk instance has a frame
        if self._master.body_frame is not None:
            self._master.body_frame.destroy()
        # assign new frame to tk instance
        self._master.body_frame = self.container_frame
        self._master.body_frame.grid_propagate(False)
        self._master.body_frame.pack(side="top", fill="both", expand=True)

    def sort_branches(self):
        '''
        sort branches by alphabetical order
        '''
        sorted_branches = []

        # get branch list from MPMS instance
        for branch in self.MPMS.get_list_of_branches().get_branch_list():
            sorted_branches.append(branch.get_name())

        # sort branches
        sorted_branches.sort()  # List of str

        return sorted_branches

    def display_detail_view(self, master: tk.Tk, branch) -> None:
        '''
        dispaly the GP view
        '''

        # save the branch
        self.branch = branch

        # create new view
        view = AppointmentDetailView(self.container_frame, self)
        self.views_stack.append(view)

        # get data from the MPMS instance
        self.appointments = self.MPMS.get_branch(branch).get_appointments()  # AppointmentList
        self.list_of_gps = self.MPMS.get_branch(branch).get_gps()  # GPList

        # display the detail view
        view.render_view(self.container_frame, self.list_of_gps, self.get_reason_list())
        view.grid(row=0, column=1, sticky="ns")

        # put the view on the top of previous one
        view.tkraise()
        self._view = view

    def show_info(self, branch):
        '''
        show information of branch
        '''
        self._view.show_branch_info(self.MPMS.get_branch(branch))

    ###################  Appointment Detail View  ##################
    def back(self):
        '''
        back to the previous view
        '''

        # destroy current frame and load the previous frame
        current_frame = self.views_stack.pop()
        current_frame.destroy()
        previous_view = self.views_stack[-1]
        previous_view.reload_values()
        previous_view.tkraise()
        self._view = previous_view

    def find_gp_with_least_appointment(self) -> str:
        '''
        if user do not select a GP, this method will find the GP with least appointments
        '''

        # get data from MPMS
        gps = self.MPMS.get_branch(self.branch).get_gps() # GPList
        appointments = self.MPMS.get_branch(self.branch).get_appointments() # AppointmentList

        # initialize a dict
        gp_dict = {}

        # insert values to the dict
        for gp in gps.get_gps():
            gp_dict[gp.get_full_name()] = 0

        for appointment in appointments.get_appointment_list():
            gp_dict[appointment.get_gp().get_full_name()] += 1

        # sorted the dict and get the first key
        sorted_gp = sorted(gp_dict.items(), key=lambda item: item[1])
        gp_name = sorted_gp[0][0]  # str

        return gp_name

    def get_time(self, reason):
        '''
        offer time list to the time box based on the reason
        '''

        duration = 1
        # get duration from reason obj
        for each_reason in self.MPMS.get_list_of_reasons().get_resaon_list():
            if each_reason.get_reason() == reason:
                duration = each_reason.get_duration()

        # create open_hour and close_hour
        minute = timedelta(minutes=int(duration))  # timedelta
        open_hour = datetime.datetime(year=2021, month=1, day=1, hour=9, minute=0, second=0)  # datetime
        close_hour = datetime.datetime(year=2021, month=1, day=1, hour=17, minute=0, second=0)  # datetime
        open_hour = open_hour - minute
        times = []

        # create time list
        while open_hour < close_hour - minute:
            open_hour = open_hour + minute
            now_str = open_hour.strftime('%H:%M')
            times.append(now_str)

        self._view.set_time_list(times)

    def get_reason_list(self):
        '''
        offer reason list to appointment detail view
        '''
        reasons = []

        # get reason list from MPMS
        for reason in self.MPMS.get_list_of_reasons().get_resaon_list():
            reasons.append(reason.get_reason())
        return reasons


    def display_questionnaire_view(self, master: tk.Tk, gp, reason, patient_status, date, time) -> None:
        '''
        display the questionnaire view
        '''

        # store the details from the detail view
        self.gp = gp   # str
        self.reason = reason    # str
        self.patient_status = patient_status   # str
        self.date = date   # str
        self.time = time   # str

        # create questionnaire view
        view = QuestionnaireView(self.container_frame, self)
        self.views_stack.append(view)

        # display the questionnaire view
        view.render_view(self.container_frame, self.MPMS.get_questionnaire().get_question_list(), self.get_data(), self.branch)
        view.grid(row=0, column=1, sticky="ns")
        # put the new view on the top of the previous one
        view.tkraise()

    def get_data(self):
        '''
        return the data for the appointment to a list
        '''
        return [self.gp, self.reason, self.patient_status, self.date, self.time]

    ##########################  Questionnaire  #######################
    def write_appointment(self):
        '''
        write new appointment to the file
        '''

        branch_id = 0
        # get the branch id
        for branch in self.MPMS.get_list_of_branches().get_branch_list():
            if self.branch == branch.get_name():
                branch_id = branch.get_id()
                break

        # get the obj based on the str
        appointment_gp = self.find_gp(self.gp)   # GP
        appointment_reason = self.find_reason(self.reason)   # AppointmentReason
        appointment_date = datetime.datetime.strptime(self.date + 'T' + self.time, "%d/%m/%YT%H:%M")    # datetime

        # create a new appointment with the data
        new_appointment = Appointment(bool(self.patient_status), appointment_date, self.patient, appointment_gp,
                                      appointment_reason, self.MPMS.get_questionnaire())  # Appointment

        # add new appointment to the list
        self.appointments.add_appointment(new_appointment)

        # read file from file
        dt = pd.read_csv("./app_data/branches.csv")
        # change the appointment list value and write to the file
        dt.loc[int(branch_id) - 1, ('appointments')] = self.appointments.to_JSON()
        dt.to_csv("./app_data/test.csv", index=False)

    ######################  Controller  #########################
    def find_gp(self, gp):
        '''
        get the gp obj based on the gp_full name
        '''

        for each_gp in self.list_of_gps.get_gps():
            if gp == each_gp.get_full_name():
                return each_gp

    def find_reason(self, reason):
        '''
        get the reason obj based on the reason str
        '''
        for each_reason in self.MPMS.get_list_of_reasons().get_resaon_list():
            if reason == each_reason.get_reason():
                return each_reason