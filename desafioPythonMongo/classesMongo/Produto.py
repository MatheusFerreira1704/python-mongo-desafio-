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

    def inserir(self, cnpjFornecedor): #funcao de persistencia do documento produto na collection produto.

        trazerFornecedor = Fornecedores() #instancia criada para trazer documento do fornecedor

        produto = {
            'categoria': self.categoria,
            'nome': self.nome,
            'codigo': self.codigo,
            'preco': self.preco,
            'fornecedor': trazerFornecedor.referenciador(codigoCNPJ=cnpjFornecedor) #referencia ao documento do fornecedor
        }
        produtos = banco.produtos
        produtos.insert_one(produto)
        time.sleep(1)
        print('Produto inserido com sucesso...')

    def listarProdutos(self): #função de listar produtos cadastrado.
        produtos = banco.produtos
        for doc in produtos.find():

            print(f"Categoria:{doc['categoria']}\nNome:{doc['nome']}\nCódigo:{doc['codigo']}\nPreço:{doc['preco']}\n"
                  f"Nome Fornecedor:{doc['fornecedor']['razao_social']}\n"
                  f"CNPJ Fornecedor:{doc['fornecedor']['cnpj']}"
                  )

    def pesquisarProduto(self, codigo): #função de buscar produto pelo codigo.
        produtos = banco.produtos
        doc = produtos.find_one({'codigo': codigo})
        print('Buscando Produto...')
        time.sleep(1)
        if doc is None:
            print('Produto não encontrado.')
        else:
            print(f"Categoria: {doc['categoria']}\nNome: {doc['nome']}\nCódigo: {doc['codigo']}\nPreço: {doc['preco']}\n"
            f"Nome Fornecedor: {doc['fornecedor']['razao_social']}\n"
            f"CNPJ Fornecedor: {doc['fornecedor']['cnpj']}"
            )

    def atualizarProduto(self, codigo, dado, valor): #função de atualização do documento produto ja cadastrado.
        produtos = banco.produtos
        doc = produtos.find_one({'codigo': codigo})
        if doc is None:
            print('Produto não encontrado. ')
        else:
            produtos.update_one({'codigo': codigo},{
                "$set": {
                    f'{dado}': valor
                }
            })

    def removerProduto(self, codigo): #função de remover produto.
        produtos = banco.produtos
        doc = produtos.find_one({'codigo': codigo})
        if doc is None:
            print(f'Não existe produto cadastrado com esse código: {codigo}. ')
        else:
            produtos.delete_one(doc)
            print('Produto excluido com sucesso...')


    def buscarProduto(self, refCodigo): #função utilizada para referenciar o produto na persistencia do documento venda.
        produtos = banco.produtos
        doc = produtos.find_one({'codigo': refCodigo})
        print('Buscando produto')
        time.sleep(1)
        if (doc is None):
            print('Produto não encontrado.')
        else:
            print('Produto encontrado.')
            time.sleep(1)
            return doc