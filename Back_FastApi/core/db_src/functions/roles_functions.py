from fastapi import HTTPException
from sqlalchemy.orm import Session as _Session

from core.db_src.db_models import UserModel, IntendantModel, SchoolModel
from core.db_src.services.intendant_services import get_current_intendant_worker


async def check_if_intendant_is_main_admin(token: str, db: _Session) -> bool:
    """
    Checks if token of logged user is assigned to school admin
    :param token: JWT Token
    :param db: Session of DB
    :return: boolean, True if is main admin, false if not
    """
    try:
        user, intendant, school = await get_current_intendant_worker(token, db)
    except:
        raise HTTPException(status_code=400, detail="Token not exists or intendant is not school admin")

    if not intendant.is_main_admin:
        return False
    return True


async def get_intendant_data(token: str, db: _Session) -> tuple[UserModel, IntendantModel, SchoolModel] | bool:
    """
    Gets data about intendant and its school
    :param token: JWT Token
    :param db: Session of DB
    :return: data from DB about intendant and school or False if no data matched
    """
    try:
        user, intendant, school = await get_current_intendant_worker(token, db)
    except:
        raise HTTPException(status_code=400, detail="Token not exists or intendant is not forking for this school")

    if not intendant or not school:
        return False
    return user, intendant, school
