
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

---------------
## PATHLIB

if __name__ == "__main__":
    
    #CAMINHO DO PROJETO
    caminho_projeto = Path()
    print('caminho\n')
    # print(caminho_projeto.absolute())
    #* C:\Users\vcamargg\Impacta\AULA_05
    
    #CAMINHO DO ARQUIVO
    caminho_arquivo = Path(__file__)
    # print(caminho_arquivo)
    #* c:\Users\vcamargg\Impacta\AULA_05\flights-data-pipeline\src\assets\cleansing.py
    
    #CAMINHO DO PAI DO ARQUIVO
    print()
    # print(caminho_arquivo.parent)
    #* c:\Users\vcamargg\Impacta\AULA_05\flights-data-pipeline\src\assets
    
    #Criando arquivos e caminhos > utilizamos a barra normal / (true div), pois ele automaticamente coloca como barra invertida \ (backslash)
    ideias = caminho_arquivo.parent / 'ideias'
    print(ideias / 'ideias.txt')
    #* c:\Users\vcamargg\Impacta\AULA_05\flights-data-pipeline\src\assets\ideias\ideias.txt
    
    #Criando o arquivo e escrevendo dentro dele
    '''
    caminho_arquivo2 = Path.home() / 'Downloads' /'arquivo_test.txt'
    caminho_arquivo2.touch()                        #salva o arquivo
    
    with open (caminho_arquivo2, 'a+') as file:
        file.write('uma linha \r\n')
        file.write('duas linhas \r\n')
        file.write('tres linhas \r\n')
        
    print(caminho_arquivo2.read_text())
    '''
    #Criando uma pasta nova
    caminho_arquivo3 = Path.home() / 'Downloads'/ 'Teste_Path_lib'
    caminho_arquivo3.mkdir(exist_ok=True) #se existir, não faça nada

