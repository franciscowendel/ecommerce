from aux import float_to_str


class Product:

    contador: int = 0

    def __init__(self, nome: str, valor: float) -> None:
        self.__codigo = Product.contador
        self.__nome: str = nome
        self.__valor: float = valor
        Product.contador += 1

    @property
    def codigo(self) -> int:
        return self.codigo

    @property
    def nome(self) -> str:
        return self.nome


