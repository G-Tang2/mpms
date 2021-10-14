from typing import List
from models.appointment_reason import AppointmentReason
import csv


class AppointmentReasonList():
    def __init__(self, reasons: List[AppointmentReason]):
        self.reasons = reasons

    def get_reason_list(self):
        return self.reasons

    def get_reason(self, reason):
        for each_reason in self.reasons:
            if reason == each_reason.get_reason():
                return each_reason

    @staticmethod
    def create_from_csv():
        reason_list = []

        with open("./app_data/appointment_resaon.csv", "r", encoding='utf-8-sig') as f:
            f_reader = csv.DictReader(f)
            for reason_info in f_reader:
                reason_list.append(AppointmentReason.create_from_json(reason_info))

        return AppointmentReasonList(reason_list)