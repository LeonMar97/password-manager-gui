from fastapi import HTTPException,status
from database_base import Database
from models.models import User
from typing import List

class LocalDatabase(Database):
    def __init__(self):
        self.connect_to_database()

    async def register_user(self, usr: User):
        if self.user_exists(usr):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user already registerd")
        else:
            self.db.append(usr)
        return {"message": "User registered successfully"}, status.HTTP_201_CREATED
    
    async def user_exists(self, usr: User):
        '''using a genrator to check if there a name in the list'''
        return  any(cur_usr.user_name==usr.user_name for cur_usr in self.db)
             
    async def connect_to_database(self):
        self.db: List[User] = [User(user_name="leon", password="123456")]
        