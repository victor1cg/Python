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

print(bd.dados)
        
# 