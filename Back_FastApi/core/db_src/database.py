from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool

from .db_settings import Settings
from .getenv_helper import getenv

Base = declarative_base()
testing_database_uri = "sqlite:///:memory:"
testing_engine = create_engine(
        testing_database_uri, connect_args={"check_same_thread": False}, poolclass=StaticPool
    )


def create_database(engine: Engine = testing_engine) -> callable:
    """
    Creates ORM models for certain DB connection
    :param engine: engine of DB
    :return: Function with creating DB with models
    """
    return Base.metadata.create_all(bind=engine)


def clear_database() -> callable:
    """
    Removes ORM models for certain DB connection
    :return: Function dropping DB tables
    """
    return Base.metadata.drop_all(bind=testing_engine)


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

    # create_database(engine)
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
    engine = testing_engine
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    testing_session = session()

    try:
        yield testing_session
    finally:
        testing_session.close()
