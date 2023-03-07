"""The file containing the User route"""
from fastapi import APIRouter
from config.db import connection
from models.index import users

user = APIRouter()


@user.get("/")
async def read_data():
    """The root endpoint for the users

    Returns:
        connection data: The result of a db query
    """
    return connection.execute(users.select()).fetchall()


@user.get("/{id}")
async def read_data_with_id(id: int):
    """Reading the data of a specific user with the given id

    Args:
        id (int): The id of the user

    Returns:
        Query Result: THe result of the executed query
    """
    return connection.execute(users.select().where(users.c.id == id)).fetchall()
