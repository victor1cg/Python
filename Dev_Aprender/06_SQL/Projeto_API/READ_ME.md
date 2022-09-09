## Nossa Estrutura para CRUD com API e SQLite
# Aula 15

# schema_db_02 - Utilizando SQL Alchemy conseguimos criar as tabelas 
1. Classe que representa uma postagem no nosso blog (DB)
2. Classe que representa um autor no nosso blog (DB)

# app_01 - Criar os endereços das APIs
3. API para criar novas postagens (app)
4. API para criar novos autores (app)
5. Add o banco de dados para cada chamado de Postagem e Autor
6. Add autenticação a nossas APIs - Deixa API segura com token de autenticação;

Fluxo: 
1) Realizar o Login e copiar o token; 
2) Com o token poder ter acesso as duas tabelas : autor e postagem
Fazemos isso criando um decorator e acoplando em todas as funções;
> from functools import wraps

Deploy Heroku:
1. Indicar no Heroku qual o repositorio do github;
2. Criar um ambiente virtual: 
> python -m venv heroku-api 
> .\heroku-api\Scripts\activate
> pip install flask pyjwt flask_sqlalchemy 
> pip install gunicorn (servidor mais potente)
3. Criar um arquivo Procfile (colocar os comandos):
dentro do arquivo:
> python schema_db_02.py
> web: gunicorn
> app: app
4.Requirements:
> pip freeze > requirements.txt
5. Incluir no gitignore o venv:
> heroku-api/


> postagens = [
    {
        "titulo":"Minha historia",
        "autor":"Amanda Dias"
    },
    {
        "titulo":"Novo dispositivo Sony",
        "autor":"Howard Stringer"
    },
    {
        "titulo":"Lancamento do Ano",
        "autor":"Jeff Bezos"
    }
]  