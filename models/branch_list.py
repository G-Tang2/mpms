from typing import List
from models.branch import Branch
import csv

class BranchList():
    def __init__(self, branches: List[Branch]):
        self.branches = branches

    def get_branch_list(self):
        return self.branches

    @staticmethod
    def create_from_csv():
        branch_list = []

        with open("./app_data/branches.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.DictReader(f)
            for branch_info in f_reader:
                branch_list.append(Branch.create_from_json(branch_info))
        
        return BranchList(branch_list)
                