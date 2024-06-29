from pydantic import Field, BaseModel

from . import BaseLogged


class StudentSchema(BaseLogged):
    id_school: int = Field(None)
    student_first_name: str = Field(None)
    student_last_name: str = Field(None)
    student_class: str = Field(None)

    class Config:
        orm_mode = True


class GetStudentListSchema(BaseLogged):
    id_school: int


class GetAttendanceListSchema(GetStudentListSchema):
    date: str


class StudentAttendanceSchema(BaseModel):
    id_student: int = Field(None)
    id_meal_type: list[int] = Field(None)


class AddAttendanceListSchema(GetAttendanceListSchema):
    attendance_list: list[StudentAttendanceSchema] = Field(None)
