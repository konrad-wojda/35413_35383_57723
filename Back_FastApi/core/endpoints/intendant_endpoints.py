from typing import Annotated, Type

from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session as _Session

import core.db_src.schemas.intendant_schemas as schemas
from core.db_src.schemas.base_schemas import BaseLogged
from core.db_src.services import intendant_services as services
from core.db_src.functions import intendant_functions as functions
from core.db_src.db_models.intendant_models import UserModel, IntendantModel
from core.db_src.database import get_db
from ..db_src.getenv_helper import getenv_int


router_user = APIRouter(
    prefix="/api/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router_user.post("/login")
async def read_item(form_data: Annotated[schemas.UserPasswords, Depends(oauth2_scheme)],
                    db: _Session = Depends(get_db)) -> callable:
    """
    Uses data passed by user to login him and generate token
    :param form_data: data from user, schema UserPasswords
    :param db:Session of DB
    :return: function generate token
    """
    return await services.generate_token(form_data, db)


@router_user.post("/register")
async def create_user(form_data: schemas.UserPasswords, db: _Session = Depends(get_db)):
    """
    Creates user in DB with data passed by user or raise errors when something is wrong
    :param form_data: schema UserPasswords
    :param db: Session of DB
    :return: object with email of user created and code 200
    """
    form_data.email = form_data.email.lower()

    if not await functions.is_valid_passwords(form_data.hashed_password, form_data.repeat_password):
        raise HTTPException(status_code=400,
                            detail=f"Passwords not match, or at least one is shorter than"
                                   f" {getenv_int('MIN_PASSWORD_LEN')} characters, "
                                   f"password should have small and capital letter with number and special character.")

    if not await functions.is_valid_email(form_data.email):
        raise HTTPException(status_code=400, detail="E-mail is not valid or too long; max "
                                                    f"{getenv_int('MAX_EMAIL_LEN')} characters.")

    if await services.get_user_by_email(form_data.email, db):
        raise HTTPException(status_code=400, detail="Email already in use")

    user = await services.create_user(form_data, db)
    return dict(status_code=200, email=user.email)


@router_user.get("/get")
async def get_user(token: str, db: _Session = Depends(get_db)) -> Type[UserModel]:
    """
    Gets data about user from DB
    :param token: user JWT token
    :param db: Session of DB
    :return: UserModel without password
    """
    user = await services.get_current_user(token, db)
    user.pop('hashed_password')
    return user


@router_user.patch("/edit")
async def edit_user(form_data: schemas.UserRest, db: _Session = Depends(get_db)) -> callable:
    """
    Edits user data in DB
    :param form_data: schema of UserRest
    :param db: Session of DB
    :return: update_user
    """
    if not await functions.is_valid_email(form_data.email) and form_data.email:
        raise HTTPException(status_code=400, detail="E-mail is not valid or too long; max "
                                                    f"{getenv_int('MAX_EMAIL_LEN')} characters")
    if not functions.is_valid_password(form_data.hashed_password):
        raise HTTPException(status_code=400, detail="Password is too weak")

    return await services.update_user(form_data, db)


@router_user.delete("/delete")
async def delete_user(form_data: schemas.UserPasswords, db: _Session = Depends(get_db)):
    """
    Deletes user data from DB
    :param form_data: schema of UserPasswords (for confirmation)
    :param db: Session of DB
    :return: text if correct, raise 404 if error
    """
    if not functions.are_passwords_matched(form_data.hashed_password, form_data.repeat_password):
        raise HTTPException(status_code=400, detail="Passwords not match")
    if not await services.authenticate_user(form_data.email, form_data.hashed_password, db):
        raise HTTPException(status_code=400, detail="User cannot be deleted with this data")

    if not await services.authenticate_user(form_data.email, form_data.hashed_password, db):
        raise HTTPException(status_code=404, detail="User cannot be deleted with this data")

    await services.delete_user(form_data, db)
    return {'status_code': 200, 'text': 'Account got deleted'}


# ----------------------------------------------------------------------------------------------------------------------
router_school = APIRouter(
    prefix="/api/school",
    tags=["School"],
    responses={404: {"description": "Not found"}},
)


@router_school.post("/create")
async def create_school(form_data: schemas.SchoolSchema, db: _Session = Depends(get_db)) -> callable:
    """
    Creates school with data passed
    :param form_data: schema of SchoolSchema
    :param db: Session of DB
    :return: create_school
    """
    return await services.create_school(form_data, db)


# ----------------------------------------------------------------------------------------------------------------------
router_intendant = APIRouter(
    prefix="/api/intendant",
    tags=["Intendant"],
    responses={404: {"description": "Not found"}},
)


@router_intendant.get("/get")
async def get_intendant(token: BaseLogged = Depends(), db: _Session = Depends(get_db)) -> IntendantModel:
    """
    Gets data about intendant from DB
    :param token: user JWT token
    :param db: Session of DB
    :return: data about intendant from DB
    """
    intendant = await services.get_current_intendant(token.token, db)
    return intendant


@router_intendant.get("/find-by-email")
async def find_intendant(email: str, token: str, db: _Session = Depends(get_db)) -> dict:
    """
    Looks from intendant by his email
    :param email: intendants' email to be found in DB
    :param token: user JWT token
    :param db: Session of DB
    :return: IntendantModel without password
    """
    intendant = await services.find_intendant(email, token, db)
    return intendant


@router_intendant.post("/register-admin")
async def create_school_admin(form_data: schemas.Intendant, db: _Session = Depends(get_db)):
    """
    Registers intendant as school admin
    :param form_data: schema of Intendant
    :param db: Session of DB
    :return: text if operation is completed
    """
    intendant = await services.create_intendant_school_admin(form_data, db)
    return dict(status_code=200, id_school=intendant.id_school)
