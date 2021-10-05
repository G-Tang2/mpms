from models.appointment import Appointment
import csv

class AppointmentList():
    def __init__(self, json):
        self.appointments = self.__get_appointments(json)
    
    def __get_appointments(self, json):
        appointment_list = []
        for appointment in json["appointments"]:
            appointment_list.append(Appointment(appointment))
        return appointment_list

    def get_appointment_list(self):
        return self.appointments

                