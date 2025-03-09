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
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE")
