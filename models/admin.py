from models.user import User

class Admin(User):
    def __init__(self, arg) -> None:
        User.__init__(self, arg["email_address"], arg["password"])