from fastapi import FastAPI
from app.database import engine, Base
from app.routers import posts, users, auth, votes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
# No needed for this since we set up Alembic for migrations
# Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"Hello": "World arsh"}


# Include routers
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)
