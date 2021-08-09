'''Encapsulamento é para metodos que não são publicos'''

class BaseDeDados:
    def __init__(self):
        self.dados = {}                                 #dicionario que é o principal da classe é publico
    
    def inserir_clientes (self, id, nome):
        if 'clientes' not in self.dados:                #na primeira vez que rodar, irá criar o dicionario
            self.dados['clientes'] = {id : nome}
        else:
            self.dados['clientes'].update({id: nome})   #na proxima vez que rodar, irá atualizar o dicionario
        
    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items(): #manipulando dicionario
            print(id,nome)
    
    def apaga_cliente(self, id):
        del self.dados['clientes'][id]                  #função de apagar o dado
        
        
bd = BaseDeDados()                                      #instanciar a classe
bd.inserir_clientes(1,'Otavio')
bd.inserir_clientes(2,'Miranda')
bd.inserir_clientes(3,'Rose')
bd.apaga_cliente(1)
bd.lista_clientes() 
