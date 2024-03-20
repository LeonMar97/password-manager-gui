from fastapi import FastAPI ,HTTPException, status
from typing import List
from models import User
app = FastAPI()
db: List[User] = [User(user_name="leon", password="123456")]


@app.get("/api/v1/db")
def get_db():
    return db

@app.post("/api/v1/user")
async def register_user(usr:User):
    for i in db:
        if i.user_name==usr.user_name:
             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user already registerd")
    db.append(usr)
    return {"message": "User registered successfully"}, status.HTTP_201_CREATED
