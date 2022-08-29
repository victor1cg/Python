
#! SQL Alchemy - 
#* transformar uma Classe python em uma tabela SQL.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#ENGINE - é como o SQLAlchemy se comunica com o banco de dados.

#Criar uma API Flask
app = Flask(__name__)

#Criar uma instancia SQLAlchemy - key é o acesso de autenticação
app.config['SECRETE_KEY'] = 'FSD2323#$SP'

#CONNECTION STRING - cadeia de conexão para um banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

#instanciar e tipando como SQLAlchemy
db = SQLAlchemy(app)
db:SQLAlchemy

#Definir uma estrutura da tabela de postagem
# db.Model estamos instanciando, permite criar tabelas sem utilizar o SQL
class Postagem(db.Model):           #consigor herdar as classes do db.Model
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

#Definir a estrutura da tabela autor
class Autor(db.Model) :
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')


#Criar usuarios administradores

def inicializar_banco():
    db.drop_all()
    db.create_all()
    autor = Autor(nome = 'jow',email = 'jow@gmail.com',senha = '1234',admin = True)
    db.session.add(autor)
    db.session.commit()

if __name__ == '__main__':
    inicializar_banco()