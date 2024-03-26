from fastapi import HTTPException,status
from password_manager_gui.database.database_base import Database
from password_manager_gui.models.models import User
import password_manager_gui.backend.encryption as encryption
# from typing import List

class LocalDatabase(Database):
    async def register_user(self, usr: User):
        if await self.user_exists(usr):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user already registerd")
        else:
            '''adding the password as 32 bit for now...'''
            usr.password=encryption.generate_kdf(usr.password)
            self.db.append(usr)
            return {"message": "User registered successfully"}, status.HTTP_201_CREATED
    
    async def user_exists(self, usr: User):
        '''using a genrator to check if there a name in the list'''
        return any(cur_usr.user_name==usr.user_name for cur_usr in self.db)
    
    
    async def connect_to_database(self):
        self.db = [User(user_name="leon", password="123456")]