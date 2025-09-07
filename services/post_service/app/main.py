from fastapi import FastAPI
from app.db.database import engine
from libs.db import Base
from app.api import posts, votes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# No need for Base.metadata.create_all(bind=engine) since Alembic is used

@app.get("/")
async def read_root():
    return {"Hello": "Post Service"}

# Include routers
app.include_router(posts.router)
app.include_router(votes.router)
