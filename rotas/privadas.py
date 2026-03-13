from fastapi import APIRouter, Depends
from services.token_JWS import valida_token

rotas_privadas = APIRouter(
    prefix="/privado",
    tags=["privado"],
    dependencies=[Depends(valida_token)]  
)

@rotas_privadas.get("/status")
def status_privado():
    return {"mensagem": "Você está autenticado"}