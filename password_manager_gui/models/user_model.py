from pydantic import BaseModel
# from uuid import UUID,uuid4


class User(BaseModel):
    # id:uuid4
    user_name: str
    password: str
