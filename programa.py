from funcoes import *
from menu import menu


op = 0
while op != 11:
    menu()
    op = int(input("digite uma opção: "))
    if op == 1:
        Data = str(input("comece uma compra informando a data"))
        add_compra(Data)

    if op == 2:
        Descricao = input("Informe o nome do produto:")
        Quantidade = int(input("Informe a quantidade de produtos que irá comprar: "))
        Valor_unitario = int(input("Informe o valor do produto: "))
        Id_compra = int(input("Informe o código da compra: "))

        inserir_produto_lista(Descricao, Quantidade, Valor_unitario, Id_compra)

    if op == 3:
        Id_compra = input("Digite aqui o Id da compra que voce deseja listar:")
        listar_produtos(Id_compra)

    if op == 4:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        buscar_por_id(Id_produto,Id_compra)

    if op == 5:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        excluir_produto_p_id(Id_produto, Id_compra)

    if op == 6:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        Valor_unitario = float(input('Informe o novo preço do produto'))
        alterar_preco(Id_produto, Id_compra,Valor_unitario)

    if op == 7:
        Id_compra = int(input("Informe o Id do compra: "))
        Id_produto = int(input("Informe o Id do produto: "))
        Descricao = input('Informe a nova descrição do produto')
        alterar_descricao(Descricao,Id_produto,Id_compra)

    if op == 8:
        Id_compra = int(input("Informe o Id do compra: "))
        descricao = input("Informe a descrição do produto: ")
        buscar_por_descricao(Id_compra,descricao)

    if op == 9:
        exibir_listas()
        

    if op == 10:
        Id_compra = int(input("informe o ID da compra para ver o total: "))
        print(get_total(Id_compra))
