from typing import List, Dict
from time import sleep

from MercadoPy.models.produto import Produto
from MercadoPy.utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    """Menu de opções do sistema"""
    print('=============================================')
    print('=============== Bem vindo(a) ================')
    print('================= Geek Shop =================')
    print('=============================================')

    print('Selecione uma opção abaixo:')
    print('1- Cadastrar produto')
    print('2- Listar produto')
    print('3- Comprar produto')
    print('4- Vizualizar carrinho')
    print('5- Fechar pedido')
    print('6- Sair do sistema')

    opcao: int = int(input())
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        vizualiar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2) # congela o programa por 2 segundos
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()

def cadastrar_produto() -> None:
    """É cadastrado um novo produto no carrinho"""
    print('Cadastro de produto')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    menu()

def listar_produto() -> None:
    """São listaedos os produtos do carrinho"""
    if len(produtos) > 0:
        print('Listagem de produtos:')
        print('---------------------')
        for produto in produtos:
            print(produto)
            print('-------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados!')
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos)>0:
        print('Informe o código do produto que deseja adicionar no carrinho:')
        print('-------------------------------------------------------------')
        print('=================== Produtos disponíveis ====================')
        for produto in produtos:
            print(produto)
            print('-------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pagar_produto_por_codigo(codigo)
        if produto:
            if len(carrinho)>0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para serem vendidos...')
    sleep(2)
    menu()

def vizualiar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('----------------------------')
                sleep(1)
        menu()
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def fechar_pedido() -> None:
    """Caso já existam produtos no carrinho eles gerarão um valor total e o carrinho será esvaziado"""
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                #o preço de cada produto multiplicado pela quantidade do mesmo no carrinho
        print(f'A sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho...')
        sleep(2)
        menu()

def pagar_produto_por_codigo(codigo: int) -> Produto:
    """O usuário informa um código e assim é retornado o produto do respectivo código"""
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()