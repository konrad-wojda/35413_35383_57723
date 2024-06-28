from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as _Session

from core.db_src.services import meal_services as services
from core.db_src.database import get_db


router_meal_types = APIRouter(
    prefix="/api/meals",
    tags=["Meals"],
    responses={404: {"description": "Not found"}},
)


@router_meal_types.get("/get")
async def get_meal_types(db: _Session = Depends(get_db)) -> callable:
    return await services.get_meal_types(db)