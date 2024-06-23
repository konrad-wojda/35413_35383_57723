from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as _Session

from core.db_src.services import testing_services as services
from core.db_src.database import get_db


router_testing = APIRouter(
    prefix="/api/testing",
    tags=["Testing"],
    responses={404: {"description": "Not found"}},
)


@router_testing.get("/add_new_student")
async def add_new_student(password: str,
                          db: _Session = Depends(get_db)) -> callable:

    if password != "MakeTesting":
        raise HTTPException(status_code=400, detail="Wrong password.")
    return await services.add_new_student(db)


@router_testing.get("/add_attendance")
async def add_attendance(password: str,
                         db: _Session = Depends(get_db)) -> callable:

    if password != "MakeTesting":
        raise HTTPException(status_code=400, detail="Wrong password.")
    return await services.add_attendance(db)
