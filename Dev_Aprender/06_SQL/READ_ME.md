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

postagens = [
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