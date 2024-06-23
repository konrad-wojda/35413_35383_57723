import re
from ..getenv_helper import getenv_int


async def is_valid_email(email: str) -> bool:
    """
    Checks with regex if email have correct format and length
    :param email: user email
    :return: True if email is valid / False if email is too long or not formatted correctly
    """
    if not email:
        return False
    email = email.lower()
    regex = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}\b'
    if len(email) > getenv_int("MAX_EMAIL_LEN"):  # test case
        return False
    if re.fullmatch(regex, email):
        return True
    return False


async def is_valid_passwords(password1: str, password2: str) -> bool:
    """
    Checks with regex if password matching pattern and if user correctly written same password twice
    :param password1: needed password
    :param password2: repeated password
    :return: True if password is valid and user repeated it correctly /
     False if password is too short or not formatted correctly
    """
    return are_passwords_matched(password1, password2) if is_valid_password(password1) else False


def is_valid_password(password: str) -> bool:
    """
    Check if password matches regex with minimal length
    :param password: password of user
    :return: True if password have good minimal length and regex pattern / False if regex is not matching
    """
    password_pattern = (fr"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{{"
                        fr"{getenv_int('MIN_PASSWORD_LEN')},}}$")

    return True if re.match(password_pattern, str(password)) else False


def are_passwords_matched(password1: str, password2: str) -> bool:
    """
    Checks if both passwords are same, meaning that user repeated password twice correctly
    :param password1: needed password
    :param password2: repeated password
    :return: True if password are matched, False if they're not same
    """
    return password1 == password2
