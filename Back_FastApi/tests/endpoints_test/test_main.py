from fastapi.testclient import TestClient
from passlib import hash
from main import app
import jwt
from core.db_src.database import get_db, override_get_db,create_database, clear_database
from core.db_src.db_models import UserModel
from core.db_src.getenv_helper import getenv_int


app.dependency_overrides[get_db] = override_get_db
db = next(override_get_db())
client = TestClient(app)
email, password = 'string@com.pl', 'String123*'


def clean_up(*args: str):
    clear_database()
    create_database()

    if 'add_user' in args:
        passwrd = 'String123'
        if 'String123*' in args:
            passwrd = 'String123*'

        db.add(UserModel(email=email, hashed_password=hash.bcrypt.hash(passwrd)))
        db.commit()
    jwt_secret = 'nothingspecialtogetitrightlite'
    token = jwt.encode({'id_user': 1, "email": email}, jwt_secret)
    return token


def test_health_check():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == "Server is running"


def test_login_good(_password: str = password):
    token = clean_up('add_user', _password)
    response = client.post(
        "/api/user/login",
        json={"email": email, "hashed_password": _password},
    )
    assert response.status_code == 200
    assert response.json() == {'status_code': 200, "id_user": 1, "token": token, "token_type": "bearer"}


def test_login_bad():
    clean_up()
    response = client.post(
        "/api/user/login",
        json={"email": email, "hashed_password": password+'1'},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid Credentials"}


def test_register_good():
    clean_up()
    response = client.post(
        "/api/user/register",
        json={"email": email, "hashed_password": password, "repeat_password": password},
    )
    assert response.status_code == 200
    assert response.json() == {'status_code': 200, "email": email}


def test_register_repeat_bad():
    clean_up("add_user")
    response = client.post(
        "/api/user/register",
        json={"email": email, "hashed_password": password, "repeat_password": password},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Email already in use'}


def test_register_bad_passwords():
    clean_up("add_user")
    response = client.post(
        "/api/user/register",
        json={"email": email, "hashed_password": password, "repeat_password": password[0:-1]},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': f"Passwords not match, or at least one is shorter than"
                                         f" {getenv_int('MIN_PASSWORD_LEN')} characters, "
                                         f"password should have small and capital letter with number"
                                         f" and special character."}

    response = client.post(
        "/api/user/register",
        json={"email": email, "hashed_password": password, "repeat_password": ''},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': f"Passwords not match, or at least one is shorter than"
                                         f" {getenv_int('MIN_PASSWORD_LEN')} characters, "
                                         f"password should have small and capital letter with number"
                                         f" and special character."}


def test_register_bad_email():
    clean_up("add_user")
    response = client.post(
        "/api/user/register",
        json={"email": email[0:-1], "hashed_password": password, "repeat_password": password},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': "E-mail is not valid or too long; max "
                                         f"{getenv_int('MAX_EMAIL_LEN')} characters."}


def test_user_exists():
    token = clean_up('add_user')
    response = client.get(
        f"/api/user/get?token={token}",
    )
    assert response.status_code == 200
    assert response.json() == {'email': 'string@com.pl', 'first_name': '', 'last_name': '',
                               'is_admin': False, 'id_user': 1}


def test_user_not_exists():
    clean_up()
    response = client.get(
        f"/api/user/get?token=bad.token",
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'Token not exists'}


#
#
# def test_user_edit():
#     token = clean_up('add_user')
#     response = client.patch(
#         "/api/user/edit",
#         json={"token": token, "hashed_password": "String123!"},
#     )
#     assert response.status_code == 200
#     assert response.json() == {"detail": "User edited"}
#     test_login_good('String123!')
#     
#
#
# def test_user_edit_bad():
#     clean_up('add_user')
#     response = client.patch(
#         "/api/user/edit",
#         json={"token": "bad.token", "hashed_password": "String123!"},
#     )
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Token not exists'}
#     
#
#
# def test_delete_good():
#     clean_up('add_user')
#     response = client.delete(
#         "/api/user/delete",
#         json={"email": email, "hashed_password": password, "repeat_password": password, "id_user": 1},
#     )
#     assert response.status_code == 200
#     assert response.json() == {'status_code': 200, 'text': 'Account got deleted'}
#
#     
#
#
# def test_delete_bad():
#     clean_up()
#     response = client.delete(
#         "/api/user/delete",
#         json={"email": email, "hashed_password": password, "repeat_password": password, "id_user": 2},
#     )
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Invalid Credentials'}
#
#     
