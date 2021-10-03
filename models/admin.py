from models.user import User

class Admin(User):
    def __init__(self, email_address: str, password: str) -> None:
        User.__init__(self, email_address, password)