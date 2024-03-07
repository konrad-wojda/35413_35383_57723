from pydantic import BaseModel, Field
from typing import Optional


class _UserBase(BaseModel):
    user_id: Optional[int] = Field(None)
    email: str


class UserLogged(_UserBase):
    token: str

    class Config:
        orm_mode = True


class UserPasswords(_UserBase):
    hashed_password: Optional[str] = Field(None)
    repeat_password: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class UserEdit(UserLogged):
    email: Optional[str] = Field(None)
    hashed_password: Optional[str] = Field(None)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)

    telephone: Optional[int] = Field(None)
    post_code: Optional[int] = Field(None)
    street_name: Optional[str] = Field(None)
    street_number: Optional[str] = Field(None)
    flat_number: Optional[int] = Field(None)

    class Config:
        orm_mode = True
