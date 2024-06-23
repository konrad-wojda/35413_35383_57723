import re

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from io import StringIO
from sqlalchemy.orm import Session as _Session


import core.db_src.schemas.student_schemas as schemas
from core.db_src.services import student_services as services
from core.db_src.database import get_db


router_student = APIRouter(
    prefix="/api/student",
    tags=["Student"],
    responses={404: {"description": "Not found"}},
)


@router_student.post("/add")
async def create_student(form_data: schemas.StudentSchema,
                          db: _Session = Depends(get_db)) -> callable:

    return await services.create_student(form_data, db)


router_attendance_list = APIRouter(
    prefix="/api/attendance-list",
    tags=["Attendance List"],
    responses={404: {"description": "Not found"}},
)


@router_attendance_list.post("/add-single")
async def create_attendance_list(form_data: schemas.AddAttendanceListSchema,
                                 db: _Session = Depends(get_db)) -> callable:
    date_reg_exp = re.compile(r'\d{4,5}-\d{2}-\d{2}')

    if not date_reg_exp.match(form_data.date):
        raise HTTPException(status_code=400, detail="This date is not in format yyyy-mm-dd")

    return await services.create_attendance_list(form_data, db)


@router_attendance_list.get("/get")
async def get_attendance_list(form_data: schemas.GetAttendanceListSchema = Depends(),
                              db: _Session = Depends(get_db)) -> callable:
    return await services.get_attendance_list(form_data, db)


# @router_attendance_list.put("/edit")
# async def edit_attendance_list(form_data: schemas.GetAttendanceListSchema,
# db: _Session = Depends(get_db)) -> Response:
#     pass


@router_attendance_list.get("/get-file")
async def download_attendance_list(form_data: schemas.GetAttendanceListSchema = Depends(),
                                   db: _Session = Depends(get_db)) -> Response:
    """
    Download CSV file with attendance list for day passed from frontend
    :param form_data: schema of GetAttendanceListSchema
    :param db: Session of DB
    :return: CSV file
    """
    date_reg_exp = re.compile(r'\d{4,5}-\d{2}-\d{2}')

    if not date_reg_exp.match(form_data.date):
        raise HTTPException(status_code=400, detail="This date is not in format yyyy-mm-dd")

    await services.download_attendance_list(form_data, db=db)

    csv_buffer = StringIO(await services.download_attendance_list(form_data, db=db))

    # # Create a custom response with UTF-8 encoding
    response = Response(content=csv_buffer.getvalue().encode("utf-8"))
    response.headers["Content-Disposition"] = f"attachment; filename={form_data.date}.csv"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"

    return response
