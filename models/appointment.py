from datetime import datetime
from models.appointment_reason import AppointmentReason
from models.gp import GP
from models.patient import Patient
from models.questionnaire import Questionnaire
from models.util.json import JSON
import copy

class Appointment():
    def __init__(self, info):
        self.new_patient = info["new_patient"]
        self.date_time = datetime.strptime(info["date_time"], '%b %d %Y %I:%M%p')
        self.patient= Patient(info["patient"])
        self.gp = GP(info["gp"])
        self.appointment_reason = AppointmentReason(info["appointment_reason"])
        self.questionnaire = Questionnaire(info["questionnaire"])

    def get_appointment_reason(self):
        return self.appointment_reason

    def get_appointment_datetime(self):
        return self.date_time

    def serialise(self):
        tmp = copy.deepcopy(self)
        tmp.date_time = tmp.date_time.strftime("%b %d %Y %I:%M%p")
        return tmp
    
    def to_JSON(self):
        tmp = self.serialise()
        return JSON.to_JSON(tmp)
    