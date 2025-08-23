from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Post, Vote
from app.schemas import PostCreate, PostResponse, UserResponse, PostResponseWithVotes
from app.oauth2 import get_current_user
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=list[PostResponseWithVotes])
def get_posts(
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user),
    limit: int = 100,
    search: Optional[str] = ""
):
    query = db.query(
        Post,
        func.count(Vote.post_id).label("votes")
    ).join(
        Vote, Post.id == Vote.post_id, isouter=True
    ).group_by(Post.id)

    if search:
        query = query.filter(
            Post.title.contains(search) | Post.description.contains(search)
        )

    results = query.limit(limit).all()
    return results

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(get_current_user)
):
    user_id = current_user.id
    new_post = Post(
        user_id=user_id,  
        title=post.title,
        description=post.description
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/{post_id}", response_model=PostResponseWithVotes)
def read_post(post_id: int, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    result = db.query(Post, func.count(Vote.post_id).label("votes"))\
        .join(Vote, Vote.post_id == Post.id, isouter=True)\
        .filter(Post.id == post_id)\
        .group_by(Post.id)\
        .first()
    if result:
        post, votes = result
        return {"Post": post, "votes": votes}
    raise HTTPException(status_code=404, detail="Post not found")

@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    existing_post = db.query(Post).filter(Post.id == post_id).first()
    if not existing_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if existing_post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    existing_post.title = post.title
    existing_post.description = post.description
    existing_post.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(existing_post)
    return existing_post

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
