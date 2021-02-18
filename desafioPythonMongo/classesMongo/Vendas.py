"""
Modulo responsável pelo CRUD da classe  Vendas,
referenciando forncedor.
"""
import time
import datetime
from pymongo import MongoClient
from classesMongo.Produto import Produtos
from classesMongo.Cliente import Clientes
from classesUtilidades.Util import data, numeroRandom

bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

class Vendas(object):

    def cadastrarVenda(self, codigoProd, cpf):

        trazerClientes = Clientes()
        trazerProdutos = Produtos()

        venda = {
            'data': self.data,
            'hora': self.hora,
            'produto_venda': trazerProdutos.buscarProduto(codigoProd),
            'cliente_venda': trazerClientes.buscarCliente(cpf)
        }

        vendas = banco.vendas
        vendas.insert_one(venda)
        # time.sleep(1)
        print('Venda cadastrada no sistema.')


