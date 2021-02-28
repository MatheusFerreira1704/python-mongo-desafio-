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
    while (opcaoProduto >= 0) and (opcaoProduto <= 5):

        if opcaoProduto == 0: #Interação do menu principal do Produto.
            print('----------Menu principal de Produto----------\n')
            print('Escolha uma das opções:')
            print('\t1 - Cadastrar Produto')
            print('\t2 - Listar Produtos')
            print('\t3 - Pesquisar Produto')
            print('\t4 - Atualizar Produto')
            print('\t5 - Remover Produto')
            print('\t6 - Voltar ao menu principal')
            try:
                opcaoProduto = int(input('Digite uma opção: '))
                if opcaoProduto > 5:
                    print('Opção inexistente.')
                    time.sleep(2)
                    print('Retornando ao menu principal.')
                    time.sleep(1)
                    opcaoProduto = 0

            except ValueError:
                opcaoProduto = 0

        elif opcaoProduto == 1: #Opção de cadastro do produto
            novoProduto = Produtos()
            print('----------Abrindo cadastro de Produtos----------')
            time.sleep(1)
            print('----------Cadastro de Produtos----------')
            time.sleep(1)

            novoProduto.categoria = input('Categoria do produto: ')
            novoProduto.nome = input('Nome do produto: ')
            novoProduto.codigo = input('Código do produto: ')
            novoProduto.preco = input('Preço: ')
            cnpj = input('CNPJ do fornecedor: ')

            fornecedor = banco.fornecedores #acesso a collection fornecedores.
            doc = fornecedor.find_one({'cnpj': cnpj}) #busca do doc do fornecedor.

            if doc is None:
                print(f'Fornecedor {cnpj}, não encontrado.')
            else:
                novoProduto.inserir(cnpjFornecedor=cnpj)
            time.sleep(1)
            opcaoProduto = -1

        elif opcaoProduto == 2: #opcao de listar todos os produtos da collection
            listarProdutos = Produtos()
            print('----------Abrindo lista de Produtos ----------')
            time.sleep(1)
            print('--------- Lista Produtos ---------\n')
            time.sleep(1)
            listarProdutos.listarProdutos()
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoProduto = -1

        elif opcaoProduto == 3: #Opção de pesquisar produto especifico pelo código.
            pesquisarProduto = Produtos()
            print('----------Abrindo busca de Produtos ----------')
            time.sleep(1)
            print('--------- Buscar Produtos ---------\n')
            time.sleep(1)
            codigo = input('Digite o CÓDIGO do produto: ')
            pesquisarProduto.pesquisarProduto(codigo)
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoProduto = -1

        elif opcaoProduto == 4: #opcão de atualizar produto.
            atualizarProduto = Produtos()
            print('---------- Abrindo atualização de Produto ----------')
            time.sleep(1)
            print('--------- Atualizar Produto ---------\n')
            time.sleep(1)
            codigo = input('Digite o CÓDIGO do produto que deseja atualizar: ')
            print(
                'Qual alteração deseja fazer no produto? \n'
                '\t1 - Alterar Categoria.\n'
                '\t2 - Alterar Nome.\n'
                '\t3 - Alterar Código.\n'
                '\t4 - Alterar Preço.\n'
                '\t5 - Alterar Fornecedor.\n') #menu de interação de atualização do produto.
            time.sleep(1)
            try:
                opcaoDeAtualizar = int(input('Digite uma opção: '))
            except ValueError:
                opcaoDeAtualizar = -1

            if opcaoDeAtualizar == 1: #opção de atualizar categoria
                novaCategoria = input('Digite a categoria: ') #input da nova categoria
                atualizarProduto.atualizarProduto(codigo, dado='categoria', valor=novaCategoria)
                print('Categoria atualizada com sucesso...')

            if opcaoDeAtualizar == 2: #opcao de atualizar nome do produto.
                novoNome = input('Digite o nome: ') #input do novo nome.
                atualizarProduto.atualizarProduto(codigo, dado='nome', valor=novoNome)
                print('Nome do produto atualizado com sucesso...')

            if opcaoDeAtualizar == 3: #opcao de atualizar codigo do produto.
                novoCodigo = input('Digite o código: ') #input do novo código
                atualizarProduto.atualizarProduto(codigo, dado='codigo', valor=novoCodigo)
                print('Código do produto atualizado com sucesso...')

            if opcaoDeAtualizar == 4: #opcao de atualizar preço do produto.
                novoPreco = input('Digite o preço: ') #input do novo preço
                atualizarProduto.atualizarProduto(codigo, dado='preco', valor=novoPreco)
                print('Preço atualizado com sucesso...')

            if opcaoDeAtualizar == 5: #opção de atualizar fornecedor do produto.
                novoFornecedor = input('Digite o CNPJ do novo fornecedor: ') #input do CNPJ do fornecedor.

                fornecedor = banco.fornecedores  # acessar banco do fornecedor
                doc_Fornecedor = fornecedor.find_one({'CNPJ': novoFornecedor})  # encontrar dados do fornecedor

                if (doc_Fornecedor is None):
                    print(f'O CNPJ {novoFornecedor} não está inserido no sistema.')

                else: #só atualiza se o fornecedor estiver cadastrado.
                    atualizarProduto.atualizaProduto(codigo, dado='fornecedor', valor=doc_Fornecedor)

            else:
                opcaoProduto = -1
            time.sleep(1)

        elif opcaoProduto == 5: #Opção de remover produto.
            removerProduto = Produtos()
            print('---------- Abrindo remoção de Produto ----------')
            time.sleep(1)
            print('--------- Remover Produto ---------\n')
            time.sleep(1)
            codigo = input('Digite o CÓDIGO do produto que deseja remover: ')
            removerProduto.removerProduto(codigo)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoProduto = -1

        elif opcaoProduto == 6: #Opção de voltar ao menu principal.
            pass