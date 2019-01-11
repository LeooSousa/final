import sqlite3

BD = "base.db"


def add_compra(Data):
    '''Adciona uma compra'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " INSERT INTO Compras ( Data, Total) VALUES ( '%s', '%d' )" % (Data, 0)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print("Lista de compra", Data, "Criada")
    else:
        conexao.rollback()
        print("Nao foi possivel  criar a lista")
        cursor.close()
        conexao.close()


def get_total(Id_compra):
    '''Calcula o total da compra'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT Total FROM Compras WHERE Id_compra= '%d'" % Id_compra
    cursor.execute(sql)
    total = cursor.fetchone()
    if total:
        return total[0]



def exibir_listas():
    '''Exibi as listas'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = " SELECT * FROM Compras"
    cursor.execute(sql)
    compras = cursor.fetchall()
    if compras:
        for compra in compras:
            print("Id compra: ", compra[0], " - Data da compra: ", compra[1], " - Total da compra: ", compra[2])
    else:
        print("Nao foi possivel  criar a lista")
        cursor.close()
        conexao.close()


def listar_produtos(Id_compra):
    '''Listar todos os produtos de uma compra'''
    conexao = sqlite3.connect(BD)  # sempre preciso criar conexao com o banco
    sql = "SELECT * FROM Produto where Id_compra == '%s'" % Id_compra
    cursor = conexao.cursor()  # pego os codigos roda no bd
    cursor.execute(sql)
    Produtos = cursor.fetchall()  # seleciona tudo ta tabela
    if Produtos.__len__() > 0:
        for Produto in Produtos:
            print("Id_produto: ", Produto[0], ' - Descrição:', Produto[1], " - Quantidade: ", Produto[2],
                  " - Valor_unitario: ", Produto[3])
    else:
        print("Nenhum produto cadastrado!")
    cursor.close()
    conexao.close()


def atualiza_total(Id_compra, Valor):
    '''Atualiza o total'''
    total = get_total(Id_compra) + Valor
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "UPDATE Compras SET Total= '%d' WHERE Id_compra = '%d'" %(total, Id_compra)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        return True
    else:
        conexao.rollback()
    cursor.close()
    conexao.close()


def inserir_produto_lista(Descricao, Quantidade, Valor_unitario, Id_compra):
    '''Inserir um produto em uma lista de compra'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = ("INSERT INTO Produto (Descricao, Quantidade, Valor_unitario, Id_compra) VALUES ('%s', '%d', '%s', '%d')"
           % (Descricao, Quantidade, Valor_unitario, Id_compra))
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        atualiza_total(Id_compra, Valor_unitario * Quantidade)
        print("Produto", Descricao, "cadastrado")
    else:
        conexao.rollback()
        print("Nao foi possivel cadastrar o produto")
    cursor.close()
    conexao.close()


def buscar_por_id(Id_produto,Id_compra):
    '''Buscar produto por id'''
    conexao = sqlite3.connect(BD)  # sempre preciso criar conexao com o banco
    cursor = conexao.cursor()  # pego os codigos roda no bd
    sql = "SELECT * FROM Produto WHERE Id_produto='%d' and Id_compra == '%s'" % (Id_produto, Id_compra)
    cursor.execute(sql)
    Produto = cursor.fetchone()
    if Produto:
        print("Id_produto: ", Produto[0], ' - Descrição:', Produto[1], " - Quantidade: ", Produto[2],
              " - Valor_unitario: ", Produto[3])
        return True
    else:
        print("Nenhum produto cadastrado!")

    cursor.close()
    conexao.close()


def excluir_produto_p_id(Id_produto, Id_compra):
    '''Excluir produto por id'''
    if buscar_por_id(Id_produto, Id_compra):
        resposta = input("Deseja realmente excluir esse produto?").lower()
        if resposta == 's':
            conexao = sqlite3.connect(BD)
            cursor = conexao.cursor()
            sql = "DELETE FROM Produto WHERE Id_produto='%d' and Id_compra == '%s'" % (Id_produto, Id_compra)
            cursor.execute(sql)
            if cursor.rowcount == 1:
                conexao.commit()
                print('Produto deletado!')
            else:
                conexao.rollback()
                print("Nao foi possivel deletar produto")
            cursor.close()
            conexao.close()



def alterar_preco(Id_produto, Id_compra,Valor_unitario):
    '''Alterar preço'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "UPDATE Produto SET Valor_unitario='%f' WHERE Id_produto='%d' and Id_compra == '%d'" % (Valor_unitario, Id_produto, Id_compra)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        atualiza_total(Id_compra,Valor_unitario)
        print('Produto alterado!')
    else:
        conexao.rollback()
        print('Não foi possível alterar produto')
    cursor.close()
    conexao.close()



def alterar_descricao(descricao,Id_produto,Id_compra):
    '''Alterar descrição'''
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "UPDATE Produto SET Descricao='%s' WHERE Id_produto= '%d' and Id_compra == '%d'" % (
        descricao, Id_produto,Id_compra)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        conexao.commit()
        print('Produto alterado!')
    else:
        conexao.rollback()
        print('Não foi possível alterar produto')
    cursor.close()
    conexao.close()



def buscar_por_descricao(Id_compra,Descricao):
    '''Buscar por descrição'''
    Descricao = Descricao + '%'
    conexao = sqlite3.connect(BD)
    cursor = conexao.cursor()
    sql = "SELECT * FROM produto WHERE Descricao LIKE '%s' and Id_compra == '%d'" % (Descricao,Id_compra)
    cursor.execute(sql)
    Produtos = cursor.fetchall()
    if Produtos:
        for Produtos in Produtos:
            print("Id_produto: ", Produtos[0], ' - Descrição:', Produtos[1], " - Quantidade: ", Produtos[2],
                  " - Valor_unitario: ", Produtos[3])
        return True
    else:
        print("Nenhum produto encontrado!")
        return False

    cursor.close()
    conexao.close()


