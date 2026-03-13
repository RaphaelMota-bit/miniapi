from fastapi import HTTPException, BackgroundTasks, APIRouter
from modelos.schemas import RegisterRequest, DeleteUser
from services.auth import registrar_user, login, delete
from services.email_service import enviar_email
from services.token_JWS import gerar_token


rotas = APIRouter(
    prefix="",
    tags=["publicas"],
)


@rotas.get("/")
def home():
    return {"mensagem": "Servidor ok"}


@rotas.post("/registrar")
def registrar(dados: RegisterRequest):
    resultado = registrar_user(dados.email, dados.senha)

    if resultado:
        return {"mensagem": "usuario criado com sucesso"}
    else:
        raise HTTPException(status_code=409, detail="Usuário já existe")


@rotas.post("/login")
async def login_usuario(dados: RegisterRequest, background_tasks: BackgroundTasks):
    user_data = login(dados.email, dados.senha)

    if user_data:
        id = user_data["id"]
        token = gerar_token(id)
        background_tasks.add_task(
            enviar_email,
            user_data["email"],
            assunto="Token de autenficação",
            mensagem= token ,  # pyright: ignore[reportArgumentType]
        )

        return {
            "mensagem": "acesso permitido , verifique seu email ",
            "id": user_data["id"],
            "email": user_data["email"],
            "tempo de registro": user_data["tempo"],
        }
    else:
        raise HTTPException(status_code=401, detail="Acesso negado")

@rotas.post("/delete")
def delete_usuario(dados: DeleteUser):
    deletado = delete(dados.email)

    if deletado:
        return {
            "mensagem" : "user deletado, tome cuidado para isso não vazar"
        }
    else:
        raise HTTPException(status_code=500 , detail= "algum red maximo")