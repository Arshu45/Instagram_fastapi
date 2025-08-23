from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.oauth2 import get_current_user
from app.models import Vote, Post
from app.schemas import VoteCreate, UserResponse

router = APIRouter(
    prefix="/vote",
    tags=["votes"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: VoteCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):

    post = db.query(Post).filter(Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    db_vote = db.query(Vote).filter(Vote.post_id == vote.post_id, Vote.user_id == current_user.id).first()

    if vote.direction == 1:
        if db_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="You have already voted on this post")
        new_vote = Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message": "Vote added"}

    elif vote.direction == 0:
        if not db_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote not found")
        db.delete(db_vote)
        db.commit()
        return {"message": "Vote removed"}

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid vote direction")