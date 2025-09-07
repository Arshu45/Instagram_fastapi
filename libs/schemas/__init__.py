from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True
