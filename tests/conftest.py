import pytest
from copy import deepcopy
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to known state before each test"""
    original = deepcopy(activities)
    yield
    # Reset after test
    activities.clear()
    activities.update(original)
