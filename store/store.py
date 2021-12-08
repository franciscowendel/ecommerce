from typing import List, Dict
from time import sleep
from product import Product
from userverify import User
import datetime
from aux import float_to_str

produtos: List[Product] = []
carrinho: List[Dict[Product, int]] = []


def menu():
    """Mostra as opções do que pode ser feito para o usuário."""
    try:
        print('-------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------- STORE --------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('1 - CADASTRAR PRODUTO: ')
        print('2 - LISTAR PRODUTOS: ')
        print('3 - COMPRAR PRODUTO: ')
        print('4 - VER CARRINHO: ')
        print('5 - FECHAR PEDIDO: ')
        print('6 - SAIR: ')
        print()

        opcao = input()

        if not opcao.isnumeric() or opcao == '':
            print('ESCOLHA UMA OPÇÃO!')
            print()
            menu()
        else:
            opcao = int(opcao)
            if opcao > 6:
                print('ESCOLHA APENAS AS OPÇÕES APRESENTADAS.')
                menu()

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
            sleep(0.5)
            exit(1)
        else:
            print('OPÇÃO INVÁLIDA...')
            sleep(0.5)
            menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados...'


def cadastrar_produto():
    """Cadastra o produto e o adiciona na lista de produtos."""
    try:
        print('-------------------')
        print('CADASTRAR PRODUTO: ')
        print('-------------------')
        print()
        nome: str = input('NOME DO PRODUTO: ')
        if nome == '' or nome.isnumeric():
            print()
            print('DIGITE O NOME DO PRODUTO!')
            sleep(0.5)
            menu()
        valor = input('VALOR DO PRODUTO: ')
        if valor == '':
            print()
            print('DIGITE O VALOR DO PRODUTO!')
            sleep(0.5)
            menu()
        else:
            valor = float(valor)
        print()
        produto: Product = Product(nome, valor)

        print('------------------')
        print('DADOS DO PRODUTO: ')
        print('------------------')
        print()
        print('----------------------------')
        print(produto)
        print('----------------------------')
        produtos.append(produto)
        print()
        print('PRODUTO CADASTRADO COM SUCESSO!')
        print()
        sleep(0.5)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados...'


def listar_produtos():
    """Lista os produtos cadastrados ma lista de produtos."""
    if len(produtos) > 0:

        print('-------------------')
        print('LISTA DE PRODUTOS: ')
        print('-------------------')
        print()
        for produto in produtos:
            print(produto)
            print('-------------------')
            print()
            sleep(1)

    else:
        print('NENHUM PRODUTO CADATRADO...')
    sleep(1)
    menu()


def comprar_produto():
    """Adiciona o produto (informando o seu código) no carrinho."""
    try:
        if len(produtos) > 0:
            print('-------------------------------------------')
            print('CÓDIGO DO PRODUTO QUE VOCÊ DESEJA COMPRAR: ')
            print('-------------------------------------------')
            print()
            for produto in produtos:
                print('---------------------------')
                print(produto)
                print('---------------------------')
                print()

            numero: int = int(input())

            produto: Product = rastrear_produto(numero)

            if produto:
                if len(carrinho) > 0:
                    exist: bool = False

                    for item in carrinho:
                        quant: int = item.get(produto)

                        if quant:
                            item[produto] = quant + 1
                            print(f'PRODUTO {produto.nome} AGORA POSSUI {quant + 1} UNIDADES NO CARRINHO.')
                            exist: bool = True
                            print()
                            sleep(1)
                            menu()

                    if not exist:
                        prod: Dict[Product, int] = {produto: 1}
                        carrinho.append(prod)
                        print(f'O PRODUTO {produto.nome} FOI ADICIONADO NO CARRINHO COM SUCESSO!')
                        sleep(1)
                        menu()

                else:
                    item: Dict[Product, int] = {produto: 1}
                    carrinho.append(item)
                    print(f'O PRODUTO {produto.nome} FOI ADICIONADO NO CARRINHO COM SUCESSO!')
                    print()
                    sleep(1)
                    menu()

            else:
                print(f'PRODUTO COM CÓDIGO INFORMADO NÃO FOI ENCONTRADO.')
                print()
            sleep(1)
            menu()

        else:
            print('NENHUM PRODUTO CADASTRADO...')
        sleep(1)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados...'


def ver_carrinho():
    """Lista os produtos no carrinho."""
    if len(carrinho) > 0:

        print('----------')
        print('CARRINHO: ')
        print('----------')
        print()
        for item in carrinho:
            for dados in item.items():
                print('-------------------')
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-------------------')
                print()

    else:
        print('CARRINHO VAZIO...')
        print()
    sleep(1)
    menu()


def fechar_pedido():
    """Após informar os dados de usuário, o pedido é fechado, informando o total da fatura e o vencimento do boleto."""
    try:
        if len(carrinho) > 0:
            fatura: float = 0

            nome: str = input('NOME: ')
            if nome == '':
                exit(1)
            email: str = input('EMAIL: ')
            if email == '':
                exit(1)
            senha: str = input('SENHA: ')
            if senha == '':
                exit(1)
            confirma_senha: str = input('CONFIRME A SENHA: ')
            if confirma_senha == '':
                exit(1)
            print()

            if senha == confirma_senha:
                usuario: User = User(nome, email, senha)
            else:
                print('SENHA INCORRETA!')
                exit(1)

            print('USUÁRIO CRIADO COM SUCESSO!')
            print()

            senha: str = input('DIGITE A SENHA NOVAMENTE: ')
            print()

            if usuario.password_check(senha):  # noqa
                print('ACESSO PERMITIDO!')
            else:
                print('ACESSO NEGADO, SENHA INCORRETA!')

            print()

            print('----------------------')
            print('PRODUTOS NO CARRINHO: ')
            print('----------------------')
            print()
            for item in carrinho:
                for dados in item.items():
                    print('-------------------')
                    print(dados[0])
                    print(f'Quantidade: {dados[1]}')
                    fatura += dados[0].valor * dados[1]
                    print('-------------------')
                    print()

            data_compra = datetime.datetime.today()
            vencimento = datetime.timedelta(days=3)
            boleto = vencimento + data_compra
            print(f'TOTAL DA FATURA: {float_to_str(fatura)}')
            print()
            print(f'VENCIMENTO DO BOLETO: {boleto}')
            print()

        else:
            print('CARRINHO VAZIO...')
        sleep(1)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados...'


def rastrear_produto(numero):
    """Dá a possibilidade de pegarmos o produto pelo seu código."""
    x: Product = None  # noqa

    if len(produtos) > 0:
        for produto in produtos:
            if produto.codigo == numero:
                x: Product = produto
    return x


if __name__ == '__main__':
    menu()
