from models.favourite_list import FavouriteList

class Patient():
    def __init__(self, info):
        ''' info: {
            first_name: "patient first name",
            last_name: "patient last name",
            phone_number: "0412345678",
            date_of_birth: "Jun 1 2005  1:33PM",
            gender: "male",
            list_of_favourites: {list_of_favourites:[]}
        }
        '''
        self.first_name: info["first_name"]
        self.last_name: info["last_name"]
        self.phone_number: info["phone_number"]
        self.date_of_birth: info["date_of_birth"]
        self.gender: info["gender"]
        self.list_of_favourites: FavouriteList(info["list_of_favourites"])