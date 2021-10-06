from models.gp_list import GPList
from models.queue import Queue
from models.apppointment_list import AppointmentList
import json

class Branch():
    def __init__(self, name, address, open_hour, close_hour, 
        phone_number, unavailable_days,appointments, gps, queue = Queue()):
            self.name = name
            self.address = address
            self.open_hour = open_hour
            self.close_hour = close_hour
            self.phone_number = phone_number
            self.unavailable_days = unavailable_days
            self.appointments = AppointmentList(json.loads(appointments))
            self.gps = GPList(json.loads(gps))
            self.queue = queue
    
    def get_name(self):
        return self.name

    def get_appointments(self):
        return self.appointments