from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .db_settings import Settings
from dotenv import load_dotenv
from pathlib import Path  # python3.6+
from os import getenv

# set path to env file
env_path = Path('.env').absolute()
load_dotenv(dotenv_path=env_path)

if getenv('DB_TYPE') == "lite":
    print("SQLite here")
    engine = create_engine(Settings().db_url(), connect_args={"check_same_thread": False})  # args only if LiteDB
else:
    print("PostgresSQL here")
    engine = create_engine(Settings().db_url())


Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        session.close()

