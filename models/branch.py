from models.queue import Queue

class Branch():
    def __init__(self, info):
            self.name = info["name"]
            self.address = info["address"]
            self.open_hour = info["open_hour"]
            self.close_hour = info["close_hour"]
            self.phone_number = info["phone_number"]
            self.unavailable_days = info["unavailable_days"]
            self.appointments = info["appointments"]
            self.queue = Queue()
    
    def get_name(self):
        return self.name