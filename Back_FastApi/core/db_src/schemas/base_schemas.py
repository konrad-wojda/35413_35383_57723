from pydantic import BaseModel


class BaseLogged(BaseModel):
    token: str

    class Config:
        orm_mode = True
