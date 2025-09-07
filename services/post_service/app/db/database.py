from app.core.config import settings
from libs.db import get_engine, get_session_local, Base

DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = get_engine(DATABASE_URL)
SessionLocal = get_session_local(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
