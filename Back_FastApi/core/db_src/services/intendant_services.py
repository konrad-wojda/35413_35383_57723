from typing import Type

from fastapi import HTTPException
from sqlalchemy.orm import Session as _Session
from sqlalchemy import update, delete, Row
from passlib import hash

from core.db_src.db_models.intendant_models import UserModel, SchoolModel, IntendantModel
import core.db_src.schemas.intendant_schemas as schemas
from core.db_src.functions.jwt_functions import encode_jwt, decode_jwt
from core.db_src.schemas import BaseLogged


async def get_user_by_email(email: str, db: _Session) -> Type[UserModel] | None:
    """
    Checks DB if there is already user with passed email address
    :param email: email of user to find
    :param db: Session of DB
    :return: UserModel with matched email / None if user not found
    """
    return db.query(UserModel).filter(UserModel.email == email).first()


async def create_user(user: schemas.UserPasswords, db: _Session) -> UserModel:
    """
    Creating new user in DB
    :param user: schema of User with passwords passed
    :param db: Session of DB
    :return: Data of created user
    """
    user_obj = UserModel(
        email=user.email, hashed_password=hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    if user_obj.id_user == 1:
        await make_admin(db)

    return user_obj


async def make_admin(db: _Session) -> None:
    """
    Promoting 1st registered user as admin of whole app
    :param db: Session of DB
    :return: None
    """
    db.execute(update(UserModel).values(is_admin=True).where(UserModel.id_user == 1))


async def authenticate_user(email: str, password: str, db: _Session) -> Type[UserModel] | bool:
    """
    checks if user by email used good password
    :param email: user email
    :param password: user password
    :param db: Session of DB
    :return: Data of created user / False if there is no user nor hash of password matches
    """
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not user.verify_password(password=password):
        return False

    return user


async def generate_token(
        form: schemas.UserPasswords,
        db: _Session,
) -> callable:
    """
    Calls functions to create JWT if user is logged
    :param form: schema of UserPasswords
    :param db: Session of DB
    :return: function with response and token
    """
    user: UserModel | bool = await authenticate_user(email=form.email, password=form.hashed_password, db=db)

    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")

    return await create_token(user)


async def create_token(user: UserModel) -> dict:
    """
    Creates JWT from data about user
    :param user: data of user from DB
    :return: response with token
    """
    token = encode_jwt({"id_user": user.__dict__['id_user'], "email": user.__dict__['email']})
    return dict(status_code=200, token=token, token_type="bearer", id_user=user.id_user)


async def get_current_user(
        token: str,
        db: _Session,
) -> Type[UserModel]:
    """
    Gets data about user from DB
    :param token: JWT with user info
    :param db: Session of DB
    :return: user data from DB
    """
    try:
        payload = decode_jwt(token)
        user = db.query(UserModel).get(payload["id_user"]).__dict__
    except:
        raise HTTPException(status_code=404, detail="Token not exists")
    return user


async def get_current_intendant_worker(
        token: str,
        db: _Session,
) -> Row[tuple[UserModel, IntendantModel, SchoolModel]]:
    """
    Gets data about user from DB
    :param token: JWT with user info
    :param db: Session of DB
    :return: user data from DB
    """
    try:
        payload = decode_jwt(token)
        user = db.query(UserModel, IntendantModel, SchoolModel). \
            join(IntendantModel, UserModel.id_user == IntendantModel.id_user). \
            join(SchoolModel, IntendantModel.id_school == SchoolModel.id_school). \
            filter(UserModel.id_user == payload["id_user"]).first()
    except:
        raise HTTPException(status_code=404, detail="Token not exists")
    return user


async def update_user(form_data: schemas.UserRest, db: _Session) -> dict:
    """
    Updates user data in DB if user token is good
    :param form_data: schema of UserRest
    :param db: Session of DB
    :return: confirmation
    """
    user = await get_current_user(form_data.token, db)
    form_data.hashed_password = hash.bcrypt.hash(form_data.hashed_password)
    del form_data.token
    db.execute(
        update(UserModel).
        where(UserModel.id_user == user['id_user']).
        values(
            form_data.dict(exclude_none=True)
        )
    )
    db.commit()
    return dict(detail="User edited")


async def delete_user(form_data: schemas.UserPasswords, db: _Session) -> None:
    """
    Deletes user from DB
    :param form_data: schema of UserPasswords
    :param db: Session of DB
    """
    user = db.query(UserModel).filter(UserModel.email == form_data.email).first()
    db.execute(delete(UserModel).where(UserModel.id_user == user.id_user))
    db.commit()


async def create_school(school: schemas.SchoolSchema, db: _Session) -> SchoolModel | None:
    """
    Adds school data to DB
    :param school: schema of SchoolSchema
    :param db: Session of DB
    :return: School data from DB / raise error 404
    """
    user = await get_current_user(school.token, db)
    if user["is_admin"]:
        school = {**school.dict()}
        school.pop('token')
        school_obj = SchoolModel(**school)
        db.add(school_obj)
        db.commit()
        db.refresh(school_obj)

        return school_obj
    raise HTTPException(status_code=404, detail="Token not exists nor user is admin")


async def get_current_intendant(
        token: str,
        db: _Session,
) -> IntendantModel:
    """
    Gets data from DB about intendant with token
    :param token: user JWT token
    :type db: Session of DB
    :return: Intendant data from DB
    """
    try:
        payload = decode_jwt(token)
        intendant = db.query(IntendantModel).filter(IntendantModel.id_user == payload["id_user"]).first().__dict__
        intendant.pop('_sa_instance_state')
    except:
        raise HTTPException(status_code=404, detail="Token have no intendant role")
    return intendant


async def find_intendant(
        email: str,
        token: str | BaseLogged,
        db: _Session,
) -> dict:
    """
    Gets data about intendant from DB with email
    :param token: user JWT token
    :param email: intendant email
    :param db: Session of DB
    :return: intendant data without password
    """
    payload = decode_jwt(token)
    user = db.query(UserModel).filter(UserModel.id_user == payload["id_user"]).first()
    if not user.is_admin:
        raise HTTPException(status_code=404, detail="Token have no admin role")

    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not registered")
    try:
        result = (db.query(UserModel, IntendantModel)
                  .filter(UserModel.id_user == user.id_user)
                  .filter(IntendantModel.id_user == UserModel.id_user)
                  .all())

        intendant_user = {}
        for user, intendant in result:
            intendant_user = {**intendant.__dict__, **user.__dict__}
        intendant_user.pop('hashed_password')
    except:
        raise HTTPException(status_code=404, detail="No school associated with this email")
    return intendant_user


async def create_intendant_school_admin(intendant: schemas.Intendant, db: _Session) -> IntendantModel:
    """
    Adds user as main admin of school
    :param intendant: schema of Intendant
    :param db: Session of DB
    :return: data of created intendant
    """
    admin = await get_current_user(intendant.token, db)
    if not admin["is_admin"]:
        raise HTTPException(status_code=404, detail="Token not exists or user is not admin")

    user_id_row = db.query(UserModel.id_user).filter(UserModel.email == intendant.email).first()
    user_id = user_id_row[0]

    if not db.query(SchoolModel.id_school).filter(SchoolModel.id_school == intendant.id_school).first():
        raise HTTPException(status_code=404, detail=f"School with id {intendant.id_school} not exists")

    intendant_obj = IntendantModel(is_main_admin=True, id_user=user_id, id_school=intendant.id_school)
    db.add(intendant_obj)
    db.commit()
    db.refresh(intendant_obj)

    return intendant_obj
