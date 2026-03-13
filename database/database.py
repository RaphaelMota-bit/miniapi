import sqlite3

def criar_tabela():
    with sqlite3.connect('banco_de_dados.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(
            '''
            CREATE TABLE if NOT EXISTS usuarios
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            email TEXT NOT NULL UNIQUE ,
            password_hash BLOB NOT NULL ,
            created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
criar_tabela()

def adicionar_user(email , senha_hash):
    try:
        with sqlite3.connect('banco_de_dados.db') as conexao:
           cursor = conexao.cursor()
           cursor.execute(
               '''
               INSERT into usuarios (email , password_hash)
               VALUES(?,?)
               ''' , (email , senha_hash)
               ) 
           return True
    except sqlite3.IntegrityError:
        return False


def buscar_usuarios(email):
     with sqlite3.connect('banco_de_dados.db') as conexao:
           cursor = conexao.cursor()
           cursor.execute( ' SELECT * FROM usuarios WHERE email = ?' , (email,))
           usuarios = cursor.fetchone()
           return usuarios

def excluir_user(email):
    try:
        with sqlite3.connect('banco_de_dados.db') as conexao:
               cursor = conexao.cursor()
               cursor.execute( ' DELETE  FROM usuarios WHERE email = ?' , (email,))
               return True
    except sqlite3.IntegrityError:
        return False
          

