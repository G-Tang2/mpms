from models.favourite_list import FavouriteList
from models.user import User
from datetime import datetime
import copy

class Patient(User):
    def __init__(self, email_address: str, password: str, first_name: str, last_name: str,
            phone_number: str, date_of_birth: datetime, gender: str, list_of_favourites = FavouriteList()) -> None:
        User.__init__(self, email_address, password)
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.list_of_favourites = list_of_favourites

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def serialise_copy(self):
        '''
        Return a serialisable version of this patient instance
        '''
        tmp = copy.deepcopy(self)
        tmp.date_of_birth = tmp.date_of_birth.strftime("%Y-%m-%dT%H:%M:%S")
        return tmp

    @staticmethod
    def create_from_json(json_info):
        '''
        Create a patient instance based on json input
        '''
        email_address = json_info["email_address"]
        password = json_info["password"]
        first_name = json_info["first_name"]
        last_name = json_info["last_name"]
        phone_number = json_info["phone_number"]
        date_of_birth = datetime.strptime(json_info["date_of_birth"], "%Y-%m-%dT%H:%M:%S")
        gender = json_info["gender"]
        list_of_favourites = FavouriteList.create_from_json(json_info["list_of_favourites"])
        return Patient(email_address, password, first_name, last_name, phone_number, date_of_birth,
            gender, list_of_favourites)