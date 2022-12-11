""" Aqui iremos trazer para o contexto, ou seja, quando meu modulo inicia devo trazer
a tabela user para o contexto.
"""

from sqlmodel import SQLModel
from .user import User          #importando modulo da mesma raiz.

__all__=  ["SQLModel","User"]   #objetos publicos


