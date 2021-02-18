"""
Modulo responsável pela interação do usuario com as opções
referente as Vendas
"""

import datetime
import time
from pymongo import MongoClient
from classesMongo.Vendas import Vendas

bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

def menuVendas():
    opcaoVenda = 0
    while(opcaoVenda >=0) and (opcaoVenda <= 5):

        if opcaoVenda == 0:
            print('----------Menu principal de Fornecedores----------\n')
            print('Escolha uma das opções:')
            print('\t1 - Cadastrar Venda')
            print('\t2 - Listar Vendas')
            print('\t3 - Pesquisar Venda')
            print('\t4 - Remover Venda')
            print('\t5 - Voltar ao menu principal')
            try:
                opcaoVenda = int(input('Digite uma opção: '))
                if opcaoVenda > 5:
                    print('Opção inexistente.')
                    # time.sleep(2)
                    print('Retornando ao menu principal.')
                    # time.sleep(1)
                    opcaoVenda = 0

            except ValueError:

                opcaoVenda = 0

        elif opcaoVenda == 1:
            novaVenda = Vendas()
            print('----------Abrindo cadastro de Vendas----------')
            # time.sleep(1)
            print('----------Cadastro de Vendas----------')
            # time.sleep(1)
            data_hora = datetime.datetime.now()
            print(data_hora)
            novaVenda.data = input('Digite a data: ')
            novaVenda.hora = input('Digite a hora: ')
            codigo = input('Digite o CODIGO do produto da compra: ')
            produtos = banco.produtos
            doc = produtos.find_one({'codigo':codigo})

            if doc is None:
                print(f'Produto {codigo}, não encontrado.')
                opcaoVenda = - 1
            else:
                cpf = input('Digite o CPF do cliente que está comprando: ')
                cliente = banco.clientes
                doc2 = cliente.find_one({'cpf': cpf})
                if doc2 is None:
                    print(f'Cliente {cpf} não encontrado.')
                    opcaoVenda = - 1
                else:
                    novaVenda.cadastrarVenda(codigo, cpf)
                    print('Venda cadastrada com sucesso...')
                    # time.sleep(1)
                    opcaoVenda = - 1








