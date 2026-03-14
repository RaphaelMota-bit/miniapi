from fastapi import APIRouter, Depends , HTTPException
from services.token_JWS import valida_token
from services.auth import delete
from modelos.schemas import DeleteUser

rotas_privadas = APIRouter(
    prefix="/priv",
    tags=["privado"],
    # dependencies=[Depends(valida_token)]  
)

@rotas_privadas.get("/status")
def status_privado(user_id = Depends(valida_token)):

    return {
        "mensagem": "Você está autenticado" ,
        "id" : user_id
            }



@rotas_privadas.post("/delete")
def delete_usuario(dados: DeleteUser, user_id=Depends(valida_token)):
    deletado = delete(dados.id)

    if deletado:
        return {
            "mensagem" : "user deletado, tome cuidado para isso não vazar"
        }
    else:
        raise HTTPException(status_code=500 , detail= "algum red maximo")