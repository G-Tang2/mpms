from models.appointment import Appointment
import csv

class AppointmentList():
    def __init__(self):
        self.appointments = self.__get_appointments()
    
    def __get_appointments(self):
        appointment_list = []

        with open("./app_data/appointments.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.reader(f)
            header = next(f_reader, None)

            # find index of email address and password in header
            date_time_index = header.index("date_time")
            patient_index = header.index("patient")
            branch_index = header.index("branch")
            gp_index = header.index("gp")
            reason_index = header.index("reason")
            questionnaire_index = header.index("questionnaire")

            for branch_details in f_reader:
                # extract branch 
                appointment_info = {}
                appointment_info["date_time"] = branch_details[date_time_index]
                appointment_info["patient"] = branch_details[patient_index]
                appointment_info["branch"] = branch_details[branch_index]
                appointment_info["gp"] = branch_details[gp_index]
                appointment_info["reason"] = branch_details[reason_index]
                appointment_info["questionnaire"] = branch_details[questionnaire_index]
                appointment_list.append(Appointment(appointment_info))
        return appointment_list

    def get_appointment_list(self):
        return self.appointments

                