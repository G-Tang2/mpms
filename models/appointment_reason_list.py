from typing import List
from models.appointment_reason import AppointmentReason
import csv


class AppointmentReasonList():
    def __init__(self, appointment_reasons: List[AppointmentReason]) -> None:
        self.appointment_reasons = appointment_reasons

    def get_reason_list(self) -> List[AppointmentReason]:
        return self.appointment_reasons

    def get_reason(self, reason: str) -> AppointmentReason:
        '''
        Find AppointmentReason with the given reason
        '''
        for appointment_reason in self.appointment_reasons:
            if reason == appointment_reason.get_reason():
                return appointment_reason

    @staticmethod
    def create_from_csv():
        '''
        Create an AppointmentReasonList instance based on a json input
        '''
        reason_list = []

        with open("./app_data/appointment_resaon.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.DictReader(f)
            for reason_info in f_reader:
                reason_list.append(AppointmentReason.create_from_json(reason_info))

        return AppointmentReasonList(reason_list)