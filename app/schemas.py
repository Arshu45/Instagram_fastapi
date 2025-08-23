from pydantic import BaseModel, conint
from datetime import datetime
from pydantic import EmailStr
from typing import Optional


# User schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True

# Post schemas

class PostCreate(BaseModel):
    title: str
    description: str

class PostResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None

    # User
    user: UserResponse

    class Config:
        from_attributes = True

class PostResponseWithVotes(BaseModel):
    Post: PostResponse
    votes: int

# Authentication schemas
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None


# Voting Schemas
class VoteCreate(BaseModel):
    post_id: int
    direction: conint(ge=0, le=1)

class VoteResponse(BaseModel):
    user_id: int
    post_id: int

    class Config:
        from_attributes = True