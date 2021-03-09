from passlib.hash import pbkdf2_sha256 as key


class User:
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.__nome: str = nome
        self.__email: str = email
        self.__senha: str = key.hash(senha, rounds=200000, salt_size=16)

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email
