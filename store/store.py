from typing import List, Dict
from time import sleep
from product import Product
from userverify import User


produtos: List[Product] = []
carrinho: List[Dict[Product, int]] = []


def menu():
    try:
        print('-------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------- STORE --------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('O QUE DESEJA: ')
        print()


    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def cadastrar_produto():
    pass


def listar_produtos():
    pass


def comprar_produto():
    pass


def ver_carrinho():
    pass


def fechar_pedido():
    pass


def rastrear_produto(numero):
    pass


if __name__ == '__main__':
    menu()
