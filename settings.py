import os
from core.log import logger
# from models import engine

if os.environ.get("ENVIRONTMENT") != "os":
    logger.info("load env from file")
    from dotenv import load_dotenv

    load_dotenv()
else:
    logger.info("load env from os")

# Environtment
ENVIRONTMENT = os.environ.get("ENVIRONTMENT")

# Postgresql conf
POSTGRESQL_USER = os.environ.get("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
POSTGRESQL_HOST = os.environ.get("POSTGRESQL_HOST")
POSTGRESQL_PORT = os.environ.get("POSTGRESQL_PORT")
POSTGRESQL_DATABASE = os.environ.get("POSTGRESQL_DATABASE")
