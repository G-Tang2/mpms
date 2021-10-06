from models.gp_list import GPList
from models.queue import Queue
from models.apppointment_list import AppointmentList
import json

class Branch():
    def __init__(self, info):
            self.name = info["name"]
            self.address = info["address"]
            self.open_hour = info["open_hour"]
            self.close_hour = info["close_hour"]
            self.phone_number = info["phone_number"]
            self.unavailable_days = info["unavailable_days"]
            self.appointments = AppointmentList(json.loads(info["appointments"]))
            self.queue = Queue()
            self.gps = GPList(json.loads(info["gps"]))
    
    def get_name(self):
        return self.name

    def get_appointments(self):
        return self.appointments

    def get_gps(self):
        return self.gps
