from abc import ABC, abstractmethod
from password_manager_gui.models.user_model import User
from password_manager_gui.models.password_model import Password


class Database(ABC):
    def __init__(self):
        self.db = None  # Initialize db variable to None initially

    @abstractmethod
    async def connect_to_database(self):
        """
        Connect to the database and initialize the db variable.
        """
        raise NotImplementedError("implement a connect_to_database function")

    @abstractmethod
    async def register_user(self, usr: User):
        raise NotImplementedError("implement a register user function")

    @abstractmethod
    async def user_exists(self, usr: User):
        raise NotImplementedError("implement a check if its exists")

    @abstractmethod
    async def add_password(self, usr: User, pas: Password):
        raise NotImplementedError("implement add password")

    @abstractmethod
    async def validate_user(self, usr: User):
        raise NotImplementedError("implement a check if its exists")

    @abstractmethod
    async def get_passwords(self, usr: User):
        raise NotImplementedError("implement a check if its exists")
