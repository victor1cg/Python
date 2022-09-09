# SQL - Structured Query Language
#db.sqlite3

import sqlite3

#criar conexão no banco de dados
with sqlite3.connect('artistas.db') as conexao:
    sql = conexao.cursor()

    #Check se a tabela existe no banco. fetchall cria uma lista com todas as tabelas.
    listofTables = sql.execute(
        ''' SELECT name FROM sqlite_master 
            WHERE type = 'table' 
            ORDER BY NAME;
        '''
        ).fetchall()
    
    if listofTables == []:
        #rodar comando SQL
        sql.execute('CREATE TABLE banda (nome text, estilo text, membros integer);')
        #inserir dados
        sql.execute('INSERT INTO banda(nome, estilo, membros) values ("Banda 1","Rock",3);')

    #usar dados da aplicação em SQL
    nome = input("Nome da banda: ")
    estilo = input("Estilo: ")
    qtd_integrantes = int(input("Quantidade de integrantes: "))

    sql.execute('''INSERT INTO banda values (?,?,?)''',\
        [nome, estilo, qtd_integrantes])

    #salvar alterações no banco
    conexao.commit()

    bandas = sql.execute("SELECT * FROM banda;")
    for banda in bandas:
        print(banda)
