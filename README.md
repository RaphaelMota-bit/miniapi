Mini API de autenticação em FastAPI
===================================

Este repositório contém uma **mini API de autenticação** em constante evolução, desenvolvida por **apenas uma pessoa** como projeto de estudo e prática.  
Ela inclui registro de usuários, login com senha hasheada, geração de JWT, rotas públicas/privadas e envio de token por e-mail.

Requisitos
----------

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) instalado globalmente (gerenciador de dependências e ambiente virtual)

Instalação com `uv`
-------------------

Na raiz do projeto:

```bash
# instalar dependências a partir do pyproject.toml / uv.lock
uv sync
```

Execução da API
---------------

Ainda na raiz do projeto:

```bash
# modo desenvolvimento, com reload automático
uv run python main.py
```

Isso irá iniciar a API FastAPI com Uvicorn (definido em `main.py`) e você poderá acessar a documentação interativa em:

- `http://localhost:8000/docs`

Sobre o projeto
---------------

- Projeto pequeno, mas com visão de crescer (mini API "em ascensão").
- Back-end em FastAPI, com:
  - autenticação via JWT;
  - hash de senha com bcrypt;
  - banco de dados SQLite simples;
  - envio de e-mails via API externa.
- Gerenciamento de dependências feito via `pyproject.toml` e `uv.lock` (não é necessário `requirements.txt`).