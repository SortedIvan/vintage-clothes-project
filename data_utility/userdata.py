from pydantic import BaseModel

class UserData(BaseModel):
    username: str
    email: str
    password: str

class UserDataLogin(BaseModel):
    email: str
    password: str