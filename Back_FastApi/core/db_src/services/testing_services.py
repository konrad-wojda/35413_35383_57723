from sqlalchemy.orm import Session as _Session
from passlib import hash


from core.db_src.db_models import MealTypeModel, StudentModel, UserModel, IntendantModel, SchoolModel, \
    AttendanceListModel
from core.db_src.services.intendant_services import make_admin


def check_if_empty_db(db: _Session) -> bool:
    """
    Testing purpose - quick setup. Checks if DB is empty
    :return: True if all functions are done
    """
    if db.query(UserModel).filter(UserModel.id_user == 1).first():
        return False


async def add_new_student(db: _Session) -> bool:
    """
    Testing purpose - quick setup. Creates simple setup for testing stuff if there is no user
    :return: True if all functions are done
    """
    check_if_empty_db(db)

    await create_admin(db)
    create_2nd_user(db)
    create_school(db)
    make_2nd_user_intendant(db)
    add_student(db)
    add_meal_type(db)
    return True


async def add_attendance(db: _Session) -> bool:
    """
    Testing purpose - quick setup. Creates simple setup for testing stuff if there is no user
    :return: True if all functions are done
    """
    await add_new_student(db)
    add_attendance_list(db)
    return True


async def create_admin(db: _Session) -> None:
    """
    Testing purpose - quick setup. Create 1st user who is admin
    """
    user_obj = UserModel(
        email="string@com.pl", hashed_password=hash.bcrypt.hash("String123*"),
        is_admin=False, first_name="Konrad", last_name="Wojda"
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    if user_obj.id_user == 1:
        await make_admin(db)


def create_2nd_user(db: _Session) -> None:
    """
    Testing purpose - quick setup. Saves 2nd user in DB
    """
    user_obj = UserModel(
        email="string@com.com", hashed_password=hash.bcrypt.hash("String123*"),
        is_admin=False, first_name="Marta", last_name="Tusia"
    )
    db.add(user_obj)
    db.commit()


def create_school(db: _Session) -> None:
    """
    Testing purpose - quick setup. Saves school in DB
    """
    school_obj = SchoolModel(
                             name_of_school="First School FromBork",
                             post_code="14530",
                             street_name="Ul. Grunwaldzka",
                             street_number="17"
    )
    db.add(school_obj)
    db.commit()


def make_2nd_user_intendant(db: _Session) -> None:
    """
    Testing purpose - quick setup. Adds 2nd user as intendant in DB
    """
    intendant_obj = IntendantModel(is_main_admin=True, id_user=2, id_school=1)
    db.add(intendant_obj)
    db.commit()


def add_student(db: _Session) -> None:
    """
    Testing purpose - quick setup. Saves students in DB
    """
    first_names = ["Adam", "Robert", "Maria", "Anna Maria"]
    last_names = ["Nowak", "Rogacz", "Kot", "Wesołowska"]
    classes = ["1a", "2b", "1b", "2c"]
    for index in range(len(last_names)):
        student_obj = StudentModel(
                                     id_school=1,
                                     student_first_name=first_names[index],
                                     student_last_name=last_names[index],
                                     student_class=classes[index],
        )
        db.add(student_obj)
    db.commit()


def add_meal_type(db: _Session) -> None:
    """
    Testing purpose - quick setup. Saves meal types in DB
    """
    meals = ["Śniadanie", "II Śniadanie", "Obiad", "Kolacja"]
    for meal in meals:
        meal_obj = MealTypeModel(type=meal)
        db.add(meal_obj)
    db.commit()


def add_attendance_list(db: _Session) -> None:
    """
    Testing purpose - quick setup. Saves 12 attendances in DB
    """
    id_students = [1, 2]
    id_meal_types = [[1, 2, 4], [1, 2, 3]]
    dates = '2024-06-18'
    for index in range(len(id_meal_types)):
        for meal_type in id_meal_types[index]:
            attendance_list_obj = AttendanceListModel(
                id_student=id_students[index],
                id_meal_type=meal_type,
                date=dates,
            )
            db.add(attendance_list_obj)

    id_students = [2, 3]
    id_meal_types = [[1, 2, 4], [1, 2, 4]]
    dates = '2024-06-17'
    for index in range(len(id_meal_types)):
        for meal_type in id_meal_types[index]:
            attendance_list_obj = AttendanceListModel(
                id_student=id_students[index],
                id_meal_type=meal_type,
                date=dates,
            )
            db.add(attendance_list_obj)
    db.commit()
