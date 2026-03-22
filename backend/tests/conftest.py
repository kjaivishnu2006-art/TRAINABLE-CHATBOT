import pytest
import os
import sys

# Ensure backend root is in the path so we can import 'app' and 'services'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    """Provides a FastAPI test client for endpoint testing."""
    return TestClient(app)
