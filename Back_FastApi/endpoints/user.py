from fastapi import HTTPException,APIRouter, Depends
from fastapi.templating import Jinja2Templates
from db_src.database import get_db
from sqlalchemy.orm import Session as _Session

from db_src import schemas
from db_src.services import user_services as services
from db_src.functions import user_functions as functions

templates = Jinja2Templates(directory="templates")


router = APIRouter(
    prefix="/api",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
async def read_item(form_data: schemas.UserPasswords, db: _Session = Depends(get_db)):

    return await services.generate_token(form_data, db)


@router.post("/register")
async def create_user(form_data: schemas.UserPasswords, db: _Session = Depends(get_db)):
    form_data.email = form_data.email.lower()
    if not await functions.validate_passwords(form_data.hashed_password, form_data.repeat_password):
        raise HTTPException(status_code=400, detail="Passwords not match, or at least one is empty")

    if await services.get_user_by_email(form_data.email, db):
        raise HTTPException(status_code=402, detail="Email already in use")

    if not await functions.validate_email(form_data.email):
        raise HTTPException(status_code=403, detail="E-mail is not valid")

    user = await services.create_user(form_data, db)
    return dict(status_code=200, email=user.email)


@router.get("/user")
async def get_user(token: str, db: _Session = Depends(get_db)):
    user = await services.get_current_user(token, db)
    user.pop('hashed_password')
    user.pop('created_at')
    return user


@router.patch("/user/edit")
async def edit_user(form_data: schemas.UserEdit, db: _Session = Depends(get_db)):
    await services.update_user(form_data, db)


@router.delete("/user/delete")
async def delete_user(form_data: schemas.UserPasswords, db: _Session = Depends(get_db)):
    if form_data.hashed_password == form_data.repeat_password:
        await services.generate_token(form_data, db)
    else:
        raise HTTPException(status_code=401, detail="Passwords not match")
    await services.delete_user(form_data, db)

    return {'status_code': 200, 'text': 'Account got deleted'}

