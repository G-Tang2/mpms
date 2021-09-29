from models.branch import Branch
import csv

class BranchList():
    def __init__(self):
        self.branches = self.__get_branches()
    
    def __get_branches(self):
        branch_list = []

        with open("./app_data/branches.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.reader(f)
            header = next(f_reader, None)

            # find index of email address and password in header
            name_index = header.index("name")
            address_index = header.index("address")
            open_hour_index = header.index("open_hour")
            close_hour_index = header.index("close_hour")
            phone_number_index = header.index("phone_number")
            unavailable_days_index = header.index("unavailable_days")
            appointments_index = header.index("appointments")

            for branch_details in f_reader:
                # extract branch 
                branch_info = {}
                branch_info["name"] = branch_details[name_index]
                branch_info["address"] = branch_details[address_index]
                branch_info["open_hour"] = branch_details[open_hour_index]
                branch_info["close_hour"] = branch_details[close_hour_index]
                branch_info["phone_number"] = branch_details[phone_number_index]
                branch_info["unavailable_days"] = branch_details[unavailable_days_index]
                branch_info["appointments"] = branch_details[appointments_index]

                branch_list.append(Branch(branch_info))
        return branch_list

    def get_branch_list(self):
        return self.branches

                