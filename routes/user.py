"""The file containing the User route"""
from fastapi import APIRouter

user = APIRouter()


@user.get("/")
async def read_data():
    return {"user": "data"}
