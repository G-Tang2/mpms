from models.user import User

class Admin(User):
    def __init__(self, email_address: str, password: str) -> None:
        User.__init__(self, email_address, password)

    @staticmethod
    def create_from_json(json_info):
        email_address = json_info["email_address"]
        password = json_info["password"]
        return Admin(email_address, password)