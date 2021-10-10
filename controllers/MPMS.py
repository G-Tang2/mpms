from models.branch_list import BranchList

class MPMS():
    def __init__(self) -> None:
        self.list_of_branches = BranchList.create_from_csv()
        instance = None

    def get_list_of_branches(self):
        return self.list_of_branches

    @staticmethod
    def get_instance():
        if MPMS.instance is None:
            MPMS.instance = MPMS()
        return MPMS.instance
    
