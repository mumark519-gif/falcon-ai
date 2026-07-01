from app.database import engine
from app.models import Base
import app.models
from app.ai_service import analyze_business_problem
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from app.auth import get_current_user
from fastapi import FastAPI
from pydantic import BaseModel

from app.auth import hash_password, verify_password, create_access_token
from app.schemas import User
app = FastAPI()
Base.metadata.create_all(bind=engine)

users = {}


class User(BaseModel):
    username: str
    password: str

class BusinessRequest(BaseModel):
    problem: str  
@app.get("/")
def root():
    return {"message": "Welcome to Falcon AI!"}


@app.post("/register")
def register(user: User):
    if user.username in users:
        return {"error": "User already exists"}

    users[user.username] = hash_password(user.password)
    return {"message": "User registered successfully"}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username not in users:
        return {"error": "Invalid username or password"}

    if not verify_password(form_data.password, users[form_data.username]):
        return {"error": "Invalid username or password"}

    token = create_access_token({"sub": form_data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@app.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {
        "message": f"Welcome {current_user}!"
    }
@app.post("/analyze")
def analyze(request: BusinessRequest):
    analysis = analyze_business_problem(request.problem)

    return {
        "problem": request.problem,
        "analysis": analysis
    }  