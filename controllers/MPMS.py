from models.branch_list import BranchList
from models.appointment_reason_list import AppointmentReasonList
from models.questionnaire import Questionnaire
from models.login import Login

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

    @staticmethod
    def get_instance():
        if MPMS._instance is None:
            MPMS._instance = MPMS()
        return MPMS._instance
    
