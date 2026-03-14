import sqlite3

def criar_tabela() -> None:
    with sqlite3.connect('database/banco_de_dados.db') as conexao:
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

def adicionar_user(email: str , senha_hash: bytes) -> bool:
    try:
        with sqlite3.connect('database/banco_de_dados.db') as conexao:
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


def buscar_usuarios(email:str) -> tuple | None:
     with sqlite3.connect('database/banco_de_dados.db') as conexao:
           cursor = conexao.cursor()
           cursor.execute( ' SELECT * FROM usuarios WHERE email = ?' , (email,))
           usuarios = cursor.fetchone()
           return usuarios

def excluir_user(id_user : int) -> bool :
    try:
        with sqlite3.connect('database/banco_de_dados.db') as conexao:
               cursor = conexao.cursor()
               cursor.execute( ' DELETE  FROM usuarios WHERE id = ?' , (id_user,))
               return True
    except sqlite3.IntegrityError:
        return False
          
