from fastapi import FastAPI
from password_manager_gui.models.models import User
from password_manager_gui.database.local_database import LocalDatabase
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await db.connect_to_database()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/ping")
def ping() -> str:
    return "pong"

db = LocalDatabase()


@app.post("/api/v1/user")
async def register_user(usr: User):
    return await db.register_user(usr)
