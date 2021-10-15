
class AppointmentReason():
    def __init__(self, reason: str, duration: int) -> None:
        self.reason = reason
        self.duration = duration  # duration in minutes

    def get_reason(self)-> str:
        return self.reason

    def get_duration(self) -> int:
        return self.duration
    
    @staticmethod
    def create_from_json(json_info):
        '''
        Create an AppointmentReason instance based on json input
        '''
        reason = json_info["reason"]
        duration = json_info["duration"]
        return AppointmentReason(reason, duration)
    

    