"""The file containing the User route"""
from fastapi import APIRouter
from config.db import connection
from models.index import users

user = APIRouter()


@user.get("/")
async def read_data():
    return connection.execute(users.select()).fetchall()
