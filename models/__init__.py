from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import (
    POSTGRES_DATABASE,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
)


engine = create_engine(
    f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
    pool_size=20,
    max_overflow=0,
    pool_timeout=300,
)
Session = sessionmaker(engine, future=True)
