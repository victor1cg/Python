'''
Metodos acessos a Campos - o objetivo principal de usar getters e setters em 
programas orientados a objetos é garantir o encapsulamento de dados.
Adicionar lógica de validação em torno de obter e definir um valor.
'''

class Teste():
    def __init__(self,valor):
        self.valor = valor

    def get_valor(self):
        return self.valor
    
    def set_valor(self,v):
        self.valor = v

obj = Teste(15)

#print('\nO valor de input é:', obj.get_valor())   #jeito 1
#print('O valor de input é:', obj.valor)         #jeito 2

obj.set_valor(22)
#print('\nO valor de input é:', obj.get_valor())

## ---- Otavio Miranda ----##

class Produto():
    def __init__(self, nome, preco):
        self.n = nome
        self.p = preco
    
    def desconto(self,valor):
        self.p = self.p - (self.p*(valor/100))

    #--Preco
    #Getter                             #Getter vai pegar esse valor, e depois vamos settar ele abaixo.
    @property                           #@property é um dos decoradores embutidos.
    def p(self):                        #realizo um metodo pro atributo p (preco)
        return self._p                  #diferenciar p e _p para evitar cair no loop              
    
    @p.setter                           #aqui é setado o valor de p
    def p(self,valor):
        if isinstance(valor,str):       #verificar o tipo do input recebido
            valor = float(valor.replace('R$',''))
        self._p = valor                 #vantagem que não mexe na estrutura main, so add mais codigo.

    #--Nome
    @property
    def n(self):
        return self._n
    
    @n.setter
    def n(self,valor):
        self._n = valor.title()
        
p1 = Produto('camiseta','R$50')
p1.desconto(10)
print('\n',p1.n.capitalize(),' -- R$:',p1.p)

p2 = Produto('CANECA','30')
p2.desconto(50)
print('\n',p2.n.capitalize(),' -- R$:',p2.p)
#SET E GET - Caso alguem coloque o preço como str R$15
#p2 = Produto('caneca','R$15')

print(n.valor)
