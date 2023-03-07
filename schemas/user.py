"""The user schema file"""
from pydantic import BaseModel


class User(BaseModel):
    """The template for the user data

    Args:
        BaseModel (Parent class): The User class inherits the BaseModel class
    """
    id: int
    name: str
    email: str
    password: str
