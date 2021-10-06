from models.branch import Branch
import csv

class BranchList():
    def __init__(self):
        self.branches = self.__get_branches()
    
    def __get_branches(self):
        branch_list = []

        with open("./app_data/branches.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.DictReader(f)
            for branch_info in f_reader:
                branch_list.append(Branch(branch_info["name"], branch_info["address"],
                    branch_info["open_hour"], branch_info["close_hour"], branch_info["phone_number"],
                    branch_info["unavailable_days"], branch_info["appointments"], branch_info["gps"]))

        return branch_list

    def get_branch_list(self):
        return self.branches

                