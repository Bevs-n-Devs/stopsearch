import json
import pytest
from main import app

# this creates a test client of the StopSearch API
@pytest.fixture
def init_test_app():
    with app.app_context():
        return app


@pytest.fixture
def test_client(init_test_app):
    with init_test_app.app_context():
        return init_test_app.test_client()
    
    
def test_manual_route(test_client):
    endpoint_url = test_client.get("/docs")
    response_payload = json.loads(endpoint_url.data)
    
    assert (endpoint_url.status_code == 200), "Expected 200 status code"
    assert (isinstance(response_payload, list)), "Expected object to be a list"
    assert (isinstance(response_payload[0], dict)), "Expected object to be a dictionary"
    
    assert ("App" in response_payload[0]), "Expected App attribute"
    assert ("Description" in response_payload[0]), "Expected Description attribute"
    assert ("Find Report By" in response_payload[0]), "Expected Find Report By attribute"
    assert ("status" in response_payload[1]), "Expected status attribute"
    
    assert (isinstance(response_payload[0]["App"], str)), "Expected App to be a string"
    assert (isinstance(response_payload[0]["Description"], str)), "Expected Description to be a string"
    assert (isinstance(response_payload[0]["Find Report By"], dict)), "Expected Description to be a dictionary"
    assert (isinstance(response_payload[1]["status"], int)), "Expected status to be an integer"
    