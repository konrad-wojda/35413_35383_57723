from fastapi.testclient import TestClient
from db_src.database import get_db, override_get_db
from db_src.db_models.user_models import UserModel
from passlib import hash
from main import app
import os
import jwt

client = TestClient(app)

email, password = 'string@com.pl', 'String123'


def clean_up(*args: str):
    if 'end' in args:
        if os.path.exists("test.db"):
            os.remove("test.db")
        return
    if os.path.exists("test.db"):
        os.remove("test.db")
    app.dependency_overrides[get_db] = override_get_db
    if 'add_user' in args:
        db = next(override_get_db())
        passwrd = 'String123'
        if 'String123!' in args:
            passwrd = 'String123!'
        db.add(UserModel(email=email, hashed_password=hash.bcrypt.hash(passwrd)))
        db.commit()
    jwt_secret = 'nothingspecialtogetitright'
    token = jwt.encode({'user_id': 1, "email": email}, jwt_secret)
    return token


def test_login_good(_password: str = 'String123!'):
    token = clean_up('add_user', _password)
    response = client.post(
        "/api/login",
        json={"email": email, "hashed_password": _password},
    )
    assert response.status_code == 200
    assert response.json() == {'status_code': 200, "user_id": 1, "token": token, "token_type": "bearer"}

    clean_up('end')


def test_login_bad():
    clean_up()
    response = client.post(
        "/api/login",
        json={"email": email, "hashed_password": password},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid Credentials"}

    clean_up('end')


def test_register_good():
    clean_up()
    response = client.post(
        "/api/register",
        json={"email": email, "hashed_password": password, "repeat_password": password},
    )
    assert response.status_code == 200
    assert response.json() == {'status_code': 200, "email": email}

    clean_up('end')


def test_register_repeat():
    clean_up("add_user")
    response = client.post(
        "/api/register",
        json={"email": email, "hashed_password": password, "repeat_password": password},
    )
    assert response.status_code == 402
    assert response.json() == {'detail': 'Email already in use'}

    clean_up('end')


def test_register_bad_passwords():
    clean_up("add_user")
    response = client.post(
        "/api/register",
        json={"email": email, "hashed_password": password, "repeat_password": password[0:-1]},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Passwords not match, or at least one is empty'}

    response = client.post(
        "/api/register",
        json={"email": email, "hashed_password": password, "repeat_password": ''},
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Passwords not match, or at least one is empty'}

    clean_up('end')


def test_register_bad_email():
    clean_up("add_user")
    response = client.post(
        "/api/register",
        json={"email": email[0:-1], "hashed_password": password, "repeat_password": password},
    )
    assert response.status_code == 403
    assert response.json() == {'detail': 'E-mail is not valid'}

    clean_up('end')


def test_user_exists():
    token = clean_up('add_user')
    response = client.get(
        f"/api/user?token={token}",
    )
    assert response.status_code == 200
    assert response.json() == {'email': 'string@com.pl', 'first_name': '', 'flat_number': 0, 'is_active': True,
                               'is_admin': False, 'is_employee': False, 'last_name': '', 'post_code': 0,
                               'street_name': '', 'street_number': 0, 'telephone': 0, 'user_id': 1}

    clean_up('end')


def test_user_not_exists():
    clean_up()
    response = client.get(
        f"/api/user?token=bad.token",
    )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Token not exists'}

    clean_up('end')


def test_user_edit():
    token = clean_up('add_user')
    response = client.patch(
        "/api/user/edit",
        json={"token": token, "hashed_password": "String123!"},
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "User edited"}
    test_login_good('String123!')
    clean_up('end')


def test_user_edit_bad():
    clean_up('add_user')
    response = client.patch(
        "/api/user/edit",
        json={"token": "bad.token", "hashed_password": "String123!"},
    )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Token not exists'}
    clean_up('end')


def test_delete_good():
    clean_up('add_user')
    response = client.delete(
        "/api/user/delete",
        json={"email": email, "hashed_password": password, "repeat_password": password, "user_id": 1},
    )
    assert response.status_code == 200
    assert response.json() == {'status_code': 200, 'text': 'Account got deleted'}

    clean_up('end')


def test_delete_bad():
    clean_up()
    response = client.delete(
        "/api/user/delete",
        json={"email": email, "hashed_password": password, "repeat_password": password, "user_id": 2},
    )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid Credentials'}

    clean_up('end')
