"""
Modulo responsável pela interação do usuario com as opções
referente aos fornecedores
"""

import time
from classesMongo.Fornecedor import Fornecedores

def menuFornecedores():
    opcaoFornecedor = 0
    while(opcaoFornecedor >= 0) and (opcaoFornecedor <= 5):

        if opcaoFornecedor == 0:
            print('----------Menu principal de Fornecedores----------\n')
            print('Escolha uma das opções:')
            print('\t1 - Cadastrar Fornecedor')
            print('\t2 - Listar Fornecedores')
            print('\t3 - Pesquisar Fornecedor')
            print('\t4 - Remover Fornecedor')
            print('\t5 - Voltar ao menu principal')
            try:
                opcaoFornecedor = int(input('Digite uma opção: '))
                if opcaoFornecedor > 5:
                    print('Opção inexistente.')
                    # time.sleep(2)
                    print('Retornando ao menu principal.')
                    # time.sleep(1)
                    opcaoFornecedor = 0

            except ValueError:

                opcaoFornecedor = 0

        elif opcaoFornecedor == 1:
            novoFornecedor = Fornecedores()
            print('----------Abrindo cadastro de Fornecedores----------')
            # time.sleep(1)
            print('----------Cadastro de Fornecedores----------')
            # time.sleep(1)

            novoFornecedor.razao_social = input('Digite o nome social: ')
            novoFornecedor.cnpj = input('cnpj: ')
            novoFornecedor.representante = input('Representante: ')
            novoFornecedor.telefone = input('Telefone: ')
            novoFornecedor.inserir()

            # time.sleep(1)
            print('Retornando ao menu principal...')
            # time.sleep(1)
            opcaoFornecedor = -1
