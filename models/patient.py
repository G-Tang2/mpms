from models.favourite_list import FavouriteList
from models.user import User

class Patient(User):
    def __init__(self, arg):
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
        self.first_name: arg["first_name"]
        self.last_name: arg["last_name"]
        self.phone_number: arg["phone_number"]
        self.date_of_birth: arg["date_of_birth"]
        self.gender: arg["gender"]
        self.list_of_favourites: FavouriteList(arg["list_of_favourites"])