import random

from Cliente import Client
from Conta_Bancaria import conta_bancaria


class funcionario:
    def cadastrar_client(self, nome, endereco, telefone, email):
        client = Client(nome, endereco, telefone, email)
        return client

    def criar_conta(self, client, tipo_conta, saldo_inicial):
        numero_conta = self.gerar_numero_conta()
        conta = conta_bancaria(numero_conta, tipo_conta, saldo_inicial, client)
        return conta
