from pydantic import BaseModel , EmailStr

class RegisterRequest(BaseModel):
    email : EmailStr
    senha : str


class DeleteUser(BaseModel):
    id : int