"""
Modulo responsável pelo CRUD da classe produto,
referenciando forncedor.
"""
import time
#importação do client do mongoDB
from pymongo import MongoClient
from classesMongo.Fornecedor import Fornecedores

bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

class Produtos(object):

    def inserir(self, cnpjFornecedor):

        trazerFornecedor = Fornecedores()

        produto = {
            'categoria': self.categoria,
            'nome': self.nome,
            'codigo': self.codigo,
            'preco': self.preco,
            'fornecedor': trazerFornecedor.referenciador(codigoCNPJ=cnpjFornecedor)
        }
        produtos = banco.produtos
        produtos.insert_one(produto)
        # time.sleep(1)
        print('Produto inserido com sucesso...')

    def buscarProduto(self, refCodigo):
        produtos = banco.produtos
        doc = produtos.find_one({'codigo': refCodigo})
        print('Buscando produto')
        # time.sleep(1)
        if (doc is None):
            print('Produto não encontrado.')
        else:
            print('Produto encontrado.')
            # time.sleep(1)
            return doc