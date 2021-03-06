from models.user import User

class Admin(User):
    def __init__(self, email_address: str, password: str) -> None:
        User.__init__(self, email_address, password)

    def __str__(self) -> str:
        return "Admin"

    @staticmethod
    def create_from_json(json_info):
        '''
        Create an Admin instance based on json input
        '''
        email_address = json_info["email_address"]
        password = json_info["password"]
        return Admin(email_address, password)