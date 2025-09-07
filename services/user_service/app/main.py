from fastapi import FastAPI
from app.db.database import engine
from libs.db import Base
from app.api import users, auth
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
    return {"Hello": "User Service"}

# Include routers
app.include_router(users.router)
app.include_router(auth.router)
