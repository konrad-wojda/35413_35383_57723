from fastapi import HTTPException
from sqlalchemy.orm import Session as _Session
from sqlalchemy import update
from passlib import hash
from db_src import schemas, db_settings
from db_src.db_models.user_models import UserModel
import jwt

JWT_SECRET = db_settings.Settings().db_token()


async def get_user_by_email(email: str, db: _Session):
    return db.query(UserModel).filter(UserModel.email == email).first()


async def create_user(user: schemas.UserPasswords, db: _Session):
    user_obj = UserModel(
        email=user.email, hashed_password=hash.bcrypt.hash(user.hashed_password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)

    return user_obj


async def authenticate_user(email: str, password: str, db: _Session) -> UserModel | bool:
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False

    if not user.verify_password(password):
        return False

    return user


async def generate_token(
        form: schemas.UserPasswords,
        db: _Session,
        ):
    user: UserModel | bool = await authenticate_user(email=form.email, password=form.hashed_password, db=db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")

    return await create_token(user)


async def create_token(user: UserModel):
    user_obj = schemas.UserPasswords.from_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(status_code=200, token=token, token_type="bearer", user_id=user.user_id)


async def get_current_user(
    token: str,
    db: _Session,
):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = db.query(UserModel).get(payload["user_id"]).__dict__
    except:
        raise HTTPException(status_code=401, detail="Token not exists")
    return user


async def update_user(form_data: schemas.UserEdit, db: _Session):
    user = await get_current_user(form_data.token, db)
    del form_data.token
    if user['user_id'] == form_data.user_id:
        db.execute(
            update(UserModel).
            where(UserModel.user_id == user['user_id']).
            values(
                form_data.dict(exclude_none=True)
            )
        )
        db.commit()


async def delete_user(form_data: schemas.UserPasswords, db: _Session):
    user = db.query(UserModel).filter(UserModel.email == form_data.email).first()
    db.execute(
        update(UserModel).
        where(UserModel.user_id == user.user_id).
        values(email="",
               hashed_password="",
               first_name="",
               last_name="",
               telephone=0,
               post_code=0,
               street_name="",
               street_number=0,
               flat_number=0,
               is_employee=False,
               is_active=False))
    db.commit()
