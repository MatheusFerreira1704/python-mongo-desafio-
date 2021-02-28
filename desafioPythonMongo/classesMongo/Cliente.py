"""
Modulo responsável por conter a implementação do CRUD do Cliente.
"""

import time
#importação do client do mongoDB
from pymongo import MongoClient


bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

class Clientes(object):

    def inserir(self): #função de persistencia do clinete no banco de dados.
        cliente = {
            'Nome': self.Nome,
            'cpf': self.cpf,
            'dtNascimento': self.dtNascimento,
            'Email': self.Email
        }
        clientes = banco.clientes
        clientes.insert_one(cliente)
        time.sleep(1)
        print(f'Cliente inserido com sucesso...')

    def listaCliente(self): #função para listar todos os clientes cadastrados no banco.
        clientes = banco.clientes
        for doc in clientes.find():
            print(f"Nome: {doc['Nome']}\nCPF: {doc['cpf']}\nData de Nascimento: {doc['dtNascimento']}\nEmail: {doc['Email']}\n")

    def consultarCliente(self, cpf): #função para buscar um cliente especifico pelo cpf.
        clientes = banco.clientes
        doc = clientes.find_one({'cpf': cpf})
        print('Buscando cliente.')
        time.sleep(1)
        if doc is None:
            print('CPF não encontrado.')
        else:
            print(f"Nome: {doc['Nome']}\nCPF: {doc['cpf']}\nData de Nascimento: {doc['dtNascimento']}\nEmail: {doc['Email']}\n")

    def atualizarCliente(self, cpf, dado, valor): #função utilizada para atualizar informações do cliente cadastrado.
        clientes = banco.clientes
        doc = clientes.find_one({'cpf': cpf})
        if doc is None:
            print('Cliente não encontrado. ')
        else:
            clientes.update_one({'cpf': cpf},{
                "$set": {
                    f'{dado}': valor
                }
            })

    def removerCliente(self, cpf): #função para remover cliente do banco, utilizando CPF como buscador.
        clientes = banco.clientes
        doc = clientes.find_one({'cpf':cpf})
        if doc is None:
            print('CPF não encontrado.')
        else:
            clientes.delete_one(doc)

    def buscarCliente(self, cpf): #Função de buscar de documento Cliente, para inserir no cadastro da venda.
        clientes = banco.clientes
        doc = clientes.find_one({'cpf': cpf})
        print('Buscando cliente.')
        time.sleep(1)
        if (doc is None):
            print('CPF não encontrado.')
        else:
            print('Cliente encontrado.')
            time.sleep(1)
            return doc




