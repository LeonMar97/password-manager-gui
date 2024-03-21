from fastapi import FastAPI
from password_manager_gui.models.models import User
from password_manager_gui.database.local_database import LocalDatabase

app = FastAPI()

db = LocalDatabase()


# @app.get("/api/v1/db")
# def get_db():
#     return db
@app.get("/ping")
def ping() -> str:
    return "pong"


@app.post("/api/v1/user")
async def register_user(usr: User):
    return db.register_user(usr)
