from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# JWT helpers

def create_access_token(data: dict, secret_key: str, algorithm: str, expires_delta: Optional[timedelta] = None, expire_minutes: int = 15) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=expire_minutes))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def verify_access_token(token: str, secret_key: str, algorithm: str, credentials_exception, token_data_class):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        id = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = token_data_class(user_id=id)
        return token_data
    except JWTError:
        raise credentials_exception
