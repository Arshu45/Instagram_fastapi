from pydantic import BaseModel, conint
from datetime import datetime
from typing import Optional

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
    # Note: user field removed since we don't have direct relationships

    class Config:
        from_attributes = True

class PostResponseWithVotes(BaseModel):
    Post: PostResponse
    votes: int

# Voting Schemas
class VoteCreate(BaseModel):
    post_id: int
    direction: conint(ge=0, le=1)

class VoteResponse(BaseModel):
    user_id: int
    post_id: int
    class Config:
        from_attributes = True
