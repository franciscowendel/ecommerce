from typing import List, Dict
from time import sleep
from product import Product
from userverify import User
import datetime
from auxiliary import float_to_str

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def store():
    """Shows the options that the user can choose."""
    try:
        print('-------------------------------------------------------------------------------------------------------')
        print('---------------------------------------------- STORE --------------------------------------------------')
        print('-------------------------------------------------------------------------------------------------------')
        print()
        print('1 - Register product: ')
        print('2 - List products: ')
        print('3 - Buy product: ')
        print('4 - Cart: ')
        print('5 - Close order: ')
        print('6 - Quit: ')
        print()

        option = input()

        if not option.isnumeric() or option == '':
            print()
            print('Choose an option!')
            print()
            sleep(0.5)
            store()
        else:
            option = int(option)
            if option > 6:
                print()
                print('Type one of the options that were given.')
                print()
                sleep(0.5)
                store()

        if option == 1:
            register_product()
        elif option == 2:
            list_products()
        elif option == 3:
            buy_product()
        elif option == 4:
            see_cart()
        elif option == 5:
            close_order()
        elif option == 6:
            print()
            print('...')
            sleep(0.5)
            exit(1)
        else:
            print()
            print('Invalid option...')
            print()
            sleep(0.5)
            store()

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def register_product():
    """Registers a product and place it in the product list."""
    try:
        print('-------------------')
        print('Register product: ')
        print('-------------------')
        print()
        name: str = input('NAME: ')
        if name == '' or name.isnumeric():
            print()
            print("Type the product's name!")
            print()
            sleep(0.5)
            store()
            
        price = input('Price: ')
        if price == '' or not price.isnumeric():
            print()
            print("Type the product's price")
            print()
            sleep(0.5)
            store()
        else:
            price = float(price)
            if price < 1:
                print()
                print('Only positive prices!')
                print()
                sleep(0.5)
                store()
                
        print()
        product: Product = Product(name, price)

        print('----------------')
        print("Product's info: ")
        print('----------------')
        print()
        print('----------------------------')
        print(product)
        print('----------------------------')
        products.append(product)
        print()
        print('Product registered successfully!')
        print()
        sleep(0.5)
        store()

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def list_products():
    """Lists all the registered products."""
    if len(products) > 0:

        print('----------------')
        print("Product's list: ")
        print('----------------')
        print()
        for product in products:
            print('--------------------------')
            print(product)
            print('--------------------------')
            print()
            sleep(0.5)

    else:
        print('Zero registered products...')
    sleep(0.5)
    store()


def buy_product():
    """Adds a product -- by giving its code! --, to the cart."""
    try:
        if len(products) > 0:
            print('-------------------------------------------------')
            print("Type the product's code that you want to buy it: ")
            print('-------------------------------------------------')
            print()
            for product in products:
                print('---------------------------')
                print(product)
                print('---------------------------')
                print()

            code = input()
            if code == '' or not code.isnumeric():
                print()
                print("Type the product's code!")
                print()
                sleep(0.5)
                store()
            else:
                code = int(code)

            product = get_product_by_code(code)

            if product:
                if len(cart) > 0:
                    exist: bool = False

                    for item in cart:
                        quantity: int = item.get(product)

                        if quantity:
                            item[product] = quantity + 1
                            print()
                            print(f'Product {produto.name} now has {quantity + 1} units in the cart.')
                            print()
                            exist: bool = True
                            sleep(0.5)
                            store()

                    if not exist:
                        prod: Dict[Product, int] = {product: 1}
                        cart.append(prod)
                        print()
                        print(f'The product {produto.name} has been added to the cart successfully!')
                        print()
                        sleep(0.5)
                        store()

                else:
                    item: Dict[Product, int] = {product: 1}
                    cart.append(item)
                    print()
                    print(f'The product {produto.name} has been added to the cart successfully!')
                    print()
                    sleep(0.5)
                    store()

            else:
                print()
                print(f"This product does not exist.")
                print()
            sleep(0.5)
            store()

        else:
            print()
            print('Zero registered products...')
            print()
        sleep(0.5)
        store()

    except (ValueError, TypeError) as err:
        return f'Errors {err} found...'


def see_cart():
    """Lists all the products in the cart."""
    if len(cart) > 0:

        print('------')
        print('Cart: ')
        print('------')
        print()
        for item in cart:
            for data in item.items():
                print('-------------------')
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('-------------------')
                print()

    else:
        print()
        print('Empty cart...')
        print()
    sleep(0.5)
    store()


def fechar_pedido():
    """Após informar os dados de usuário, o pedido é fechado informando o total da fatura e o vencimento do boleto."""
    try:
        if len(carrinho) > 0:
            fatura: float = 0

            nome: str = input('NOME: ')
            if nome == '' or nome.isnumeric():
                print('DIGITE O SEU NOME!')
                print()
                menu()
            email: str = input('EMAIL: ')
            if email == '' or email.isnumeric():
                print('DIGITE SEU EMAIL!')
                print()
                menu()
            senha: str = input('SENHA: ')
            if senha == '':
                print('DIGITE SUA SENHA!')
                print()
                menu()
            confirma_senha: str = input('CONFIRME A SENHA: ')
            if confirma_senha == '':
                print('CONFIRME A SUA SENHA!')
                print()
                menu()
            print()

            if senha == confirma_senha:
                usuario: User = User(nome, email, senha)
            else:
                print('SENHA INCORRETA!')
                menu()

            print('USUÁRIO CRIADO COM SUCESSO!')
            print()

            senha_2: str = input('DIGITE A SENHA NOVAMENTE: ')
            if senha_2 == '':
                print()
                print('CONFIRME A SENHA NOVAMENTE!')
                print()
                sleep(0.5)
                menu()

            if usuario.password_check(senha_2): # noqa
                print()
                print('ACESSO PERMITIDO!')
                print()
            else:
                print()
                print('ACESSO NEGADO, SENHA INCORRETA!')
                print()

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
            dia_limite = vencimento + data_compra
            formato_data_br = dia_limite.strftime('%d/%m/%Y')
            print(f'TOTAL DA FATURA: {float_to_str(fatura)}\nVENCIMENTO DA FATURA: {formato_data_br}')
            print()
            exit(1)

        else:
            print('CARRINHO VAZIO...')
        sleep(0.5)
        menu()

    except (ValueError, TypeError, UnboundLocalError) as err:
        return f'Erros do tipo {err} encontrados...'


def get_product_by_code(code):
    """Function made to get the right product in the function 'buy_product'. """
    x: Product = None  # noqa

    if len(products) > 0:
        for product in products:
            if product.code == code:
                x = product
    return x


if __name__ == '__main__':
    store()
