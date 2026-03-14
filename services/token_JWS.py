from typing_extensions import runtime
from dotenv import load_dotenv
from jose import jwt, JWTError
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from fastapi import Depends , HTTPException
from datetime import datetime, timedelta, timezone
from .auth import hash_senha, verifica_user 
import os

load_dotenv()


chave_secreta = os.getenv("JWT_Secreto")
algoritmo = os.getenv("Algoritmo_JWT")
tempo_de_expiracao_minutos = 60


tira_header = HTTPBearer()



def gerar_token(user_id):
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=tempo_de_expiracao_minutos)

    payload = {
        "sub" : str(user_id),
        "exp" : int(expiracao.timestamp())
    }
    if chave_secreta:
        token_pronto = jwt.encode(
            payload ,
            chave_secreta ,
            algorithm= algoritmo  # pyright: ignore[reportArgumentType]
        )
        return token_pronto
    else:
        RuntimeError("JWT NÃO CONFIGURADO")



def decodifica_token(token):
    try:
        payload = jwt.decode(
        token ,
        chave_secreta ,   # pyright: ignore[reportArgumentType]
        algorithms=[algoritmo]   # pyright: ignore[reportArgumentType]
        )
        # puxar o sub do payload, id_usuario = payload.get("sub")
        id_usuario = payload.get("sub") 

        if id_usuario is None:
            return None

        return int(id_usuario)

    except JWTError:
        return None


def valida_token(credenciais : HTTPAuthorizationCredentials = Depends(tira_header)):
    token = credenciais.credentials
    user_info_id = decodifica_token(token)

    if user_info_id is None:
        raise HTTPException (401 , "Token inválido")
        
    return int(user_info_id)




if __name__ == "__main__":
    print("iniciando teste...")
    
    user_data = verifica_user("raphaelcatanduba7115@gmail.com" , "1234")

    # print(user_data)
    if user_data:
        token = gerar_token(user_data["id"])
        print(token)
        token_decodificado = decodifica_token(token)
        print(token_decodificado)
    else:
        print("user_data deu red")
