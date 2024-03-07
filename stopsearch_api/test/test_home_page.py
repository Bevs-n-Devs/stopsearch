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
    
    assert (isinstance(response_payload, list)), "Expected object to be a list"
    assert (isinstance(response_payload[0], dict)), "Expected object to be a dictionary"
    
    assert ("App" in response_payload[0]), "Expected App attribute"
    assert ("AppPage" in response_payload[0]), "Expected AppPage attribute"
    assert ("Description" in response_payload[0]), "Expected Description attribute"
    assert ("Founder" in response_payload[0]), "Expected Founder attribute"
    assert ("Pages" in response_payload[0]), "Expected Pages attribute"
    assert ("ReportData" in response_payload[0]), "Expected ReportData attribute"
    assert ("Year" in response_payload[0]), "Expected Year attribute"
    
    assert (isinstance(response_payload[0]["App"], str)), "Expected App to be string"
    assert (isinstance(response_payload[0]["AppPage"], str)), "Expected AppPage to be string"
    assert (isinstance(response_payload[0]["Description"], str)), "Expected Description to be string"
    assert (isinstance(response_payload[0]["Founder"], str)), "Expected Founder to be string"
    assert (isinstance(response_payload[0]["Pages"], list)), "Expected Pages to be a list"
    assert (isinstance(response_payload[0]["ReportData"], list)), "Expected ReportData to be a list"
    assert (isinstance(response_payload[0]["Year"], str)), "Expected Year to be a string"
    
    assert ("CreateReport" in response_payload[0]["Pages"][0]), "Expected CreateReport attribute"
    assert ("FindReportByVictim" in response_payload[0]["Pages"][0]), "Expected FindReportByVictim attribute"
    assert ("FindReportByWitness" in response_payload[0]["Pages"][0]), "Expected FindReportByWitness attribute"
    assert ("HomePage" in response_payload[0]["Pages"][0]), "Expected HomePage attribute"
    assert ("Index" in response_payload[0]["Pages"][0]), "Expected Index attribute"
    assert ("Manual" in response_payload[0]["Pages"][0]), "Expected Manual attribute"
    
    assert (response_payload[0]["App"] == "StopSearch UK"), "Expected object to be equal"
    assert (response_payload[0]["AppPage"] == "/home"), "Expected object to be equal"
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
    
    
    # check if ReportData data is the same in payload
    
    
    # check reprt type drop down 
    assert ("FormType" in response_payload[0]["ReportData"][1]), "Expected ReportData attribute"
    assert (isinstance(response_payload[0]["ReportData"][1]["FormType"], list)), "Expected object to be a list"
    assert (response_payload[0]["ReportData"][1]["FormType"][0] == "FormType drop down options"), "Expected object to be equal"
    assert (response_payload[0]["ReportData"][1]["FormType"][1]["0"] == "victim"), "Expected object to be equal"
    assert (response_payload[0]["ReportData"][1]["FormType"][1]["1"] == "witness"), "Expected object to be equal"
    
    # check [optional] date functionality
    assert ("FormDate" in response_payload[0]["ReportData"][2]), "Expected FormDate attribute"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"], list)), "Expected object to be a list"
    assert ("formDate" in response_payload[0]["ReportData"][2]["FormDate"][1]), "Expected formDate attriute"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][1], dict)), "Expected object to be a dictionary"
    assert (response_payload[0]["ReportData"][2]["FormDate"][1]["formDate"] == "date in DateTime format"), "Expected object to be equal"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][1]["formDate"], str)), "Expected formDate to be string"
    assert ("formattedDate" in response_payload[0]["ReportData"][2]["FormDate"][2]), "Expected formattedDate attriute"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"], dict)), "Expected formattedDate to be a dictionary"
    assert ("formDate" in response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]), "Expected formDate attriute"
    assert ("formMonth" in response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]), "Expected formMonth attriute"
    assert ("formYear" in response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]), "Expected formYear attriute"
    assert ("formTime" in response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]), "Expected formTime attriute"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]["formDate"], str)), "Expected formDate to be a string"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]["formMonth"], str)), "Expected formMonth to be a string"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]["formYear"], str)), "Expected formYear to be a string"
    assert (isinstance(response_payload[0]["ReportData"][2]["FormDate"][2]["formattedDate"]["formTime"], str)), "Expected formTime to be a string"
    
    # check [optional] incident location data functionality
    assert ("IncidentLocation" in response_payload[0]["ReportData"][3]), "Expected IncidentLocation attribute"
    assert (isinstance(response_payload[0]["ReportData"][3]["IncidentLocation"], dict)), "Expected IncidentLocation to be a dictionary"
    assert ("automaticAddress" in response_payload[0]["ReportData"][3]["IncidentLocation"]), "Expected automaticAddress attribute"
    assert ("eneterAddress" in response_payload[0]["ReportData"][3]["IncidentLocation"]), "Expected eneterAddress attribute"
    assert ("manualAddress" in response_payload[0]["ReportData"][3]["IncidentLocation"]), "Expected manualAddress attribute"
    assert (isinstance(response_payload[0]["ReportData"][3]["IncidentLocation"]["automaticAddress"], str)), "Expected automaticAddress to be a string"
    assert (isinstance(response_payload[0]["ReportData"][3]["IncidentLocation"]["eneterAddress"], list)), "Expected eneterAddress to be a list"
    assert (isinstance(response_payload[0]["ReportData"][3]["IncidentLocation"]["manualAddress"], list)), "Expected manualAddress to be a list"
    assert ("automaticAddress" in response_payload[0]["ReportData"][3]["IncidentLocation"]["eneterAddress"][1]["0"]), "Expected automaticAddress attribute"
    assert ("manualAddress" in response_payload[0]["ReportData"][3]["IncidentLocation"]["eneterAddress"][1]["1"]), "Expected manualAddress attribute"
    assert (response_payload[0]["ReportData"][3]["IncidentLocation"]["eneterAddress"][1]["0"] == "automaticAddress"), "Expected both obejects to be equal"
    assert (response_payload[0]["ReportData"][3]["IncidentLocation"]["eneterAddress"][1]["1"] == "manualAddress"), "Expected both obejects to be equal"
    assert (response_payload[0]["ReportData"][3]["IncidentLocation"]["manualAddress"][1]["StreetName"] == "Enter street name and town or city of where the incident occured."), "Expected both obejects to be equal"
    assert (response_payload[0]["ReportData"][3]["IncidentLocation"]["manualAddress"][1]["TownOrCity"] == "Enter name of town or city of the incident"), "Expected both obejects to be equal"
    assert (response_payload[0]["ReportData"][3]["IncidentLocation"]["manualAddress"][1]["Postcode"] == "Enter the postcode of the incident"), "Expected both obejects to be equal"
    
    # check search reason drop down
    assert ("SearchReason" in response_payload[0]["ReportData"][4]), "Expected SearchReason attribute"
    assert (isinstance(response_payload[0]["ReportData"][4]["SearchReason"], list)), "Expected SearchReason to be a list"
    assert (response_payload[0]["ReportData"][4]["SearchReason"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][4]["SearchReason"][1]["1"] == "suspision of drugs"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][4]["SearchReason"][1]["2"] == "Carrying a weapon"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][4]["SearchReason"][1]["7"] == "In a location where crime is high"), "Expected both objects to be equal"
    
    # check number of victims drop down
    assert ("NumberOfVictims" in response_payload[0]["ReportData"][5]), "Expected NumberOfVictims attribute"
    assert (isinstance(response_payload[0]["ReportData"][5]["NumberOfVictims"], list)), "Expected NumberOfVictims to be a list"
    assert (response_payload[0]["ReportData"][5]["NumberOfVictims"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][5]["NumberOfVictims"][1]["1"] == "1"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][5]["NumberOfVictims"][1]["2"] == "2"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][5]["NumberOfVictims"][1]["12"] == "15+"), "Expected both objects to be equal"
    
    # check number of police drop down
    assert ("NumberOfPolice" in response_payload[0]["ReportData"][6]), "Expected NumberOfPolice attribute"
    assert (isinstance(response_payload[0]["ReportData"][6]["NumberOfPolice"], list)), "Expected NumberOfPolice to be a list"
    assert (response_payload[0]["ReportData"][6]["NumberOfPolice"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][6]["NumberOfPolice"][1]["1"] == "1 - 2"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][6]["NumberOfPolice"][1]["2"] == "3 - 4"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][6]["NumberOfPolice"][1]["6"] == "15+"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][6]["NumberOfPolice"][1]["7"] == "Over 20"), "Expected both objects to be equal"
    
    # check type of search drop down
    assert ("TypeOfSearch" in response_payload[0]["ReportData"][7]), "Expected TypeOfSearch attribute"
    assert (isinstance(response_payload[0]["ReportData"][7]["TypeOfSearch"], list)), "Expected TypeOfSearch to be a list"
    assert (response_payload[0]["ReportData"][7]["TypeOfSearch"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][7]["TypeOfSearch"][1]["1"] == "Moderate"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][7]["TypeOfSearch"][1]["2"] == "Aggressive"), "Expected both objects to be equal"
    
    # check[optional] police officer information functionality
    assert ("PoliceOfficerInformation" in response_payload[0]["ReportData"][8]), "Expected PoliceOfficerInformation attribute"
    assert ("additionalOfficers" in response_payload[0]["ReportData"][8]), "Expected additionalOfficers attribute"
    assert (isinstance(response_payload[0]["ReportData"][8]["PoliceOfficerInformation"], dict)), "Expected PoliceOfficerInformation to be a dictionary"
    assert (isinstance(response_payload[0]["ReportData"][8]["additionalOfficers"], list)), "Expected additionalOfficers to be a list"
    assert (isinstance(response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["enterPoliceInfo"], list)), "Expected enterPoliceInfo to be a list"
    assert ("PoliceBadgeNumber" in response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["enterPoliceInfo"][1]), "Expetced PoliceBadgeNumber attribute"
    assert ("PoliceOfficerName" in response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["enterPoliceInfo"][1]), "Expetced PoliceOfficerName attribute"
    assert ("PoliceStation" in response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["enterPoliceInfo"][1]), "Expetced PoliceStation attribute"
    assert (isinstance(response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["additionalOfficerData"], list)), "Expected enterPoliceInfo to be a list"
    assert (response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["additionalOfficerData"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][8]["PoliceOfficerInformation"]["additionalOfficerData"][1]["1"] == "additionalOfficers"), "Expected both objects to be equal"
    assert ("PoliceBadgeNumber" in response_payload[0]["ReportData"][8]["additionalOfficers"][1]), "Expected PoliceBadgeNumber attribute"
    assert ("PoliceOfficerName" in response_payload[0]["ReportData"][8]["additionalOfficers"][1]), "Expected PoliceOfficerName attribute"
    assert ("PoliceStation" in response_payload[0]["ReportData"][8]["additionalOfficers"][1]), "Expected PoliceStation attribute"
    
    # check victim age drop down
    assert ("VictimAge" in response_payload[0]["ReportData"][9]), "Expected VictimAge attribute"
    assert (isinstance(response_payload[0]["ReportData"][9]["VictimAge"], list)), "Expected VictimAge to be a list"
    assert (response_payload[0]["ReportData"][9]["VictimAge"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][9]["VictimAge"][1]["1"] == "15 - 17"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][9]["VictimAge"][1]["2"] == "18 - 24"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][9]["VictimAge"][1]["7"] == "45+"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][9]["VictimAge"][1]["8"] == "50+"), "Expected both objects to be equal"
    
    # check victim gender drop down
    assert ("VictimGender" in response_payload[0]["ReportData"][10]), "Expected VictimGender attribute"
    assert (isinstance(response_payload[0]["ReportData"][10]["VictimGender"], list)), "Expected VictimGender to be a list"
    assert (response_payload[0]["ReportData"][10]["VictimGender"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][10]["VictimGender"][1]["1"] == "Male"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][10]["VictimGender"][1]["2"] == "Female"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][10]["VictimGender"][1]["3"] == "Non-binary"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][10]["VictimGender"][1]["4"] == "Trans"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][10]["VictimGender"][1]["5"] == "A group of mixed genders"), "Expected both objects to be equal"
    
    # check victim race drop down
    assert ("VictimRace" in response_payload[0]["ReportData"][11]), "Expected VictimRace attribute"
    assert (isinstance(response_payload[0]["ReportData"][11]["VictimRace"], list)), "Expected VictimRace to be a list"
    assert (response_payload[0]["ReportData"][11]["VictimRace"][1]["0"] == "Unknown"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][11]["VictimRace"][1]["1"] == "Arab"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][11]["VictimRace"][1]["2"] == "Asian"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][11]["VictimRace"][1]["3"] == "Black"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][11]["VictimRace"][1]["4"] == "Mixed race"), "Expected both objects to be equal"
    assert (response_payload[0]["ReportData"][11]["VictimRace"][1]["5"] == "White"), "Expected both objects to be equal"
    
    # check notes [optional] functionality 
    assert ("AddNotes" in response_payload[0]["ReportData"][12]), "Expected AddNotes attribute"
    assert (isinstance(response_payload[0]["ReportData"][12]["AddNotes"], dict)), "Expected object to be a dictionary"
    assert ("additionalNotes" in response_payload[0]["ReportData"][12]["AddNotes"]), "Expected additionalNotes attribute"
    assert (response_payload[0]["ReportData"][12]["AddNotes"]["additionalNotes"][1]["0"] == "No"), "Expected object to be equal"
    assert (response_payload[0]["ReportData"][12]["AddNotes"]["additionalNotes"][1]["1"] == "reportNotes"), "Expected object to be equal"
    assert ("reportNotes" in response_payload[0]["ReportData"][12]["AddNotes"]), "Expected reportNotes attribute"
    assert (response_payload[0]["ReportData"][12]["AddNotes"]["reportNotes"][0]["notes"] == "Additional notes goes here if possible"), "Expected object to be equal"
    
    # check report email
    assert ("ReportEmail" in response_payload[0]["ReportData"][13]), "Expected ReportEmail attribute"
    assert (isinstance(response_payload[0]["ReportData"][13], dict)), "Expected object to be a dictionary"
    assert (isinstance(response_payload[0]["ReportData"][13]["ReportEmail"], list)), "Expected ReportEmail key to be a list"
    assert ("reportEmail" in response_payload[0]["ReportData"][13]["ReportEmail"][1]), "Expected reportEmail attribute"
    assert (response_payload[0]["ReportData"][13]["ReportEmail"][1]["reportEmail"] == "An email needs to be entered to validate the report"), "Expected object to be equal"