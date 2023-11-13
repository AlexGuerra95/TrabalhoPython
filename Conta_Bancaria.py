import Cliente

class conta_bancaria:
    def __init__(self,numero_conta, tipo_conta, saldo, client ):
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta
        self.client = client
        self.saldo = 00.00

    def deposito(self, numero_conta, tipo_conta, saldo, client, valor):
        self.saldo += valor
        return f'Depósito de {valor} realizado. Novo saldo: {self.saldo}'

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f'Saque de {valor} realizado. Novo saldo: {self.saldo}'
        else:
            return f'Saldo insuficiente para realizar saque.'

    def transferencia(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            return f'Transferência de {valor} efetuada com sucesso para {destino.numero_conta}. Novo saldo {self.saldo}!'
        else:
            return f'Saldo insuficiente para realizar transferência.'
    def verificar_saldo(self):
        return f'Saldo disponível {self.saldo}'
