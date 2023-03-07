"""The entry point for the project"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def sample_endpoint():
    return {"Hello": "World"}
