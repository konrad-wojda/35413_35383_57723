from sqlalchemy.orm import Session as _Session

from core.db_src.db_models import  MealTypeModel


async def get_meal_types(db: _Session) -> list[dict]:
    """
    Gets attendance list for given day
    :param db: Session of DB
    :return: list of attendances
    """
    meal_types = db.query(MealTypeModel).all()
    result = []
    for meal_type in meal_types:
        meal_type = meal_type.__dict__
        del meal_type['_sa_instance_state']
        result.append(meal_type)

    return result
