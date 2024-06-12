from pydantic import BaseModel, Field
from typing import Optional, Literal


class _TransactionBase(BaseModel):
    id_transaction: Optional[int] = Field(None)


class IntendantLogged(_TransactionBase):
    pass

    class Config:
        orm_mode = True


TransactionEnum = Literal["output", "input", "event", "return"]
