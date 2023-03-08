"""The file containing the User route"""
from fastapi import APIRouter

from config.db import connection
from models.index import users
from schemas.index import User

user = APIRouter()


@user.get("/")
async def read_data():
    """The root endpoint for the users

    Returns:
        connection data: The result of a db query
    """
    return connection.execute(users.select()).fetchall()


@user.get("/{id}")
async def read_data_with_id(_id: int):
    """Reading the data of a specific user with the given id

    Args:
        id (int): The id of the user

    Returns:
        Query Result: THe result of the executed query
    """
    return connection.execute(users.select().where(users.c.id == _id)).fetchall()


@user.post('/')
async def write_data(_user: User):
    """A function to write data to teh database

    Args:
        user (User): User data based on the User template

    Returns:
        Query Result: Returns the result of the executed SQL query
    """
    connection.execute(users.insert().values(
        name=_user.name,
        email=_user.email,
        password=_user.password
    )).fetchall()

    return connection.execute(users.select()).fetchall()


@user.put('/{id}')
async def update_data(_id: int, _user: User):
    """A function that acts as the logic for the update endpoint

    Args:
        _id (int): The identifier for the user
        _user (User): The User data in a predefined template

    Returns:
        Query Result: Returns the result of a sql query
    """
    connection.execute(users.update().values(
        name=_user.name,
        email=_user.email,
        password=_user.password
    ).where(users.c.id == _id)).fetchall()

    return connection.execute(users.select()).fetchall()
