"""The user schema file"""
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
