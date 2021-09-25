
class Appointment():
    def __init__(self, info):
        self.date_time = info["date_time"]
        self.patient= info["patient"]
        self.branch = info["branch"]
        self.gp = info["gp"]
        self.reason = info["reason"]
        self.questionnaire = info["questionnaire"]

    def get_reason(self):
        return self.reason
    