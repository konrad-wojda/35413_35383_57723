from dotenv import load_dotenv
from os import getenv
from pathlib import Path  # python3.6+
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_src.db_models import user_models
from db_src.db_models.base_model import Base
from .db_settings import Settings


# set path to env file
env_path = Path('.env').absolute()
load_dotenv(dotenv_path=env_path)

if getenv('DB_TYPE') == "lite":
    print("SQLite here")
    engine = create_engine(Settings().db_url(), connect_args={"check_same_thread": False})  # args only if LiteDB
else:
    print("PostgresSQL here")
    engine = create_engine(Settings().db_url())

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engineTesting = create_engine('sqlite:///test.db', connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engineTesting)


def create_database(uri: str):
    user_models.UserModel()
    return Base.metadata.create_all(bind=create_engine(uri))


def get_db():
    create_database(Settings().db_url())
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def override_get_db():
    create_database('sqlite:///test.db')
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
