from datetime import datetime
from typing import List
from models.gp_list import GPList
from models.queue import Queue
from models.apppointment_list import AppointmentList
import json

class Branch():
    def __init__(self, name: str, address: str, open_hour: str, close_hour: str, 
            phone_number: str, unavailable_days: List[datetime], 
            appointments: AppointmentList, gps: GPList, queue = Queue()):
        self.name = name
        self.address = address
        self.open_hour = open_hour
        self.close_hour = close_hour
        self.phone_number = phone_number
        self.unavailable_days = unavailable_days
        self.appointments = appointments
        self.gps = gps
        self.queue = queue
    
    def get_name(self) -> str:
        return self.name

    def get_appointments(self) -> AppointmentList:
        return self.appointments

    @staticmethod
    def create_from_json(json_info):
        name = json_info["name"]
        address = json_info["address"]
        open_hour = json_info["open_hour"]
        close_hour = json_info["close_hour"]
        phone_number = json_info["phone_number"]
        unavailable_days = json_info["unavailable_days"]
        appointments = AppointmentList.create_from_json(json.loads(json_info["appointments"]))
        gps = GPList.create_from_json(json.loads(json_info["gps"]))

        return Branch(name, address, open_hour, close_hour, 
            phone_number, unavailable_days,appointments, gps)