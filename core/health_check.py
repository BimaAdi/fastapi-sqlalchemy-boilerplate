from core.log import logger
from settings import POSTGRES_HOST, POSTGRES_PORT
from models import Session


def health_check():
    logger.info("run app with")
    logger.info(f"postgres host = {POSTGRES_HOST}")
    logger.info(f"postgres port = {POSTGRES_PORT}")
    logger.info("try echo postgres db")
    with Session() as db:
        logger.info(not db.connection().closed)
    logger.info("successfully connect to postgres")
