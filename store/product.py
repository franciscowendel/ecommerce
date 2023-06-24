from aux import float_to_str


class Product:

    numero: int = 1

    def __init__(self, nome: str, valor: float) -> None:
        self.__codigo = Product.contador
        self.__nome: str = nome
        self.__valor: float = valor
        Product.numero += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def valor(self) -> float:
        return self.__valor

    def __str__(self):
        return f'Código do produto: {self.codigo}\nNome do produto: {self.nome}\nValor do produto: {float_to_str(self.valor)}'  # noqa
