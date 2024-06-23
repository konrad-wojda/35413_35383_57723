import re

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from io import StringIO
from sqlalchemy.orm import Session as _Session


import core.db_src.schemas.student_schemas as schemas
from core.db_src.services import student_services as services
from core.db_src.database import get_db


router_meal_types = APIRouter(
    prefix="/api/attendance-list",
    tags=["Attendance List"],
    responses={404: {"description": "Not found"}},
)


@router_meal_types.get("/get")
async def get_meal_types(form_data: schemas.GetAttendanceListSchema = Depends(),
                              db: _Session = Depends(get_db)) -> callable:
    # return await services.get_attendance_list(form_data, db)
    pass