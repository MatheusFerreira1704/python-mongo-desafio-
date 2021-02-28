"""
Modulo responsável pelo CRUD da classe  Vendas,
referenciando forncedor.
"""
import time
from pymongo import MongoClient
from classesMongo.Produto import Produtos
from classesMongo.Cliente import Clientes


bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

class Vendas(object):

    def cadastrarVenda(self, codigoProd, cpf):

        trazerClientes = Clientes() #instancia criada para buscar documento do cliente.
        trazerProdutos = Produtos() #instancia criada para buscar documento do produto.

        venda = {
            'data': self.data,
            'hora': self.hora,
            'produto_venda': trazerProdutos.buscarProduto(codigoProd),#refernecia ao documento do produto
            'cliente_venda': trazerClientes.buscarCliente(cpf) #referencia ao documento do cliente.
        }

        vendas = banco.vendas
        vendas.insert_one(venda)
        time.sleep(1)
        print('Venda cadastrada no sistema.')


