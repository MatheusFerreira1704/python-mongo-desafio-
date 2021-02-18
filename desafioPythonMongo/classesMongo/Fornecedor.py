"""
Modulo responsável pelo CRUD refernete ao fornecedor.
"""
# função time, que implementa um delay na aplicação.
import time
#Importação do Client do mongoDB
from pymongo import MongoClient

bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

class Fornecedores(object):

    def inserir(self):
        fornecedor = {
            'razao_social': self.razao_social,
            'cnpj': self.cnpj,
            'representate': self.representante,
            'telefone': self.telefone
        }
        fornecedores = banco.fornecedores
        fornecedores.insert_one(fornecedor)
        # time.sleep(1)
        print('Fornecedor inserido com sucesso...')

    def referenciador(self, codigoCNPJ):
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'cnpj': codigoCNPJ})
        print('Buscando fornecedor')
        # time.sleep(1)
        if (doc is None):
            print('CNPJ não encontrado.')
        else:
            print('Fornecedor encontrado.')
            # time.sleep(1)
            return doc

