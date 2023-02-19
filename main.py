<<<<<<< HEAD
=======
import hashlib

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean
import bcrypt
import sqlite3

app = FastAPI()

# Database configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./identifier.sqlite.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def create_database():
    conn = sqlite3.connect(SQLALCHEMY_DATABASE_URL[10:])
    cursor = conn.cursor()
    conn.commit()
    conn.close()


# Database models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


# Pydantic models
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()


# API endpoints
@app.post("/register")
async def register(user: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)  # you should implement a secure password hashing function here
    db_user = User(email=user.email, password=hashed_password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/login")
async def login(email: str, password: str):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username")
    # hashed_password = hash_password(password)
    if hash_password(password) != db_user.password:
        raise HTTPException(status_code=400, detail="Invalid password")
    return {"message": "Login successful"}


# Create database and tables if they do not exist
create_database()
Base.metadata.create_all(bind=engine)
>>>>>>> origin/develop_cherigra
