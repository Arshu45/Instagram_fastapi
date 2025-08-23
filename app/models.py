from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base

class Post(Base):
    __tablename__ = "posts"  # Table name in your database

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=False) 
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default="NOW()")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)

    # Defining relationship to User
    user = relationship("User", back_populates="posts")
    votes = relationship("Vote", back_populates="post")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default="NOW()")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True)

    # Defining relationship to posts
    posts = relationship("Post", back_populates="user")
    votes = relationship("Vote", back_populates="user")

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)

    user = relationship("User", back_populates="votes")
    post = relationship("Post", back_populates="votes")

