"""The entry point for the project"""
from fastapi import FastAPI
from routes.index import user


app = FastAPI()

print(user)

app.include_router(user)
