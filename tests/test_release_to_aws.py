from fastapi.testclient import TestClient
from src.release_to_aws import app

def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Release to AWS API!"}

def test_status():
    client = TestClient(app)
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "release-to-aws"}
