from auxiliary import float_to_str


class Product:

    number: int = 1

    def __init__(self, name: str, price: float) -> None:
        self.__code = Product.number
        self.__name: str = name
        self.__price: float = price
        Product.number += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self):
        return f"Product's code: {self.code}\nProduct's name: {self.nome}\nProduct's price: {float_to_str(self.price)}"  # noqa
