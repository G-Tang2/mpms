
class AppointmentReason():
    def __init__(self, reason: str, duration: int) -> None:
        self.reason = reason
        self.duration = duration

    def get_reason(self):
        return self.reason

    def get_duration(self):
        return self.duration
    
    @staticmethod
    def create_from_json(json_info):
        reason = json_info["reason"]
        duration = json_info["duration"]
        return AppointmentReason(reason, duration)
    

    