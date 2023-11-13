from unittest import case

from Cliente import Client, Clients
from Conta_Bancaria import conta_bancaria
from Funcionario import funcionario
import random
from venv.Lib import interface

def saudacao():
    print('Seja bem-vindo(a)!')

    while True:
        dado = menu(['Cliente','Funcionário','Sair'])
    match dado:
    case 1:
        print('Opção 1')
    case 2:
        print('Opção 2')
    case 3:
        print('Saindo...')
        break
    case _:
        print('\033[31mDigite uma opção válida\033[m')


    if __name__ == '__main__':
    lista_cliente = client.Clients()

#Menu dos clientes

def saudacao():
    print('Seja bem-vindo(a)!')

    while True:
        dado = menu(['Criar Conta','Depositar Dinheiro', 'Sacar Dinheiro', 'Transferir dinheiro', 'Verificar Saldo', 'Sair'])
    match dado:
    case 1:
      print('Opção 1')
    case 2:
      print('Opção 2')
    case 3:
      print('Opçaõ 3')
    case 4:
      print('Opção 4')
    case 5:
      print('Opção 5')
    case 6:
      print('Saindo')
      break
    case _:
      print('\033[31mDigite uma opção válida\033[m')

    if __name__ == '__main__':
        lista_cliente = client.Clients()
    if __name__ == '__main__':
        lista_conta_bancaria = conta.Contas()
    if __name__ == '__main__':
        lista_random = random()

#Menu dos funcionários

    while True:
        dado = menu(['Cadastrar Cliente','Editar Informações','Criar Conta para o Cliente', 'Realizar Transações','Sair'])
    match dado:
    case 1:
        print('Opção 1')
    case 2:
      print('Opção 2')
    case 3:
      print('Opçaõ 3')
    case 4:
      print('Opção 4')
    case 5:
      print('Saindo...')
      break
    case _:
      print('\033[31mDigite uma opção válida!\033[m')


    if __name__ == '__main__':
        lista_cliente = client.Clients()
    if __name__ == '__main__':
        lista_conta_bancaria = conta.Contas()
    if __name__ == '__main__':
        lista_random = random()

