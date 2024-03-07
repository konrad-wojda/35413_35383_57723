from fastapi import Depends, security, HTTPException
from sqlalchemy.orm import Session as _Session
from passlib import hash

from db_src import schemas, db_settings
from db_src.db_models import product_models
from db_src.database import get_db
import jwt

oauth2schema = security.OAuth2PasswordBearer(tokenUrl="/api/token")
JWT_SECRET = db_settings.Settings().db_token()


async def get_user_by_email(email: str, db: _Session = Depends(get_db)):
    return db.query(user_models.UserModel).filter(user_models.UserModel.email == email).first()
