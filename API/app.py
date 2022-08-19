
#! CRUD completo com Flask e SQLAlchemy
# API REST e BANCO DE DADOS
#https://www.youtube.com/watch?v=WDpPGFkI9UU&ab_channel=ProgramandoComRoger
# https://www.youtube.com/watch?v=kRNXKzfYrPU&ab_channel=PrettyPrinted

#Flask é a propria classe. Response é a resposta. request é quando um cliente manda um body
from datetime import datetime
from flask import Flask, Response, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey  #integration to one or more Flask applications
from sqlalchemy.sql import func
from flask_marshmallow import Marshmallow # object serialization, SCHEMA

import json
#sqlite nao precisa instalar/chamar a biblioteca, padrao no python

app = Flask(__name__)   #Criando a aplicação

#Configurando os parametros do SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #DB - youtube

db = SQLAlchemy(app)
ma = Marshmallow(app)

#* CRUD - Create, Read, Update, Delete;
#* Tabela USUARIO - 
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    # date_created = db.Column(db.DateTime,default = datetime.utcnow)
    date_created = db.Column(db.DateTime(timezone=True),nullable=False, default=func.now())

class Reward(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_reward = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #faz referencia a tabela user
    user = db.relationship('User', backref = 'reward')

#schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
class RewardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reward
        load_instance = True

#Criar a tabela - Porem, toda vez que rodar o codigo ele vai querer criar do zero. 
#Para isso, importamos via terminal.

#* CRIANDO AS FUNÇÕES
@app.route('/')
def index():
    one_user = User.query.first()
    user_schema = UserSchema()
    output = user_schema.dump(one_user) #serialize,gerar objeto in json format
    return jsonify({'user':output})



""" @app.route("/usuarios", methods = ["GET"])
def seleciona_usuarios():
    usuarios_objects = Usuario.query.all()
    # usuarios_json =  
    print (jsonify(usuarios_objects))
    # return jsonify({'usuarios': usuarios_json})
    return
 """
# seleciona_usuarios()
if __name__ == '__main__':
    app.run(port=5000, host='localhost',debug = True)


