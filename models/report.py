
from models.branch_list import BranchList
from models.apppointment_list import AppointmentList
from datetime import datetime

class Report():
    def __init__(self, type):
        self.type = type
        self.statistic = {}
        #self.list_of_appointments = self.__fetch_appointment_list()

    def calculate_statistic(self, start_date= None, end_date=None, info = None):
        self.statistic = {}

        branch_list = BranchList()
        self.list_of_branches = branch_list.get_branch_list()

        start_date = datetime.strptime('2005-2-1', '%Y-%m-%d')
        end_date = datetime.strptime('2015-2-1', '%Y-%m-%d')
        
        for branch in self.list_of_branches:
            appointment_list = branch.get_appointments()
            appointment_list = appointment_list.get_appointment_list()
            # Filter between time periods
            for appointment in appointment_list:
                # Filter between time periods
                appointment_date = appointment.get_appointment_datetime()
                if start_date <  appointment_date < end_date:
                    appointment_reason_object = appointment.get_appointment_reason()
                    appointment_reason = appointment_reason_object.get_reason()
                    if appointment_reason not in self.statistic:
                        self.statistic[appointment_reason] = 1
                    else:
                        self.statistic[appointment_reason] += 1
        
        print(self.statistic)
 
    def get_statistic(self):
        self.calculate_statistic()
        return self.statistic
    
    #def __fetch_appointment_list(self):
     #   return AppointmentList()
        