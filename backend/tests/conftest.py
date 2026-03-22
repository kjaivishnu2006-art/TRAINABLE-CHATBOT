import pytest
import os
import sys

# Ensure backend root is in the path so we can import 'app' and 'services'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def app():
    # Set to testing configuration
    os.environ['FLASK_ENV'] = 'default' 
    app = create_app('default')
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
