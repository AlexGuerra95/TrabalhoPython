from datetime import datetime

from Common import Util


class Client:

    def __init__(self, nome: str, endereco: str, telefone: str, email: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.saldo = 0.0
        self.dt_cadastro = datetime.now()
        self.dt_baixa = None

    def __eq__(self, other):
        return(self.nome == other.nome and
               self.endereco == other.endereco and
               self.telefone == other.telefone and
               self.email == other.email)

    def add_saldo(self, saldo):
        self.saldo += saldo

    def sub_saldo(self, saldo):
        self.saldo -= saldo

    def baixa_cad(self, dt_baixa: datetime):
        self.dt_baixa = dt_baixa

class Clients:

    def __init__(self):
        self.list_client ={}

    def add_client(self, client: Client):
        self.list_client.append(client)

    def rem_client(self, client: Client):
        self.list_client.remove(client)

    def up_client(self, client: Client, index: int):
        self.list_client.insert(index, client)

    def print_clients(self):
        print('-----------------------------------------------------------------------')
        for pos, client in enumerate(self.list_client):
            print(pos, client.nome, client.endereco, client.telefone, client.email,
                  client.saldo)
            print('-----------------------------------------------------------------------')
        input("Pressione qualquer tecla para continuar...")

    def buscar_por_nomes(self):
        names_client = [client.nome for client in self.list_client]
        client_name = input(f"Digite o nome do cliente {names_client}: ")
        return Util(self.list_client).search_by_name(client_name)

    def insert(self):
        nome = input('Insira o nome do cliente: ')
        endereco = input('Insira o endereço do cliente: ')
        email = input('Insira o email do cliente: ')
        telefone = input('Insira o telefone do cliente: ')
        saldo = int(input('Insira o saldo do cliente (ex=9999.99): '))
        client = Client(nome, endereco, email, telefone, saldo)
        self.add_client(client)

    def updete(self, client: Client, index: int):
        client.endereco = input('Insira o novo endereço do cliente: ')
        client.telefone = input('Insira o novo telefone do cliente: ')
        client.email = input('Insira o novo email do cliente: ')
        self.up_client(client, index)