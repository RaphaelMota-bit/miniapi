import bcrypt
from database.database import adicionar_user , buscar_usuarios , excluir_user

def hash_senha(senha: str) -> bytes :
    return bcrypt.hashpw(senha.encode() , bcrypt.gensalt())


def registrar_user(email: str , senha: str) -> bool:
        senha_hash = hash_senha(senha)
        return adicionar_user(email , senha_hash)
        

def comparar_senha(senha: str ,senha_hash: bytes) -> bool:
    return bcrypt.checkpw(senha.encode() , senha_hash ) 

def verifica_user(email: str , senha: str):
     user = buscar_usuarios(email)
     if not user:
          return None
     senha_hash : bytes = user[2]
     
     if comparar_senha(senha, senha_hash):
          return {
               "id" : user[0],
               "email" : user[1] ,
               "tempo" : user[3]
          }
     else:
          return False

     
def delete(id):
     user_chato = excluir_user(id)
     if user_chato:
          return True
     else:
          return False


if __name__ == "__main__":
    # código só de teste desse arquivo
    print(hash_senha("fael"))
    print("Rodando teste rápido de auth...")