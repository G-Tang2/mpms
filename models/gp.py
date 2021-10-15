from datetime import datetime
import json
from typing import List
from utils.json import JSON

class GP():
    def __init__(self, first_name: str, last_name: str, phone_number: str, area_of_interests: List[str],
            unavailable_days: List[datetime]) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.area_of_interests = area_of_interests
        self.unavailable_days = unavailable_days
        
    def get_full_name(self) -> str:
        '''
        Returns gp's full name
        '''
        return "{} {}".format(self.first_name, self.last_name)

    def to_JSON(self) -> json:
        '''
        Returns a json object from this AppointmentList instance
        '''
        return JSON.to_JSON(self)

    @staticmethod
    def create_from_json(json_info):
        '''
        Create a GP instance based on json input
        '''
        first_name = json_info["first_name"]
        last_name = json_info["last_name"]
        phone_number = json_info["phone_number"]
        area_of_interests = json_info["area_of_interests"]
        unavailable_days = json_info["unavailable_days"]
        return GP(first_name, last_name, phone_number, area_of_interests, unavailable_days)