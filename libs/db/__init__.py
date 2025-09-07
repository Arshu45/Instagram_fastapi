from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

def get_engine(database_url: str):
    return create_engine(database_url)

Base = declarative_base()

def get_session_local(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db(SessionLocal) -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
