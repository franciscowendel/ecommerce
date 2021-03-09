from passlib.hash import pbkdf2_sha256 as key


class User:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.__nome: str = nome

