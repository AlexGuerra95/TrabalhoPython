import os

import cliente
import produto
import venda


def menu():
    os.system('cls')
    print("1 para cadastrar cliente")
    print("2 para alterar   cliente")
    print("3 para remover   cliente")
    print("4 para cadastrar produto")
    print("5 para alterar   produto")
    print("6 para remover   produto")
    print("7 para cadastrar venda")
    print("8 para remover   venda")
    print("9 para alterar   venda")
    print("10 imprimir clientes")
    print("11 imprimir produtos")
    print("12 imprimir vendas")
    print("0 Sair")


if __name__ == '__main__':
    lista_cliente = cliente.Clientes()
    lista_produto = produto.Produtos()
    lista_venda = venda.Vendas()

    sistema = True
    while sistema:
        menu()
        try:
            opcao = int(input("Digite a opcão: "))
            match opcao:
                case 1:
                    lista_cliente.insert()
                case 2:
                    index, client = lista_cliente.buscar_por_nome()
                    if client is None:
                        print("Cliente Invalido!")
                    else:
                        lista_cliente.update(client, index)
                case 3:
                    _, client = lista_cliente.buscar_por_nome()
                    if client is None:
                        print("Cliente Invalido!")
                    else:
                        lista_cliente.rem_client(client)
                case 4:
                    lista_produto.insert()
                case 5:
                    posicao, prod = lista_produto.buscar_por_nome()
                    if prod is None:
                        print("Produto Invalido!")
                    else:
                        lista_produto.update(prod, posicao)
                case 6:
                    _, prod = lista_produto.buscar_por_nome()
                    if prod is None:
                        print("Produto Invalido!")
                    else:
                        lista_produto.rem_produto(prod)
                case 7:
                    lista_venda.insert(lista_cliente, lista_produto)
                case 8:
                    lista_venda.update()
                case 9:
                    lista_venda.rem_mov_pos()
                case 10:
                    lista_cliente.print_clients()
                case 11:
                    lista_produto.print_produtos()
                case 12:
                    lista_venda.print_mov()
                case 0:
                    sai_sys = input("Deseja sair (S)im/(N)ao: ").upper()
                    if sai_sys in ['SIM', 'S']:
                        break
        except ValueError:
            print("Opção invalida")
