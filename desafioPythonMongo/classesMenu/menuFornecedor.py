"""
Modulo responsável pela interação do usuario com as opções
referente aos fornecedores
"""

import time
from classesMongo.Fornecedor import Fornecedores

def menuFornecedores():
    opcaoFornecedor = 0
    while(opcaoFornecedor >= 0) and (opcaoFornecedor <= 6):

        if opcaoFornecedor == 0: #Menu principal de interação.
            print('----------Menu principal de Fornecedores----------\n')
            print('Escolha uma das opções:')
            print('\t1 - Cadastrar Fornecedor')
            print('\t2 - Listar Fornecedores')
            print('\t3 - Pesquisar Fornecedor')
            print('\t4 - Atualizar Fornecedor')
            print('\t5 - Remover Fornecedor')
            print('\t6 - Voltar ao menu principal')
            try:
                opcaoFornecedor = int(input('Digite uma opção: '))
                if opcaoFornecedor > 5:
                    print('Opção inexistente.')
                    time.sleep(2)
                    print('Retornando ao menu principal.')
                    time.sleep(1)
                    opcaoFornecedor = 0

            except ValueError:

                opcaoFornecedor = 0

        elif opcaoFornecedor == 1: #Opção de cadastro de fornecedor..
            novoFornecedor = Fornecedores()
            print('----------Abrindo cadastro de Fornecedores----------')
            time.sleep(1)
            print('----------Cadastro de Fornecedores----------')
            time.sleep(1)

            novoFornecedor.razao_social = input('Digite o nome social: ')
            novoFornecedor.cnpj = input('cnpj: ')
            novoFornecedor.representante = input('Representante: ')
            novoFornecedor.telefone = input('Telefone: ')
            novoFornecedor.inserir()

            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoFornecedor = -1

        elif opcaoFornecedor == 2: #Opção de listar.
            listarFornecedores = Fornecedores()
            print('----------Abrindo lista de Fornecedores ----------')
            time.sleep(1)
            print('--------- Lista Fornecedores ---------\n')
            time.sleep(1)
            listarFornecedores.listarFornecedores()
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoFornecedor = -1

        elif opcaoFornecedor == 3: #Opção consulta especifica de fornecedor.
            buscarFornecedor = Fornecedores()
            print('----------Abrindo consulta de Fornecedores ----------')
            time.sleep(1)
            print('--------- Consultar Fornecedores ---------\n')
            time.sleep(1)
            cnpj = input('Digite o CNPJ do fornecedor: ')
            buscarFornecedor.consultarFornecedores(cnpj)
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoFornecedor = -1

        elif opcaoFornecedor == 4: #Opção de atualização de forncedor.
            atualizarFornecedor = Fornecedores()
            print('---------- Abrindo atualização de Fornecedor ----------')
            time.sleep(1)
            print('--------- Atualizar Fornecedor ---------\n')
            time.sleep(1)
            cnpj = input('Digite o CNPJ do Fornecedor que deseja atualizar: ')
            print(
                f'Qual alteracao deseja fazer no CPF:{cnpj}?\n'
                f'\t1 - Alterar Razão Social.\n'
                f'\t2 - Alterar CNPJ.\n'
                f'\t3 - Alterar Representante.\n'
                f'\t4 - Alterar Telefone.') #interação com o usuário sobre quais informações ele deseja atualizar do fornecedor.
            time.sleep(1)
            try:
                opcaoDeAtualizar = int(input('Digite uma opcao: '))
            except ValueError:
                opcaoDeAtualizar = -1

            if opcaoDeAtualizar == 1: #Opcao de atualizar razao social do fornecedor.
                novaRazaoSocial = input('Digite o novo nome da Empresa: ')# input da nova razao social do fornecedor.
                atualizarFornecedor.atualizarFornecedor(cnpj, dado='razao_social', valor=novaRazaoSocial)
                print('Nome da Empresa atualizado com sucesso...')

            elif opcaoDeAtualizar == 2: #opcao de atualizar cnpj do fornecedor.
                novoCnpj = input('Digite o CNPJ: ') #input do cnpj
                atualizarFornecedor.atualizarFornecedor(cnpj, dado='cnpj', valor=novoCnpj)
                print('CNPJ atualizado com sucesso...')

            elif opcaoDeAtualizar == 3: #opcao de atualizar representante.
                novoRepresentante = input('Digite o nome do Representante: ') #input do nome do representante.
                atualizarFornecedor.atualizarFornecedor(cnpj, dado='representante', valor=novoRepresentante)
                print('Representante atualizado(a) com sucesso...')

            elif opcaoDeAtualizar == 4: #opcao de atualizar telefone.
                novoTelefone = input('Digite o novo Telefone: ') #input do telefone.
                atualizarFornecedor.atualizarFornecedor(cnpj, dado='telefone', valor=novoTelefone)
                print('Telefone atualizado com sucesso...')

            else:
                print('Opção inválida.')
                print('Retornando ao menu principal...')
                time.sleep(1)

            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoFornecedor = -1

        elif opcaoFornecedor == 5: #Opção de remoção de Fornecedores.
            removerFornecedor = Fornecedores()
            print('----------Abrindo remoção de Fornecedor ----------')
            time.sleep(1)
            print('--------- Remover Fornecedor ---------\n')
            time.sleep(1)
            cnpj = input('Digite o CNPJ do Fornecedor que deseja remover: ')
            removerFornecedor.removerFornecedor(cnpj)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoFornecedor = -1

        elif opcaoFornecedor == 6: #Opção de voltar ao menu principal.
            pass
