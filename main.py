from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Role, Gender, UserUpdateRequest
app = FastAPI()

db: List[User] = [
    User(
        id=UUID("0d7192d0-aa11-4950-a5ab-97103dc5397d"),
        first_name = "Hari",
        last_name="Rajesh",
        middle_name = "B",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
        ),
    User(
        id=UUID("51a576a5-e4d0-49f9-8f3f-efa9da58456c"),
        first_name = "Karishma",
        last_name="Vishwa",
        middle_name = "R",
        gender=Gender.female,
        roles=[Role.student]
        )
]

@app.get("/")
async def root():
    return {"Hello":"Hari"}

@app.get("/api/v1/users")
async def fetch_users():
    return db 

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id":user.id}
@app.delete("/api/v1/users{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = f"user with id: {user_id} not found!"
    )


@app.put("/api/v1/users{upUser}")
def update_user(upUser:UUID, User_id:UserUpdateRequest):
    for user in db:
        if user.id == upUser:
            if User_id.first_name is not None:
                user.first_name = User_id.first_name
            
            if User_id.last_name is not None:
                user.last_name = User_id.last_name
            
            if User_id.middle_name is not None:
                user.middle_name = User_id.middle_name
            
            if User_id.roles is not None:
                user.roles = User_id.roles
            return
        
        raise HTTPException(
            status_code=404,
            detail = f"user id {User_id} does not exist"
        )
