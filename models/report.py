
from models.apppointment_list import AppointmentList

class Report():
    def __init__(self, type):
        self.type = type
        self.statistic = {}
        self.list_of_appointments = self.__fetch_appointment_list()

    def calculate_statistic(self, start_date, end_date, info = None):
    #count
        list_of_reasons = ["General Check-up","Reason2","Reason3"]
        reason_list = [] 
        # Append all reasons used in appointment to list
        for appointment in self.list_of_appointments:
            reason_list.append(appointment.get_reason())
        #numpy

        total = len(reason_list)

        # Count occurence of each reason
        for reason in list_of_reasons:
            reason_count = reason_list.count(reason)
            reason_percent = reason_count/total
            self.statistic[reason] = reason_percent
 
    def get_statistic(self):
        return self.statistic
    
    def __fetch_appointment_list(self):
        return AppointmentList()
        