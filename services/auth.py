import bcrypt
from database.database import adicionar_user , buscar_usuarios , excluir_user

def hash_senha(senha):
    return bcrypt.hashpw(senha.encode() , bcrypt.gensalt())


def registrar_user(email , senha):
        senha_hash = hash_senha(senha)
        return adicionar_user(email , senha_hash)
        

def verifica_senha(senha ,senha_hash):
    return bcrypt.checkpw(senha.encode() , senha_hash ) 

def login(email , senha):
     user = buscar_usuarios(email)
     if not user:
          return False
     senha_hash = user[2]
     
     if verifica_senha(senha, senha_hash):
          return {
               "id" : user[0],
               "email" : user[1] ,
               "tempo" : user[3]
          }
     else:
          return False

     
def delete(email):
     user_chato = excluir_user(email)
     if user_chato:
          return True
     else:
          return False


if __name__ == "__main__":
    # código só de teste desse arquivo
    print(hash_senha("fael"))
    print("Rodando teste rápido de auth...")