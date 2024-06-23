from pydantic import BaseModel, Field
from typing import Optional

from . import BaseLogged


class SchoolSchema(BaseLogged):
    id_school: Optional[int] = Field(None)
    name_of_school: str = Field(None)

    post_code: int = Field(None)
    street_name: str = Field(None)
    street_number: int = Field(None)

    class Config:
        orm_mode = True


class _UserBase(BaseModel):
    id_user: Optional[int] = Field(None)
    email: str


class UserPasswords(_UserBase):
    hashed_password: str
    repeat_password: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class UserRest(_UserBase, BaseLogged):
    email: Optional[str] = Field(None)
    hashed_password: Optional[str] = Field(None)
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class Intendant(BaseLogged):
    id_user: Optional[int] = Field(None)
    id_school: Optional[int] = Field(None)
