from fastapi import FastAPI 
from models.models import User
from database.local_database import LocalDatabase
app = FastAPI()

db = LocalDatabase()
# @app.get("/api/v1/db")
# def get_db():
#     return db

@app.post("/api/v1/user")
async def register_user(usr:User):
    return db.register_user(usr)
