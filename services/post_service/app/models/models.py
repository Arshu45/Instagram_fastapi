from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from libs.db import Base

class Post(Base):
    __tablename__ = "post_service_posts"  # Table name in your database

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # No foreign key constraint
    title = Column(String, nullable=False) 
    description = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default="NOW()")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)

    # Note: User relationship will be handled via API calls to user_service
    votes = relationship("Vote", back_populates="post")

class Vote(Base):
    __tablename__ = "post_service_votes"

    user_id = Column(Integer, primary_key=True)  # No foreign key constraint
    post_id = Column(Integer, ForeignKey("post_service_posts.id", ondelete="CASCADE"), primary_key=True)

    # Note: User relationship will be handled via API calls to user_service
    post = relationship("Post", back_populates="votes")
