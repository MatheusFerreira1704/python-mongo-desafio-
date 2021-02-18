"""
Desafio do curso de GamaAcademy + Accenture
Desenvolver um sistema de vendas com o mongo.
O Sistema deve ter um CRUD de:
Cliente, Fornecedores, Produtos e Vendas.
Produtos deve referenciar Forncedores e
Vendas, deve referenciar produtos, e clientes.
"""

#Main será a .py que vai armadezar o código do menu do principal,
#onde a aplicação começa e termina.

import time
from classesMenu.menuCliente import menuClientes
from classesMenu.menuFornecedor import menuFornecedores
from classesMenu.menuProduto import menuProdutos
from classesMenu.menuVenda import menuVendas

#Menu principal
opcao = 0
while (opcao >= 0) and (opcao <= 5):

    if opcao == 0:
        print('----------Menu Principal----------\n')
        print('Escolha uma das opções:')
        print('\t1 - Clientes')
        print('\t2 - Fornecedores')
        print('\t3 - Produtos')
        print('\t4 - Vendas')
        print('\t5 - Encerrar')
        try:
            opcao = int(input('Digite uma opção: '))
            if opcao > 5:
                print('Opção inexistente.')
                # time.sleep(2)
                print('Retornando ao menu principal.')
                # time.sleep(1)
                opcao =0

        except ValueError:
            opcao = 0
    elif opcao == 1:
        print('----------Abrindo Área do Ciente----------')
        # time.sleep(2)
        print('----------Área do Ciente----------\n')
        # time.sleep(1)
        menuClientes()

    elif opcao == 2:
        print('----------Abrindo Área do Fornecedor----------')
        # time.sleep(2)
        print('----------Área do Fornecedor----------\n')
        # time.sleep(1)
        menuFornecedores()
    elif opcao == 3:
        print('----------Abrindo Área de Produtos----------')
        # time.sleep(2)
        print('----------Área de Produtos----------\n')
        # time.sleep(1)
        menuProdutos()
    elif opcao == 4:
        print('----------Abrindo Área de Vendas----------')
        # time.sleep(2)
        print('----------Área das Vendas----------')
        # time.sleep(1)
        menuVendas()
        exit()
    elif opcao == 5:
        print('----------Programa Encerrado----------')
        exit()
    else:
        print('Digite um número válido.')
