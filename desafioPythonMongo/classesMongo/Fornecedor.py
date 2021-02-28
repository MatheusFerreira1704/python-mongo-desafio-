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

    def inserir(self): #persistência do documento fornecedor na collection.
        fornecedor = {
            'razao_social': self.razao_social,
            'cnpj': self.cnpj,
            'representate': self.representante,
            'telefone': self.telefone
        }
        fornecedores = banco.fornecedores
        fornecedores.insert_one(fornecedor)
        time.sleep(1)
        print('Fornecedor inserido com sucesso...')

    def listarFornecedores(self): #função que mostra a lista de fornecedores cadastrados.
        fornecedores = banco.fornecedores
        for doc in fornecedores.find():
            print(f"Razão Social: {doc['razao_social']}\nCNPJ: {doc['cnpj']}\nRepresentante: {doc['representante']}\nTelefone: {doc['telefone']}\n")

    def consultarFornecedores(self, cnpj): #função que busca um fornecedor especifico.
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'cnpj':cnpj})
        if doc is None:
            print('Fornecedor não encontrado.')
        else:
            print(f"Razão Social: {doc['razao_social']}\nCNPJ: {doc['cnpj']}\nRepresentante: {doc['representante']}\nTelefone: {doc['telefone']}\n")

    def atualizarFornecedor(self, cnpj, dado, valor): #função de atualização de informações dos fornecedores cadastrados.
        fornecedor = banco.fornecedores
        doc = fornecedor.find_one({'cnpj': cnpj})
        if doc is None:
            print('Fornecedor não encontrado.')
        else:
            fornecedor.update_one({'cnpj': cnpj},{
                "$set": {
                    f'{dado}': valor
                }
            })

    def removerFornecedor(self, cnpj): #função de remoção do documento fornecedor da collection.
        fornecedor = banco.fornecedores
        doc = fornecedor.find_one({'cnpj': cnpj})
        if doc is None:
            print('Fornecedor não encontrado.')
        else:
            fornecedor.delete_one(doc)
            print('Fornecedor removido com sucesso.')

    def referenciador(self, codigoCNPJ): #função que referência o documento do fornecedor na hora da inserir
        # um documento vento na collection de venda.
        fornecedores = banco.fornecedores
        doc = fornecedores.find_one({'cnpj': codigoCNPJ})
        print('Buscando fornecedor')
        time.sleep(1)
        if (doc is None):
            print('CNPJ não encontrado.')
        else:
            print('Fornecedor encontrado.')
            time.sleep(1)
            return doc

