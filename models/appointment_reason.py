
class AppointmentReason():
    def __init__(self, info):
        self.reason = info["reason"]
        self.duration = info["duration"]

    def get_reason(self):
        return self.reason

    