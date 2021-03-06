"""
Modulo responsável pela interação do úsuario com as opções
referente aos clientes.
"""
import time
from classesMongo.Cliente import Clientes

def menuClientes():
    opcaoCliente = 0
    while(opcaoCliente >= 0) and (opcaoCliente <= 6):

        if opcaoCliente == 0: #Menu principal de interação.
            print('----------Menu principal de Clientes----------\n')
            print('Escolha uma das opções:')
            print('\t1 - Cadastrar Clientes')
            print('\t2 - Listar Clientes')
            print('\t3 - Pesquisar Cliente')
            print('\t4 - Atualizar Cliente')
            print('\t5 - Remover Cliente')
            print('\t6 - Voltar ao menu principal')
            try:
                opcaoCliente = int(input('Digite uma opção: '))
                if opcaoCliente > 6:
                    print('Opção inexistente.')
                    time.sleep(2)
                    print('Retornando ao menu principal.')
                    time.sleep(1)
                    opcaoCliente= 0

            except ValueError:
                opcaoCliente = 0

        elif opcaoCliente == 1: #Opção de persistência do documento cliente na collection.
            novoCliente = Clientes()
            print('---------- Abrindo cadastro de Clientes ----------')
            time.sleep(1)
            print('--------- Cadastro de Cliente ---------\n')
            time.sleep(1)

            novoCliente.Nome = input('Digite o nome do cliente: ')
            novoCliente.cpf = input('CPF: ')
            novoCliente.dtNascimento = input('Data de nascimento: ')
            novoCliente.Email = input('E-mail: ')
            novoCliente.inserir()

            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoCliente = -1

        elif opcaoCliente == 2: #opção de listar os clientes da collection
            listarClientes = Clientes()
            print('----------Abrindo lista de Cliente ----------')
            time.sleep(1)
            print('--------- Lista Cliente ---------\n')
            time.sleep(1)
            listarClientes.listaCliente()
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoCliente = -1

        elif opcaoCliente == 3: #Opção de consultar cliente especifico pelo CPF.
            buscarCliente = Clientes()
            print('----------Abrindo consulta de Cliente ----------')
            time.sleep(1)
            print('--------- Consultar Cliente ---------\n')
            time.sleep(1)
            cpf = input('Digite o CPF do cliente: ')
            buscarCliente.consultarCliente(cpf)
            time.sleep(1)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoCliente = -1

        elif opcaoCliente == 4: #Opcão de atualizar documento do cliente cadastrado.
            atualizarCliente = Clientes()
            print('----------Abrindo atualização de Cliente ----------')
            time.sleep(1)
            print('--------- Atualizar Cliente ---------\n')
            time.sleep(1)
            cpf = input('Digite o CPF do cliente que deseja alterar: ')
            print(
                f'Qual alteracao deseja fazer no CPF:{cpf}?\n'
                f'\t1 - Alterar Nome\n'
                f'\t2 - Alterar CPF\n'
                f'\t3 - Alterar Data de Nascimento\n'
                f'\t4 - Alterar email') #interação com o usuário sobre quais informações ele deseja atualizar do cliente.
            time.sleep(1)
            try:
                opcaoDeAtualizar = int(input('Digite tua opcao: '))
            except ValueError:
                opcaoDeAtualizar = -1

            if opcaoDeAtualizar == 1: #opcao de atualizar nome do cliente.
                novoNome = input('Digite o nome: ')
                atualizarCliente.atualizaCliente(cpf, dado='Nome', valor=novoNome)
                print('Nome atualizado com sucesso...')

            elif opcaoDeAtualizar == 2: #opcao de atualizar cpf
                novoCpf = input('Digite o cpf: ') #input do novo cpf
                atualizarCliente.atualizarCliente(cpf, dado='cpf', valor=novoCpf)
                print('CPF atualizado com sucesso...')

            elif opcaoDeAtualizar == 3: #opcao de atualizar data de nascimento
                novaData = input('Digite a Data de Nascimento: ') #input da data de nascimento.
                atualizarCliente.atualizarCliente(cpf, dado='dtNascimento', valor=novaData)
                print('Data de nascimento atualizada com sucesso...')

            elif opcaoDeAtualizar == 4: #opcao de atualizar email
                novoEmail = input('Digite o novo E-mail: ') #input do novo e-mail
                atualizarCliente.atualizarCliente(cpf, dado='Email', valor=novoEmail)
                print('E-mail atualizado com sucesso...')

            else:
                print('Opção inválida.')
                print('Retornando ao menu principal...')
                time.sleep(1)

            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoCliente = -1

        elif opcaoCliente == 5: #Opção de remoção de cliente.
            removerCliente = Clientes()
            print('----------Abrindo remoção de Cliente ----------')
            time.sleep(1)
            print('--------- Remover Cliente ---------\n')
            time.sleep(1)
            cpf = input('Digite o CPF do cliente que deseja remover: ')
            removerCliente.removerCliente(cpf)
            print('Retornando ao menu principal...')
            time.sleep(1)
            opcaoCliente = -1

        elif opcaoCliente == 6: #Opção de voltar ao menu principal.
            pass



