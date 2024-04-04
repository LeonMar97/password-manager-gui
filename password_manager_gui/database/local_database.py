from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from password_manager_gui.database.database_base import Database
from password_manager_gui.models.user_model import User
from password_manager_gui.models.password_model import Password
import password_manager_gui.backend.encryption as encryption
import json
# from typing import List


class LocalDatabase(Database):
    async def register_user(self, usr: User):
        """adds new user to a local db (in memory for now)
        Parameter:
        usr=user for db
        """
        if await self.user_exists(usr):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user already registerd")
        else:
            self.db[usr.user_name] = encryption.generate_kdf(usr.password)
            content = {"message": "User registered successfully"}
            return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)

    async def user_exists(self, usr: User) -> bool:
        """checks existence for user in db (in memory for now)
        Parameter:
        usr=user to check
        """
        return usr.user_name in self.db

    async def connect_to_database(self):
        self.db = {"leonm": encryption.generate_kdf("1234")}

    async def validate_user(self, usr: User) -> bool:
        """checks if the users password matches whats in db (in memory for now)
        Parameter:
        usr=user to check
        """
        if await self.user_exists(usr):
            return self.db[usr.user_name] == encryption.generate_kdf(usr.password)
        else:
            return False

    async def add_password(self, usr: User, pas: Password):
        """adds a site password to a local file in passwords/encrypted_passwords file
        Parameters:
        usr=user to add to
        password= site info to encrypt
        """
        if await self.validate_user(usr):
            password_json = {"user_name": pas.website_user_name, "password": pas.website_password}
            if encryption.encrypt_data(
                main_usr=usr.user_name, main_pass=usr.password, website=pas.website_url, new_password=password_json
            ):
                content = {"message": "password added successfully"}
                return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something is wrong with the encryption"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=f"password for user {usr.user_name} is incorect"
            )

    async def get_passwords(self, usr: User):
        """returns a json list for all the passwords of the user
        Parameter:
        usr=user for the passwords
        """
        # should be changed later on to get passwords for multiple users

        if await self.validate_user(usr):
            decrypted_data = encryption.decrypt_data(usr.user_name + usr.password)
            if decrypted_data:
                return json.loads(decrypted_data.replace("'", '"'))
            else:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="something is wrong with the encryption"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=f"password for user {usr.user_name} is incorect"
            )
