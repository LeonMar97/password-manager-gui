from fastapi import FastAPI
from password_manager_gui.models.user_model import User
from password_manager_gui.models.password_model import Password
from password_manager_gui.database.local_database import LocalDatabase
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await db.connect_to_database()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
def ping() -> str:
    return HTMLResponse("pong")


db = LocalDatabase()


@app.post("/api/v1/add-user")
async def register_user(usr: User):
    """creates new user and adds to db"""
    return await db.register_user(usr)


@app.post("/api/v1/add-password")
async def add_passwords(usr: User, pas: Password):
    """creates a password of a website for user"""
    return await db.add_password(usr, pas)


# its post because im passing main password in the body, and i rather not pass it by parms
# should later on changed to work via session
@app.post("/api/v1/decrypt-passwords")
async def get_passwords(usr: User):
    """returns all decrypted password of user"""
    return await db.get_passwords(usr)
