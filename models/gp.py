import json
from models.user import User

class GP():
    def __init__(self, json) -> None:
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.phone_number = json["phone_number"]
        self.area_of_interests = json["area_of_interests"]
        self.unavailable_days = json["unavailable_days"]

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)