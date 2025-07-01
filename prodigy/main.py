from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import uuid

app = FastAPI()

# In-memory database
db = []

class User(BaseModel):
    id: str  # UUID as string
    name: str
    email: EmailStr
    age: int

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management API"}

@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    # Generate a unique UUID for the new user
    new_id = str(uuid.uuid4())
    # Check for duplicate email (optional, but good practice)
    for existing_user in db:
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="User with this email already exists")
    new_user = User(id=new_id, **user.dict())
    db.append(new_user)
    return new_user

@app.get("/users", response_model=List[User])
def get_users():
    return db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, user_update: UserUpdate):
    for index, user in enumerate(db):
        if user.id == user_id:
            updated_user = user.copy(update=user_update.dict(exclude_unset=True))
            db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str):
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return
    raise HTTPException(status_code=404, detail="User not found") 