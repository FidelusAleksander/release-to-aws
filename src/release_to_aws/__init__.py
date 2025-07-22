from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Release to AWS API!"}


# New useful endpoint for testing
@app.get("/status")
async def status():
    return {"status": "ok", "service": "release-to-aws"}


# Dummy endpoint for testing purposes
@app.get("/dummy")
async def dummy():
    return {"message": "This is a dummy endpoint", "data": {"id": 123, "name": "test"}}
