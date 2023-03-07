"""The entry point for the project"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def sample_endpoint():
    """A simple endpoint for testing purposes

    Returns:
        Object: Sample data
    """
    return {"Hello": "World"}
