from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.core.config import settings
from libs.auth import create_access_token, verify_access_token
from libs.schemas import TokenData
from app.db.database import get_db

# Point to user service for token URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8000/auth/login")

SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expiration_minutes

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, SECRET_KEY, ALGORITHM, credentials_exception, TokenData)
    # For now, just return the user_id from the token
    return {"id": token_data.user_id}
