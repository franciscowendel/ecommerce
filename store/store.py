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
        print('1 - CADASTRAR PRODUTO: ')
        print('2 - LISTAR PRODUTOS: ')
        print('3 - COMPRAR PRODUTO: ')
        print('4 - VER CARRINHO: ')
        print('5 - FECHAR PEDIDO: ')
        print('6 - SAIR: ')
        print()

        opcao: int = int(input())

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            comprar_produto()
        elif opcao == 4:
            ver_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('VOLTE SEMPRE!')
            sleep(1)
            exit(1)
        else:
            print('OPÇÃO INVÁLIDA...')
            sleep(1)
            menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


def cadastrar_produto():
    try:
        print('-------------------')
        print('CADASTRAR PRODUTO: ')
        print('-------------------')
        print()
        nome: str = input('NOME DO PRODUTO: ')
        valor: float = float(input('VALOR DO PRODUTO: '))
        print()
        produto: Product = Product(nome, valor)

        print('------------------')
        print('DADOS DO PRODUTO: ')
        print('------------------')
        print()
        print(produto)
        produtos.append(produto)
        print()
        print('PRODUTO CADASTRADO COM SUCESSO!')
        print()
        sleep(1)
        menu()

    except (ValueError, TypeError) as err:
        return f'Erro do tipo {err} encontrado...'


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
