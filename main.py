from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

users = []

app = FastAPI()

class User_Base(BaseModel):
    id: int
    username: str
    email: str


@app.get("/users/{user_id}", response_model=User_Base)
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
        
@app.get("/users", response_model=list[User_Base])
def get_users():
    return users

@app.post("/create_user", response_model=User_Base)
def create_user(user: User_Base):
    users.append(user)
    return user