# SQL - Structured Query Language
#db.sqlite3

import sqlite3

#criar conexão no banco de dados
with sqlite3.connect('artistas.db') as conexao:
    sql = conexao.cursor()
    #rodar comando SQL
    sql.execute('CREATE TABLE banda (nome text, estilo text, membro integer);')
    #inserir dados
    sql.execute('insert into banda(nome, estilo, membros) values ("Banda 1","Rock",3);')

    #usar dados da aplicação em SQL
    nome = input("Nome da banda: ")
    estilo = input("Estilo: ")
    qtd_integrantes = int(input("Quantidade de integrantes: "))

    sql.execute('INSERT INTO banda values (?,?,?)'), [
        nome, estilo, qtd_integrantes]

    #salvar alterações no banco
    conexao.commit()

    bandas = sql.execute("SELECT * FROM banda;")
    for banda in bandas