from models.branch_list import BranchList
from models.appointment_reason_list import AppointmentReasonList
from models.questionnaire import Questionnaire
from models.login import Login
from datetime import datetime
import datetime

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

    def calculate_reason_statistic(self, start_date, end_date, report_type, info = None):
        self.statistic = {}

        list_of_branches = self.list_of_branches.get_branch_list()

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

    @staticmethod
    def get_instance():
        if MPMS._instance is None:
            MPMS._instance = MPMS()
        return MPMS._instance
    
