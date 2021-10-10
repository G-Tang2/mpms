
class User():
    def __init__(self, email_address: str, password: str) -> None:
        self.email_address = email_address
        self.password = password

    def get_email_address(self) -> str:
        return self._email_address

    def set_email_address(self, email_address: str) -> bool:
        self._email_address = email_address
        return True

    def get_password(self) -> str:
        return self._password 

    def set_password(self, password: str) -> None:
        self._password = password
        return True

    
