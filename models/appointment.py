from datetime import datetime
# from models.patient import Patient
from models.appointment_reason import AppointmentReason

class Appointment():
    def __init__(self, info):
        self.new_patient = info["new_patient"]
        self.date_time = datetime.strptime(info["date_time"], '%b %d %Y %I:%M%p')
        # self.patient= Patient(info["patient"])
        # self.gp = GP(info["gp"])
        self.appointment_reason = AppointmentReason(info["appointment_reason"])
        # self.questionnaire = Questionnaire(info["questionnaire"])

    def get_appointment_reason(self):
        return self.appointment_reason
    