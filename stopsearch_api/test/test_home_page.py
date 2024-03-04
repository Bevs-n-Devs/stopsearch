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


def test_home_route(test_client):
    endpoint_url = test_client.get("/home")
    response_payload = json.loads(endpoint_url.data)
    
    assert (endpoint_url.status_code == 200), "Expected 200 status code"
    assert (isinstance(response_payload, list)), "Expected object to be a list"
    assert (isinstance(response_payload[0], dict)), "Expected object to be a dictionary"
    
    assert ("App" in response_payload[0]), "Expected App attribute"
    assert ("Instructions" in response_payload[0]), "Expected Instructions attribute"
    assert ("Report Page" in response_payload[0]), "Expected Report Page attribute"
    assert ("Report Questions" in response_payload[0]), "Expected Report Questions attribute"
    assert ("status" in response_payload[1]), "Expected status attribute"
    
    assert (isinstance(response_payload[0]["App"], str)), "Expected App to be a string"
    assert (isinstance(response_payload[0]["Instructions"], str)), "Expected Instructions to be a string"
    assert (isinstance(response_payload[0]["Report Page"], str)), "Expected Report Page to be a string"
    assert (isinstance(response_payload[0]["Report Questions"], list)), "Expected Report Questions to be a list"
    assert (isinstance(response_payload[1]["status"], int)), "Expected status to be an integer"
    
    assert ("FormType" in response_payload[0]["Report Questions"][0]), "Expected FormType attribute"
    assert ("FormDate" in response_payload[0]["Report Questions"][1]), "Expected FormDate attribute"
    assert ("IncidentLocation" in response_payload[0]["Report Questions"][2]), "Expected IncidentLocation attribute"
    assert ("IncidentPostcode" in response_payload[0]["Report Questions"][3]), "Expected IncidentPostcode attribute"
    assert ("SearchReason" in response_payload[0]["Report Questions"][4]), "Expected SearchReason attribute"
    assert ("NumberOfVictims" in response_payload[0]["Report Questions"][5]), "Expected NumberOfVictims attribute"
    assert ("NumberOfPolice" in response_payload[0]["Report Questions"][6]), "Expected NumberOfPolice attribute"
    assert ("TypeOfSearch" in response_payload[0]["Report Questions"][7]), "Expected TypeOfSearch attribute"
    assert ("PoliceOfficerInformation" in response_payload[0]["Report Questions"][8]), "Expected PoliceOfficerInformation attribute"
    assert ("VictimAge" in response_payload[0]["Report Questions"][9]), "Expected VictimAge attribute"
    assert ("VictimGender" in response_payload[0]["Report Questions"][10]), "Expected VictimGender attribute"
    assert ("VictimRace" in response_payload[0]["Report Questions"][11]), "Expected VictimRace attribute"
    assert ("AddNotes" in response_payload[0]["Report Questions"][12]), "Expected AddNotes attribute"
    assert ("ReportEmail" in response_payload[0]["Report Questions"][13]), "Expected ReportEmail attribute"
    
    assert (response_payload[0]["Report Questions"][0]["FormType"], dict), "Expected FortType to be a dictionary"
    assert (response_payload[0]["Report Questions"][0]["FormType"]["0"], str), "Expected FortType to be a string"
    assert (response_payload[0]["Report Questions"][0]["FormType"]["0"] == "victim")
    assert (response_payload[0]["Report Questions"][0]["FormType"]["1"] == "witness")
    
    assert (response_payload[0]["Report Questions"][1]["FormDate"], dict), "Expected FormDate to be a dictionary"
    assert (response_payload[0]["Report Questions"][1]["FormDate"]["0"], str), "Expected FormDate to be a string"
    assert (response_payload[0]["Report Questions"][1]["FormDate"]["0"] == "datime format")
    
    assert (response_payload[0]["Report Questions"][2]["IncidentLocation"], dict), "Expected IncidentLocation to be a dictionary"
    assert (response_payload[0]["Report Questions"][2]["IncidentLocation"]["0"], str), "Expected IncidentLocation to be a string"
    assert (response_payload[0]["Report Questions"][2]["IncidentLocation"]["0"] == "Enter street name and town or city of where the incident occured.")
    
    assert (response_payload[0]["Report Questions"][3]["IncidentPostcode"], dict), "Expected IncidentPostcode to be a dictionary"
    assert (response_payload[0]["Report Questions"][3]["IncidentPostcode"]["0"], str), "Expected IncidentPostcode to be a string"
    assert (response_payload[0]["Report Questions"][3]["IncidentPostcode"]["0"] == "Enter the postcode where the incident occured.")
    
    assert (response_payload[0]["Report Questions"][4]["SearchReason"], dict), "Expected SearchReason to be a dictionary"
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["0"], str), "Expected SearchReason to be a string"
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["0"] == "Unknown")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["1"] == "suspision of drugs")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["2"] == "Carrying a weapon")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["3"] == "Stolen goods")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["4"] == "suspision of committing a crime")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["5"] == "suspision of committing a serious or violent crime")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["6"] == "History of carrying or using a weapon in the past")
    assert (response_payload[0]["Report Questions"][4]["SearchReason"]["7"] == "In a location where crime is high")
    
    assert (response_payload[0]["Report Questions"][5]["NumberOfVictims"], dict), "Expected NumberOfVictims to be a dictionary"
    assert (response_payload[0]["Report Questions"][5]["NumberOfVictims"]["0"], str), "Expected NumberOfVictims to be a string"
    assert (response_payload[0]["Report Questions"][5]["NumberOfVictims"]["0"] == "1")
    assert (response_payload[0]["Report Questions"][5]["NumberOfVictims"]["1"] == "2")
    
    assert (response_payload[0]["Report Questions"][6]["NumberOfPolice"], dict), "Expected NumberOfPolice to be a dictionary"
    assert (response_payload[0]["Report Questions"][6]["NumberOfPolice"]["0"], str), "Expected NumberOfPolice to be a string"
    assert (response_payload[0]["Report Questions"][6]["NumberOfPolice"]["0"] == "1 - 2")
    assert (response_payload[0]["Report Questions"][6]["NumberOfPolice"]["1"] == "3 - 4")
    assert (response_payload[0]["Report Questions"][6]["NumberOfPolice"]["3"] == "6+")
    assert (response_payload[0]["Report Questions"][6]["NumberOfPolice"]["6"] == "Over 20")
    
    assert (response_payload[0]["Report Questions"][7]["TypeOfSearch"], dict), "Expected TypeOfSearch to be a dictionary"
    assert (response_payload[0]["Report Questions"][7]["TypeOfSearch"]["0"], str), "Expected TypeOfSearch to be a string"
    assert (response_payload[0]["Report Questions"][7]["TypeOfSearch"]["0"] == "Unknown")
    assert (response_payload[0]["Report Questions"][7]["TypeOfSearch"]["1"] == "Moderate")
    assert (response_payload[0]["Report Questions"][7]["TypeOfSearch"]["2"] == "Aggressive")
    
    assert (response_payload[0]["Report Questions"][8]["PoliceOfficerInformation"], dict), "Expected PoliceOfficerInformation to be a dictionary"
    assert (response_payload[0]["Report Questions"][8]["PoliceOfficerInformation"]["0"], str), "Expected PoliceOfficerInformation to be a string"
    assert (response_payload[0]["Report Questions"][8]["PoliceOfficerInformation"]["0"] == "Yes")
    assert (response_payload[0]["Report Questions"][8]["PoliceOfficerInformation"]["1"] == "No")
    
    assert (response_payload[0]["Report Questions"][9]["VictimAge"], dict), "Expected VictimAge to be a dictionary"
    assert (response_payload[0]["Report Questions"][9]["VictimAge"]["0"], str), "Expected VictimAge to be a string"
    assert (response_payload[0]["Report Questions"][9]["VictimAge"]["0"] == "15 - 17")
    assert (response_payload[0]["Report Questions"][9]["VictimAge"]["1"] == "18 - 24")
    assert (response_payload[0]["Report Questions"][9]["VictimAge"]["2"] == "25 - 30")
    assert (response_payload[0]["Report Questions"][9]["VictimAge"]["3"] == "31 - 35")
    assert (response_payload[0]["Report Questions"][9]["VictimAge"]["7"] == "50+")
    
    assert (response_payload[0]["Report Questions"][10]["VictimGender"], dict), "Expected VictimGender to be a dictionary"
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["0"], str), "Expected VictimGender to be a string"
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["0"] == "I don't know")
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["1"] == "Male")
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["2"] == "Female")
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["3"] == "Non-binary")
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["4"] == "Trans")
    assert (response_payload[0]["Report Questions"][10]["VictimGender"]["5"] == "A group of mixed genders")
    
    assert (response_payload[0]["Report Questions"][11]["VictimRace"], dict), "Expected VictimRace to be a dictionary"
    assert (response_payload[0]["Report Questions"][11]["VictimRace"]["0"], str), "Expected VictimRace to be a string"
    assert (response_payload[0]["Report Questions"][11]["VictimRace"]["0"] == "Arab")
    assert (response_payload[0]["Report Questions"][11]["VictimRace"]["1"] == "Asian")
    assert (response_payload[0]["Report Questions"][11]["VictimRace"]["2"] == "Black")
    assert (response_payload[0]["Report Questions"][11]["VictimRace"]["3"] == "Mixed race")
    assert (response_payload[0]["Report Questions"][11]["VictimRace"]["4"] == "White")
    
    assert (response_payload[0]["Report Questions"][12]["AddNotes"], dict), "Expected AddNotes to be a dictionary"
    assert (response_payload[0]["Report Questions"][12]["AddNotes"]["0"], str), "Expected AddNotes to be a string"
    assert (response_payload[0]["Report Questions"][12]["AddNotes"]["0"] == "Additional notes goes here if possible")
    
    assert (response_payload[0]["Report Questions"][13]["ReportEmail"], dict), "Expected ReportEmail to be a dictionary"
    assert (response_payload[0]["Report Questions"][13]["ReportEmail"]["0"], str), "Expected ReportEmail to be a string"
    assert (response_payload[0]["Report Questions"][13]["ReportEmail"]["0"] == "An email needs to be entered to validate the report")