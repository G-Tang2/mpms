import json
from models.appointment import Appointment
from models.util.json import JSON

class AppointmentList():
    def __init__(self, json):
        self.appointments = self.__get_appointments(json)
        self.x = self.to_JSON()
        self.y = 4
    
    def __get_appointments(self, json):
        appointment_list = []
        for appointment in json["appointments"]:
            appointment_list.append(Appointment(appointment))
        return appointment_list

    def get_appointment_list(self):
        return self.appointments

    def to_JSON(self):
        lst = []
        for appointment in self.appointments:
            lst.append(appointment.serialise())
        return JSON.to_JSON(lst)
        
                