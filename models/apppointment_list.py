from typing import List
from models.appointment import Appointment
from utils.json import JSON

class AppointmentList():
    def __init__(self, appointments: List[Appointment]) -> None:
        self.appointments = appointments

    def get_appointment_list(self) -> List[Appointment]:
        return self.appointments

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def to_JSON(self):
        lst = []
        for appointment in self.appointments:
            lst.append(appointment.serialise_copy())
        return JSON.to_JSON({"appointments": lst})

    @staticmethod
    def create_from_json(json_info):
        appointment_list = []
        for appointment_json in json_info["appointments"]:
            appointment_list.append(Appointment.create_from_json(appointment_json))
        return AppointmentList(appointment_list)
        
                