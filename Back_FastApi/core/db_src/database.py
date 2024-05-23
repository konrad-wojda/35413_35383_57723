from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .db_settings import Settings
from .getenv_helper import getenv

Base = declarative_base()


def create_database(uri: str) -> callable:
    """
    Creates ORM models for certain DB connection
    :param uri: uri of DB
    :return: Function with creating DB with models
    """
    return Base.metadata.create_all(bind=create_engine(uri))


def get_db():
    """
    Makes connecting session for DB
    """
    if getenv('DB_TYPE') == "lite":
        print("SQLite here")
        engine = create_engine(Settings().db_uri(), connect_args={"check_same_thread": False})  # args only if LiteDB
    else:
        print("PostgresSQL here")
        engine = create_engine(Settings().db_uri())

    create_database(Settings().db_uri())
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    try:
        yield session
    finally:
        session.close()


def override_get_db():
    """
    Overrides connecting session for testing purpose
    """
    print("override SQLite here")
    engine = create_engine('sqlite:///test.db', connect_args={"check_same_thread": False})
    testing_session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = testing_session_local()

    try:
        yield session
    finally:
        session.close()
