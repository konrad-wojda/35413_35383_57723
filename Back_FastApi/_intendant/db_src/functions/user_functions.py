import re


async def validate_email(email: str) -> bool:
    email = email.lower()
    regex = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}\b'
    if len(email) > 60:  # test case
        return False
    if re.fullmatch(regex, email):
        return True
    return False


async def validate_passwords(password1: str, password2: str) -> bool:
    if password1 != "" and password2 != "":
        return password1 == password2
    return False
