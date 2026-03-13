from fastapi import FastAPI
from rotas.publicas import rotas
from rotas.privadas import rotas_privadas
import uvicorn

app = FastAPI()

app.include_router(rotas)
app.include_router(rotas_privadas)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000 )