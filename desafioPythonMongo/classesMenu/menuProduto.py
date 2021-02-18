"""
Modulo responsável pela interação do usuario com as opções
referente aos produtos
"""

import time
from classesMongo.Produto import Produtos
from pymongo import MongoClient

bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.


def menuProdutos():
    opcaoProduto = 0
    while (opcaoProduto >= 0 ) and (opcaoProduto <= 5):

        if opcaoProduto == 0:
            print('----------Menu principal de Fornecedores----------\n')
            print('Escolha uma das opções:')
            print('\t1 - Cadastrar Produto')
            print('\t2 - Listar Produtos')
            print('\t3 - Pesquisar Produto')
            print('\t4 - Remover Produto')
            print('\t5 - Voltar ao menu principal')
            try:
                opcaoProduto = int(input('Digite uma opção: '))
                if opcaoProduto > 5:
                    print('Opção inexistente.')
                    # time.sleep(2)
                    print('Retornando ao menu principal.')
                    # time.sleep(1)
                    opcaoProduto = 0

            except ValueError:
                opcaoProduto = 0

        elif opcaoProduto == 1:
            novoProduto = Produtos()
            print('----------Abrindo cadastro de Produtos----------')
            # time.sleep(1)
            print('----------Cadastro de Produtos----------')
            # time.sleep(1)

            novoProduto.categoria = input('Categoria do produto: ')
            novoProduto.nome = input('Nome do produto: ')
            novoProduto.codigo = input('Código do produto: ')
            novoProduto.preco = input('Preço: ')
            cnpj = input('CNPJ do fornecedor: ')

            fornecedor = banco.fornecedores
            doc = fornecedor.find_one({'cnpj': cnpj})

            if doc is None:
                print(f'Fornecedor {cnpj}, não encontrado.')
            else:
                novoProduto.inserir(cnpjFornecedor=cnpj)
            # time.sleep(1)
            opcaoProduto = -1