import os
from dotenv import load_dotenv
import httpx

load_dotenv()

API_KEY = os.getenv("CHAVE_API")


SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"
EMAIL_FROM = os.getenv("EMAIL_FROM")

async def enviar_email(destinatario: str, assunto: str, mensagem: str) -> bool:
    if not API_KEY:
        raise RuntimeError("CHAVE_API não encontrada. Verifique seu arquivo .env.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "personalizations": [
            {
                "to": [{"email": destinatario}],
                "subject": assunto,
            }
        ],
        "from": {
            "email": EMAIL_FROM,
        },
        "content": [
            {
                "type": "text/html",
                "value": mensagem,
            }
        ],
    }


    async with httpx.AsyncClient() as client:
        response = await client.post(
            SENDGRID_URL,
            headers=headers,
            json=payload,
        )

    if response.status_code != 202:
        raise RuntimeError(f"Erro ao enviar email: {response.text}")

    return True



