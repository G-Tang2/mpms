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
        self.__first_name: arg["first_name"]
        self.__last_name: arg["last_name"]
        self.__phone_number: arg["phone_number"]
        self.__date_of_birth: arg["date_of_birth"]
        self.__gender: arg["gender"]
        self.__list_of_favourites: FavouriteList(arg["list_of_favourites"])