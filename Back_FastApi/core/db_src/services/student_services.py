from fastapi import HTTPException
from sqlalchemy import select, func, Text
from sqlalchemy.orm import Session as _Session, aliased

from core.db_src.db_models import UserModel, IntendantModel, SchoolModel, MealTypeModel
from core.db_src.db_models.student_models import StudentModel, AttendanceListModel
import core.db_src.schemas.student_schemas as schemas
from core.db_src.functions.roles_functions import check_if_intendant_is_main_admin, get_intendant_data
from core.db_src.functions.student_functions import format_person


async def create_student(student: schemas.StudentSchema, db: _Session) -> StudentModel | bool:
    """
    Creates new student into DB
    :param student:
    :param db: Session of DB
    :return: False if intendant is not admin; data about student added
    """
    if not await check_if_intendant_is_main_admin(student.token, db):
        return False

    student: dict = {**student.dict()}
    student.pop('token')
    student['student_first_name'] = student['student_first_name'].capitalize()
    student['student_last_name'] = student['student_last_name'].capitalize()
    student_obj = StudentModel(**student)
    db.add(student_obj)
    db.commit()
    db.refresh(student_obj)
    return student_obj


async def create_attendance_list(attendances: schemas.AddAttendanceListSchema, db: _Session) -> bool:
    """
    Saves list of attendances into DB
    :param attendances: schemas.AddAttendanceListSchema
    :param db: Session of DB
    :return: False if intendant is not admin; True if is created
    """
    if not await check_if_intendant_is_main_admin(attendances.token, db):
        return False

    attendances: dict = {**attendances.dict()}
    attendances.pop('token')
    date = attendances['date']
    attendances: list = attendances['attendance_list']
    for student_meals in attendances:
        for meal in student_meals['id_meal_type']:
            attendances_obj = AttendanceListModel(id_student=student_meals['id_student'], id_meal_type=meal, date=date)
            db.add(attendances_obj)

    try:
        db.commit()
    except:
        raise HTTPException(status_code=400, detail="This data is already in DB")

    return True


async def get_attendance_list(attendance: schemas.GetAttendanceListSchema, db: _Session) -> list[dict]:
    """
    Gets attendance list for given day
    :param attendance: schemas.GetAttendanceListSchema
    :param db: Session of DB
    :return: list of attendances
    """
    intendant_data: tuple[UserModel, IntendantModel, SchoolModel] | bool = await get_intendant_data(attendance.token,
                                                                                                    db)
    if not intendant_data:
        raise HTTPException(status_code=400, detail="Intendant not found")

    attendances = db.execute(select(StudentModel.id_student, AttendanceListModel.id_meal_type, AttendanceListModel.date)
                             .join(StudentModel, StudentModel.id_student == AttendanceListModel.id_student)
                             .filter(StudentModel.id_school == attendance.id_school,
                                     AttendanceListModel.date == attendance.date
                                     )
                             )
    result = [dict(zip(['id_student', 'id_meal_type', 'date'], attendance)) for attendance in attendances]
    return result


async def edit_attendance_list(student: schemas.AddAttendanceListSchema, db: _Session) -> StudentModel:
    #  @TODO add this feature later
    pass


async def download_attendance_list(attendance: schemas.GetAttendanceListSchema, db: _Session) -> str:
    """
    Creates CSV text for specific date and school
    :param attendance: schemas.GetAttendanceListSchema
    :param db: Session of DB
    :return: CSV text with attendance list
    """
    intendant_data: tuple[UserModel, IntendantModel, SchoolModel] | bool = await get_intendant_data(attendance.token,
                                                                                                    db)
    if not intendant_data:
        raise HTTPException(status_code=400, detail="Intendant not found")

    from core.db_src.getenv_helper import getenv
    db_type = getenv('DB_TYPE')
    if db_type == 'postgres':
        st = aliased(StudentModel)
        mt = aliased(MealTypeModel)
        al = aliased(AttendanceListModel)

        # Construct the query
        results = db.query(
            st.student_first_name,
            st.student_last_name,
            st.student_class,
            func.string_agg(mt.id_meal_type.cast(Text), ',').label('meal_types')
        ).join(al, al.id_student == st.id_student).join(mt, mt.id_meal_type == al.id_meal_type).filter(
            al.date == attendance.date
        ).filter(
            st.id_school == attendance.id_school
        ).group_by(
            st.student_first_name,
            st.student_last_name,
            st.student_class,
            al.id_student
        )

    else:
        query = (
            select(
                StudentModel.student_first_name,
                StudentModel.student_last_name,
                StudentModel.student_class,
                func.group_concat(MealTypeModel.id_meal_type.distinct()).label("meal_types")
            )
            .filter(StudentModel.id_student == AttendanceListModel.id_student)
            .filter(MealTypeModel.id_meal_type == AttendanceListModel.id_meal_type)
            .filter(AttendanceListModel.date == attendance.date)
            .filter(StudentModel.id_school == attendance.id_school)
            .group_by(AttendanceListModel.id_student)
        )

        results = db.execute(query)
    ids_meal_type = set()
    data_lists = []

    for result in results:
        eaten_mean_types = result.meal_types.split(",")
        data_lists.append([result.student_first_name, result.student_last_name, result.student_class,
                           *eaten_mean_types])
        [ids_meal_type.add(eaten_mean_type) for eaten_mean_type in eaten_mean_types]

    meal_types = dict(db.query(MealTypeModel.id_meal_type, MealTypeModel.type).
                      filter(MealTypeModel.id_meal_type.in_(ids_meal_type)).all())

    result_headers = ["Imię", "Nazwisko", "Klasa"]
    result_headers.extend(meal_types.values())

    csv_header: str = ';'.join(result_headers)+'\n'
    csv_output: str = csv_header + '\n'.join(format_person(person, meal_types) for person in data_lists)

    return csv_output

