from main import app
from alembic import context
from core.db_src.db_models import *

config = context.config

alembic_config = app.get_section(config.config_ini_section)
alembic_config['sqlalchemy.url'] = app.config['SQLALCHEMY_DATABASE_URI']
