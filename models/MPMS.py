from models.branch_list import BranchList
from models.appointment_reason_list import AppointmentReasonList
from models.questionnaire import Questionnaire
from models.login import Login
from datetime import datetime
import datetime
import pandas as pd

class MPMS:
    # global instance
    _instance = None
    
    def __init__(self) -> None:
        self.list_of_branches = BranchList.create_from_csv()
        self.list_of_reasons = AppointmentReasonList.create_from_csv()
        self.questionnaire = Questionnaire.create_from_csv()
        self.login = None

    def get_login(self) -> Login:
        return self.login

    def set_login(self, login: Login) -> bool:
        self.login = login
        return True

    def get_list_of_branches(self):
        return self.list_of_branches

    def get_questionnaire(self):
        return self.questionnaire

    def get_list_of_reasons(self):
        return self.list_of_reasons
    
    def get_branch(self, branch_name):
        for branch in self.get_list_of_branches().get_branch_list():
            if branch_name == branch.get_name():
                return branch

    def calculate_reason_statistic(self, start_date: datetime, end_date: datetime) -> dict:
        statistic = {}

        list_of_branches = self.list_of_branches.get_branch_list()

        total_reasons = 0
        for branch in list_of_branches:
            appointment_list = branch.get_appointments()
            appointment_list = appointment_list.get_appointment_list()
            # Filter between time periods
            for appointment in appointment_list:
                # Filter between time periods
                appointment_date = appointment.get_appointment_datetime()
                if start_date.date() <=  appointment_date.date() <= end_date.date():
                    total_reasons += 1
                    appointment_reason_object = appointment.get_appointment_reason()
                    appointment_reason = appointment_reason_object.get_reason()
                    if appointment_reason not in statistic:
                        statistic[appointment_reason] = 1
                    else:
                        statistic[appointment_reason] += 1

        for key,value in statistic.items():
            statistic[key] = (value/total_reasons) * 100
        return statistic

    @staticmethod
    def write_appointment(branch_id, appointment_list):
        # read file from file
        dt = pd.read_csv("./app_data/branches.csv")
        # change the appointment list value and write to the file
        dt.loc[int(branch_id) - 1, ('appointments')] = appointment_list.to_JSON()
        dt.to_csv("./app_data/branches.csv", index=False)


    @staticmethod
    def get_instance():
        if MPMS._instance is None:
            MPMS._instance = MPMS()
        return MPMS._instance
    
