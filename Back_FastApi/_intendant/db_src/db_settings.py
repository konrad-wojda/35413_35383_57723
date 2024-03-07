from dotenv import load_dotenv
from pathlib import Path  # python3.6+
import os

# set path to env file
env_path = Path('.env').absolute()
load_dotenv(dotenv_path=env_path)
db_type = os.getenv('DB_TYPE')


class Settings:
    db_type = os.getenv('DB_TYPE')

    def db_url(self):
        if self.db_type == 'postgres':
            return os.getenv('DB_POSTGRES_URL')
        if self.db_type == 'lite':
            return os.getenv('DB_LITE_URL')

    def db_token(self):
        if self.db_type == 'postgres':
            return os.getenv('JWT_SECRET_POSTGRES')
        if self.db_type == 'lite':
            return os.getenv('JWT_SECRET_LITE')
