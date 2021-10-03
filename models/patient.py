from models.favourite_list import FavouriteList
from models.user import User

class Patient(User):
    def __init__(self, arg) -> None:
        ''' 
        arg: {
            email_address: str,
            password: str,
            first_name: str,
            last_name: str,
            phone_number: str,
            date_of_birth: datetime,
            gender: str,
            list_of_favourites: {list_of_favourites:[]}
        }
        '''
        User.__init__(self, arg["email_address"], arg["password"])
        self._first_name = arg["first_name"]
        self._last_name = arg["last_name"]
        self._phone_number = arg["phone_number"]
        self._date_of_birth = arg["date_of_birth"]
        self._gender = arg["gender"]
        self._list_of_favourites = FavouriteList(arg["list_of_favourites"])