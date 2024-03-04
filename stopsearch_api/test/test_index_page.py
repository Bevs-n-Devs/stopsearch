import os
import requests
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


def test_index_route(test_client):
    endpoint_url = test_client.get('/')
    # Decode bytes and parse JSON
    response_payload = json.loads(endpoint_url.data)
    
    print(type(response_payload))
    print(response_payload)
    
    assert (endpoint_url.status_code == 200), "Expected 200 status code"
    assert (isinstance(response_payload, list)), "Expected object to be a list"
    assert (isinstance(response_payload[0], dict)), "Expected object to be a dictionary"
    
    assert ("app" in response_payload[0]), "Expected app attribute"
    assert ("description" in response_payload[0]), "Expected description attribute"
    assert ("founder" in response_payload[0]), "Expected founder attribute"
    assert ("pages" in response_payload[0]), "Expectd pages attribute"
    assert ("year" in response_payload[0]), "Expectd year attribute"
    assert ("status" in response_payload[1]), "Expected status attribute"
    
    assert (isinstance(response_payload[0]["app"], str)), "Expected app to be a string"
    assert (isinstance(response_payload[0]["description"], str)), "Expected description to be a string"
    assert (isinstance(response_payload[0]["founder"], str)), "Expected founder to be a string"
    assert (isinstance(response_payload[0]["pages"], dict)), "Expected pages to be a dictionary"
    assert (isinstance(response_payload[0]["year"], str)), "Expected year to be a string"
    assert (isinstance(response_payload[1]["status"], int)), "Expected status to be an integer"
    
    assert ("Guide / Manual" in response_payload[0]["pages"]), "Expected Guide / Manual attribute"
    assert ("Home Page" in response_payload[0]["pages"]), "Expected Home Page attribute"
    assert ("Introduction" in response_payload[0]["pages"]), "Expected Introduction attribute"
    
    assert (response_payload[0]["app"] == "Stop Search UK"), "Expected app attribute to be equal to \'Stop Search UK\'"
    assert (response_payload[0]["founder"] == "Akoto Tech"), "Expected founder attribute to be equal to \'Akoto Tech\'"
    assert (response_payload[0]["year"] == "2024"), "Expected year attribute to be equal to \'2024\'"