from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Release to AWS API!"}


# New useful endpoint for testing
@app.get("/status")
async def status():
    return {"status": "false", "service": "release-to-aws"}
