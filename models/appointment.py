from datetime import datetime
from typing import List
from models.appointment_reason import AppointmentReason
from models.gp import GP
from models.patient import Patient
from models.questionnaire import Questionnaire
from utils.json import JSON
import copy
import json

class Appointment():
    def __init__(self, new_patient: bool, date_time: datetime, patient: Patient, gp: GP,
            appointment_reason: AppointmentReason, questionnaire: Questionnaire) -> None:
        self.new_patient = new_patient
        self.date_time = date_time
        self.patient = patient
        self.gp = gp
        self.appointment_reason = appointment_reason
        self.questionnaire = questionnaire

    def get_appointment_reason(self) -> AppointmentReason:
        return self.appointment_reason

    def get_appointment_datetime(self) -> datetime:
        return self.date_time

    def get_gp(self) -> GP:
        return self.gp

    def serialise_copy(self):
        '''
        Return a serialisable version of this appointment instance
        '''
        # copy of this instance
        tmp = copy.deepcopy(self)
        # convert datetime to string
        tmp.date_time = tmp.date_time.strftime("%Y-%m-%dT%H:%M:%S")
        # serialise patient instance
        tmp.patient = tmp.patient.serialise_copy()
        return tmp
    
    def to_JSON(self) -> json:
        '''
        Returns a json object from this appointment instance
        '''
        tmp = self.serialise_copy()
        return JSON.to_JSON(tmp)

    @staticmethod
    def create_from_json(json_info):
        '''
        Create an Appointment instance based on json input
        '''
        new_patient = json_info["new_patient"]
        date_time = datetime.strptime(json_info["date_time"], "%Y-%m-%dT%H:%M:%S")
        patient= Patient.create_from_json(json_info["patient"])
        gp = GP.create_from_json(json_info["gp"])
        appointment_reason = AppointmentReason.create_from_json(json_info["appointment_reason"])
        questionnaire = Questionnaire.create_from_json(json_info["questionnaire"])
        return Appointment(new_patient, date_time, patient, gp, appointment_reason, questionnaire)
