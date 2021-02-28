"""
Modulo responsável pela interação do usuario com as opções
referente as Vendas.
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

        if opcaoVenda == 0: #Interacao do menu principal da venda.
            print('----------Menu principal de Vendas----------\n')
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
                    time.sleep(2)
                    print('Retornando ao menu principal.')
                    time.sleep(1)
                    opcaoVenda = 0

            except ValueError:

                opcaoVenda = 0

        elif opcaoVenda == 1: #opcao de cadastro de venda.
            novaVenda = Vendas()
            print('----------Abrindo cadastro de Vendas----------')
            time.sleep(1)
            print('----------Cadastro de Vendas----------')
            time.sleep(1)
            data_hora = datetime.datetime.now() #chamada do datetime para informar hora e data para preenchimento do cadastro.
            print(data_hora) #impressao da data e da hora.
            novaVenda.data = input('Digite a data: ')
            novaVenda.hora = input('Digite a hora: ')
            codigo = input('Digite o CODIGO do produto da compra: ')

            produtos = banco.produtos #acesso a collecition produtos.
            doc = produtos.find_one({'codigo':codigo})

            if doc is None:
                print(f'Produto {codigo}, não encontrado.')
                opcaoVenda = - 1
            else: #O código só avança para o cpf do cliente, se o produto estiver cadastrado.
                cpf = input('Digite o CPF do cliente que está comprando: ')
                cliente = banco.clientes #acesso a collection clientes para verificar se o cliente é cadastrado.
                doc2 = cliente.find_one({'cpf': cpf})
                if doc2 is None:
                    print(f'Cliente {cpf} não encontrado.')
                    opcaoVenda = - 1
                else: #cadastro da venda, se o produto e o cliente estiverem cadastrado.
                    novaVenda.cadastrarVenda(codigo, cpf)
                    print('Venda cadastrada com sucesso...')
                    time.sleep(1)
                    opcaoVenda = - 1

        elif opcaoVenda == 2: #opcao de listar todas as vendas da collection.
            listarVendas = Vendas()
            print('----------Abrindo lista de Vendas ----------')
            time.sleep(1)
            print('--------- Lista Vendas---------\n')
            time.sleep(1)
            listarVendas.listarVendas()
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoVenda = -1

        elif opcaoVenda == 3: #opcao de buscar venda especifica pelo código da venda.
            buscarVenda = Vendas()
            print('----------Abrindo consulta de Vendas ----------')
            time.sleep(1)
            print('--------- Consultar Vendas ---------\n')
            time.sleep(1)
            codVenda = input('Digite o Código da Venda: ')
            buscarVenda.pesquisarVenda(codVenda)
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoVenda = -1

        elif opcaoVenda == 4: #opcao de remover venda.
            removerVenda = Vendas()
            print('----------Abrindo remoção de Vendas ----------')
            time.sleep(1)
            print('--------- Remover Venda ---------\n')
            time.sleep(1)
            codVenda = input('Digite o Código da Venda que deseja remover: ')
            removerVenda.removerVenda(codVenda)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoVenda = -1

        elif opcaoVenda == 5: #Opcao de voltar ao menu principal.
            pass







