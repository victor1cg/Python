
#! CRUD completo com Flask e SQLAlchemy
# API REST e BANCO DE DADOS
#https://www.youtube.com/watch?v=WDpPGFkI9UU&ab_channel=ProgramandoComRoger
# https://www.youtube.com/watch?v=kRNXKzfYrPU&ab_channel=PrettyPrinted

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import join
from sqlalchemy.sql import select
import sqlite3

#Flask é a propria classe. Response é a resposta. request é quando um cliente manda um body
#! 1- Criando a aplicação
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Chico'

#! 2 - Configurando os parametros do SQLAlchemy
# CONNECTION STRING - cadeia de conexão para um banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sold.db'
#Instanciar o SQL
db = SQLAlchemy(app)

#! 3 - Criando as Classes
# Tabela USUARIO -
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    role = db.Column(db.String(50),nullable = False)
    password = db.Column(db.String(50))
    sellout = db.relationship('Sellout')
    #username = db.Column(db.String(80), unique=True, nullable=False)

class Sellout(db.Model):
    __tablename__ = 'sellout'
    id_sale = db.Column(db.Integer, primary_key = True) 
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    name_product = db.Column(db.String(50))
    qty = db.Column(db.Integer)

#! 5 - Definindo Schema
# > Definido no relationship

#Criar a tabela - Porem, toda vez que rodar o codigo ele vai querer criar do zero. 
#Para isso, importamos via terminal.

#! 6 - CRIANDO AS FUNÇÕES
conexao = sqlite3.connect('sold.db')
sql = conexao.cursor()
# results = sql.execute("""SELECT * FROM sellout;""").fetchall()
listofTables = sql.execute(
        ''' SELECT name FROM sqlite_master 
            WHERE type = 'table' 
            ORDER BY NAME;
        '''
        ).fetchall()
print(listofTables)

# for result in results:
#     print(result)

if __name__ == '__main__':
    app.run(debug=True)

