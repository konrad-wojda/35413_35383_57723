import datetime

from pydantic import BaseModel, Field
from typing import Optional, Literal


class _TransactionBase(BaseModel):
    id_transaction: Optional[int] = Field(None)


class IntendantLogged(_TransactionBase):
    id_student: int = Field(None)
    id_meal_type: int = Field(None)
    date: datetime.datetime = Field(None)
