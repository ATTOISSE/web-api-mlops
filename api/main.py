from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
import sys, os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.connexion import SessionLocal
from schemas.schemas import User as UserSchema  # Import correct avec le chemin complet
from db.crud import get_all_users, get_user

app = FastAPI()

@app.get("/users/{email}", response_model=UserSchema)
def read_user(email: str):
    db: Session = SessionLocal()
    try:
        user = get_user(db, email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    finally:
        db.close()

@app.get("/users/", response_model=List[UserSchema])
def read_users():
    db: Session = SessionLocal()
    try:
        return get_all_users(db)
    finally:
        db.close()

# Optionnel : endpoint pour créer un utilisateur
@app.post("/users/", response_model=UserSchema)
def create_user_endpoint(user: UserSchema):
    from db.crud import create_user
    db: Session = SessionLocal()
    try:
        # Vérifier si l'utilisateur existe déjà
        existing_user = get_user(db, user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        return create_user(db, user)
    finally:
        db.close()

# Optionnel : endpoint de base pour tester
@app.get("/")
def root():
    return {"message": "API Users - FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)