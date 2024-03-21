from abc import ABC, abstractmethod
from models.models import User

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
