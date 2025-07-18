import pytest
from fastapi.testclient import TestClient
from src.release_to_aws import app


@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(app)
