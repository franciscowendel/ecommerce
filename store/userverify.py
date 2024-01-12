from passlib.hash import pbkdf2_sha256 as key


class User:
    def __init__(self, name: str, email: str, password: str) -> None:
        self.__name: str = name
        self.__email: str = email
        self.__password: str = key.hash(password, rounds=200000, salt_size=16)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def password(self) -> str:
        return self.__password

    def _password_check(self, password):
        """Checks if the password given by the user is correct."""
        if key.verify(password, self.password):
            return True
        return False
