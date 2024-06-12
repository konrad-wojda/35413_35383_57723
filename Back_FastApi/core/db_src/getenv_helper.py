from dotenv import load_dotenv
from pathlib import Path  # python3.6+
import os

# set path to env file
env_path = Path('.env').absolute()
load_dotenv(dotenv_path=env_path)


def getenv(var_name: str) -> str:
    """
    Gets data from .env file
    :param var_name: name of variable
    :return: string from variable
    """
    return os.getenv(var_name)


def getenv_int(var_name: str) -> int:
    """
    Gets data from .env file converted to int
    :param var_name: name of variable
    :return: string from variable
    """
    return int(os.getenv(var_name))
