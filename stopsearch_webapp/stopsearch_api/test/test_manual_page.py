import json
import pytest
from stopsearch_webapp import app

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
    
    assert (isinstance(response_payload, list)), "Expected object to be a list"
    assert (isinstance(response_payload[0], dict)), "Expected object to be a dictionary"
    
    assert ("App" in response_payload[0]), "Expected App attribute"
    assert ("AppPage" in response_payload[0]), "Expected AppPage attribute"
    assert ("Description" in response_payload[0]), "Expected Description attribute"
    assert ("Founder" in response_payload[0]), "Expected Founder attribute"
    assert ("Pages" in response_payload[0]), "Expected Pages attribute"
    assert ("Year" in response_payload[0]), "Expected Year attribute"
    
    assert (isinstance(response_payload[0]["App"], str)), "Expected App to be string"
    assert (isinstance(response_payload[0]["AppPage"], str)), "Expected AppPage to be string"
    assert (isinstance(response_payload[0]["Description"], str)), "Expected Description to be string"
    assert (isinstance(response_payload[0]["Founder"], str)), "Expected Founder to be string"
    assert (isinstance(response_payload[0]["Pages"], list)), "Expected Pages to be a list"
    assert (isinstance(response_payload[0]["Year"], str)), "Expected Year to be a string"
    
    assert ("CreateReport" in response_payload[0]["Pages"][0]), "Expected CreateReport attribute"
    assert ("FindReportByVictim" in response_payload[0]["Pages"][0]), "Expected FindReportByVictim attribute"
    assert ("FindReportByWitness" in response_payload[0]["Pages"][0]), "Expected FindReportByWitness attribute"
    assert ("HomePage" in response_payload[0]["Pages"][0]), "Expected HomePage attribute"
    assert ("Index" in response_payload[0]["Pages"][0]), "Expected Index attribute"
    assert ("Manual" in response_payload[0]["Pages"][0]), "Expected Manual attribute"
    
    assert (response_payload[0]["App"] == "StopSearch UK"), "Expected object to be equal"
    assert (response_payload[0]["AppPage"] == "/docs"), "Expected object to be equal"
    assert (response_payload[0]["Description"] == "An app developed to record and report incidents between the police and the public."), "Expected object to be equal"
    assert (response_payload[0]["Founder"] == "Daniella Rose + Akoto Tech"), "Expected object to be equal"
    assert (response_payload[0]["Year"] == "2024"), "Expected object to be equal"
    
    assert (isinstance(response_payload[0]["Pages"][0]["CreateReport"], str)), "Expected CreateReport to be a string"
    assert (isinstance(response_payload[0]["Pages"][0]["FindReportByVictim"], str)), "Expected FindReportByVictim to be a string"
    assert (isinstance(response_payload[0]["Pages"][0]["FindReportByWitness"], str)), "Expected FindReportByWitness to be a string"
    assert (isinstance(response_payload[0]["Pages"][0]["HomePage"], str)), "Expected HomePage to be a string"
    assert (isinstance(response_payload[0]["Pages"][0]["Index"], str)), "Expected Index to be a string"
    assert (isinstance(response_payload[0]["Pages"][0]["Manual"], str)), "Expected Manual to be a string"
    
    assert (response_payload[0]["Pages"][0]["CreateReport"] == "/create/report/"), "Expected object to be equal"
    assert (response_payload[0]["Pages"][0]["FindReportByVictim"] == "/find/by/victim"), "Expected object to be equal"
    assert (response_payload[0]["Pages"][0]["FindReportByWitness"] == "/find/by/witness"), "Expected object to be equal"
    assert (response_payload[0]["Pages"][0]["HomePage"] == "/home"), "Expected object to be equal"
    assert (response_payload[0]["Pages"][0]["Index"] == "/"), "Expected object to be equal"
    assert (response_payload[0]["Pages"][0]["Manual"] == "/docs"), "Expected object to be equal"
    
    assert ("status" in response_payload[1]), "Expected status attribute"
    assert (isinstance(response_payload[1], dict)), "Expected status to be a dictionary"
    assert (isinstance(response_payload[1]["status"], int)), "Expected status to be an integer"
    assert (response_payload[1]["status"] == 200), "Expected object to be equal"