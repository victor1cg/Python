
## OS - Operational System
## ARQUIVOS E DIRETORIOS

> dentro do terminal
python
import os
- os.name > nome do sistema operacional | nt - windows
- os.listdir() > lista os arquivos na pasta
- os.sep > separador nativo '\\'
- os.getcwd() > 'C:\\Users\\goncavic01\\.vscode\\github\\Python\\Dev_Aprender\\08_Automacao\\docs'

# juntar caminhos para chegar em um arquivo
- os.path.join(os.getcwd() + os.sep + 'senhas.txt')

# descobrir o atributos de um caminho
caminho = os.path.join(os.getcwd() + os.sep + 'senhas.txt')
print(os.path.dirname(caminho))  > Diretorio
print(os.path.basename(caminho)) > obter o arquivo

# Verificar se existe o caminho
os.path.exists(os.getcwd() + '\\' + 'boleto.pdf')

----------------
## MOBILIDADE ENTRE AS PASTAS
os.chdir("<nome_pasta>")
os.chdir("..") > voltar um diretorio

# CRIAR PASTA E ARQUIVOS
os.mkdir("<nome_pasta>")
os.makedirs("<nome_pasta>" + os.sep() + "<nome_subpasta>")

