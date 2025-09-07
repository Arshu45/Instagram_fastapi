from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from libs.schemas import Token, TokenData, UserResponse

# User schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    password: str

# Authentication schemas
class UserLogin(BaseModel):
    email: EmailStr
    password: str