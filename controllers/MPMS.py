from models.branch_list import BranchList
from models.login import Login

class MPMS():
    # global instance
    _instance = None
    
    def __init__(self) -> None:
        self.list_of_branches = BranchList.create_from_csv()
        self.login = None

    def get_login(self) -> Login:
        return self.login

    def set_login(self, login: Login) -> bool:
        self.login = login
        return True

    def get_list_of_branches(self):
        return self.list_of_branches

    @staticmethod
    def get_instance():
        if MPMS._instance is None:
            MPMS._instance = MPMS()
        return MPMS._instance
    
