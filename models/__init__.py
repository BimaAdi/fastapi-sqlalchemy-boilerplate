from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import (
    POSTGRESQL_DATABASE,
    POSTGRESQL_HOST,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_PORT,
    POSTGRESQL_USER,
)


engine = create_engine(
    f"postgresql+psycopg://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}",
    pool_size=20,
    max_overflow=0,
    pool_timeout=300,
)
Session = sessionmaker(engine, future=True)
