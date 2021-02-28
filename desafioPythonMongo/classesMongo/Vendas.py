"""
Modulo responsável pelo CRUD da classe  Vendas,
referenciando forncedor.
Compreendi que venda não se atualiza, se estiver errado alguma coisa,
exclui e cadastra novamente.
"""
import time
from pymongo import MongoClient
from classesMongo.Produto import Produtos
from classesMongo.Cliente import Clientes


bdCliente = MongoClient("mongodb://localhost:27017") #criando conexão com o banco local.
banco = bdCliente['MongoVendas'] #referenciação ao banco.

class Vendas(object):

    def cadastrarVenda(self, codigoProd, cpf): #função de persistencia do documento venda na collection.

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

    def listarVendas(self): #função de listar todas as vendas.
        vendas = banco.vendas
        for doc in vendas.find():
            print(f"Cod Venda: {doc['codVenda']}Data:{doc['data']}\nHora:{doc['hora']}\n"
                  f"Cod Produto:{doc['produto_venda']['codigo']}\nProduto:{doc['produto_venda']['nome']}\nPreço:{doc['produto_venda']['preco']}\n"
                  f"Nome Cliente:{doc['cliente_venda']['Nome']}\nCPF Cliente:{doc['cliente_venda']['cpf']}\n")

    def pesquisarVenda(self, codVenda): #função de pesquisar venda especifica.
        vendas = banco.vendas
        doc = vendas.find_one(codVenda)
        if doc is None:
            print('Venda não encontrada.')
        else:
            print(f"Cod Venda: {doc['codVenda']}Data:{doc['data']}\nHora:{doc['hora']}\n"
                  f"Cod Produto:{doc['produto_venda']['codigo']}\nProduto:{doc['produto_venda']['nome']}\nPreço:{doc['produto_venda']['preco']}\n"
                  f"Nome Cliente:{doc['cliente_venda']['Nome']}\nCPF Cliente:{doc['cliente_venda']['cpf']}\n")

    def removerVenda(self, codVenda): #função de remover venda.
        vendas = banco.vendas
        doc = vendas.find_one(codVenda)
        if doc is None:
            print('Venda não encontrada.')
        else:
            vendas.delete_one(codVenda)
            print('Venda excluida com sucesso.')


