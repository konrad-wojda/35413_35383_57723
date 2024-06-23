import jwt
from typing import TypedDict
from core.db_src import db_settings


class JwtPayload(TypedDict):
    id_user: int
    email: str


JWT_SECRET = db_settings.Settings().db_token()


def encode_jwt(user: JwtPayload) -> str:
    """
    Encodes data about user into JWT
    :param user: logged user data
    :return: JWT token
    """
    print("JWT_SECRET", JWT_SECRET)
    return jwt.encode({"id_user": user['id_user'], "email": user['email']}, JWT_SECRET)


def decode_jwt(token: str) -> JwtPayload:
    """
    Decodes JWT into dictionary with data about user
    :param token: JWT Token
    :return: dict with data about user
    """
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
