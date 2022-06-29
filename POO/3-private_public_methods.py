class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id:nome}       #dict dentro de um dict
        else:
            self.dados['clientes'].update({id:nome})


#Dicionarios:
#dicionario['nome_chave'] = 'valor'

bd = BaseDeDados()
bd.inserir_cliente('01','Luiz')
bd.inserir_cliente('02','Victor')
bd.inserir_cliente('03','Apple')

# print(bd.dados)
        
#-------- HERANÇA --------# - CANAL PYTHONANDO
'''Podemos utilizar atributos e metodos de uma classe em outra.
   No caso secretaria e vendedor são pessoas, mas possuem diferentes cargos.'''

class Pessoa():
    def __init__(self,nome,idade,cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

'''Quando instanciamos um objeto, ele primeiro procura o __init__ da classe filho, depois do pai'''
class Secretaria (Pessoa):
    def __init__(self,nome,idade,cidade,email):
        super().__init__(nome,idade,cidade)             #Com o super podemos acessar os dados da classe pai
        self.cargo = 'Secretária'
        self.email = email
        print(f'\n{self.nome}\n{self.idade}\n{self.cidade}\n{self.email}\n')


class Vendedor (Pessoa):
    def __init__(self,nome,idade,cidade,total_vendas):
        super().__init__(nome,idade,cidade)             #Com o super podemos acessar os dados da classe pai
        self.cargo = 'Vendedor'
        total_vendas += 10 
        self.total_vendas = total_vendas 
        print(self.nome,self.idade,self.cidade,self.total_vendas)

f1 = Secretaria('Maria',30,'SP','maria@hotmail.com')

f2 = Vendedor('Jose',45,'PG',15)

print(f1)
print(f2)