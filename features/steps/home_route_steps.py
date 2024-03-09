import json
from main import app
from behave import given, when, then

@given("the Home route is running")
def home_route_client(context):
    with app.app_context():
        context.client = app.test_client()

@when("a request is made to the Home route")
def home_route_request(context):
    with app.app_context():
        context.endpoint_url = "/home"
        context.http_response = context.client.get(context.endpoint_url)

@then("the ReportData should be in the response")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[3]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["ReportData"], list)), "Expected object to be a list"
        assert (isinstance(response_payload["ReportData"][0], dict)), "Expected object to be a dictionary"
        
        assert ("FormType" in response_payload["ReportData"][0]), "Expoected FormType in payload"
        assert ("FormDate" in response_payload["ReportData"][1]), "Expoected FormDate in payload"
        assert ("IncidentLocation" in response_payload["ReportData"][2]), "Expoected IncidentLocation in payload"
        assert ("SearchReason" in response_payload["ReportData"][3]), "Expoected SearchReason in payload"
        assert ("NumberOfVictims" in response_payload["ReportData"][4]), "Expoected NumberOfVictims in payload"
        assert ("PoliceInformation" in response_payload["ReportData"][5]), "Expoected PoliceInformation in payload"
        assert ("VictimAge" in response_payload["ReportData"][6]), "Expoected VictimAge in payload"
        assert ("VictimGender" in response_payload["ReportData"][7]), "Expoected VictimGender in payload"
        assert ("VictimRace" in response_payload["ReportData"][8]), "Expoected VictimRace in payload"
        assert ("AddNotes" in response_payload["ReportData"][9]), "Expoected AddNotes in payload"
        assert ("ReportEmail" in response_payload["ReportData"][10]), "Expoected ReportEmail in payload"
        
        assert (isinstance(response_payload["ReportData"][0]["FormType"], list)), "Expected FormType to be a list"
        assert (isinstance(response_payload["ReportData"][1]["FormDate"], list)), "Expected FormDate to be a list"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"], list)), "Expected IncidentLocation to be a list"
        assert (isinstance(response_payload["ReportData"][3]["SearchReason"], list)), "Expected SearchReason to be a list"
        assert (isinstance(response_payload["ReportData"][4]["NumberOfVictims"], list)), "Expected NumberOfVictims to be a list"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"], list)), "Expected PoliceInformation to be a list"
        assert (isinstance(response_payload["ReportData"][6]["VictimAge"], list)), "Expected VictimAge to be a list"
        assert (isinstance(response_payload["ReportData"][7]["VictimGender"], list)), "Expected VictimGender to be a list"
        assert (isinstance(response_payload["ReportData"][8]["VictimRace"], list)), "Expected VictimRace to be a list"
        assert (isinstance(response_payload["ReportData"][9]["AddNotes"], list)), "Expected AddNotes to be a list"
        assert (isinstance(response_payload["ReportData"][10]["ReportEmail"], list)), "Expected ReportEmail to be a list"
        
        # check FormType drop down options
        assert (response_payload["ReportData"][0]["FormType"][0] == "FormType drop down options"), "Expected both objects to be equal"
        assert (response_payload["ReportData"][0]["FormType"][1]["0"] == "victim"), "Expected both objects to be equal"
        assert (response_payload["ReportData"][0]["FormType"][1]["1"] == "witness"), "Expected both objects to be equal"
        
        # check FormDate drop down options
        assert (response_payload["ReportData"][1]["FormDate"][0] == "FormDate drop down options"), "Expected 'FormDate drop down options' to be equal"
        assert (response_payload["ReportData"][1]["FormDate"][1]["formDate"] == "date in DateTime format"), "Expected 'date in DateTime format' to be equal"
        assert (response_payload["ReportData"][1]["FormDate"][2]["formattedDate"]["formDate"] == "Date in verbose format: 1st - 31st"), "Expected 'Date in verbose format: 1st - 31st' to be equal"
        assert (response_payload["ReportData"][1]["FormDate"][2]["formattedDate"]["formMonth"] == "Month in a verbose format January: - December"), "Expected 'Month in a verbose format January: - December' to be equal"
        assert (response_payload["ReportData"][1]["FormDate"][2]["formattedDate"]["formTime"] == "Time of when inicent occured"), "Expected 'Time of when inicent occured' to be equal"
        assert (response_payload["ReportData"][1]["FormDate"][2]["formattedDate"]["formYear"] == "Full format of year: 2024"), "Expected 'Full format of year: 2024' to be equal"
        
        # check IncidentLocation functionality
        assert (response_payload["ReportData"][2]["IncidentLocation"][0] == "Automatically obtain the users address from their phones IP address"), "Expected Automatically obtain the users address from their phones IP address to be equal"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"], list)), "Expected IncidentLocation to be a list"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"][1], dict)), "Expected object to be a dictionary"
        
        assert (response_payload["ReportData"][2]["IncidentLocation"][1]["addressOptions"][0] == "addressOptions drop down options"), "Expected 'addressOptions drop down options' to be equal"
        assert ("addressOptions" in response_payload["ReportData"][2]["IncidentLocation"][1]), "Expected addressOptions attribute"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"][1]["addressOptions"], list)), "Expected addressOptions to be a list"
        assert (response_payload["ReportData"][2]["IncidentLocation"][1]["addressOptions"][1]["0"] == "automaticAddress"), "Expected 'automaticAddress' to be equal"
        assert (response_payload["ReportData"][2]["IncidentLocation"][1]["addressOptions"][1]["1"] == "manualAddress"), "Expected 'manualAddress' to be equal"
        
        assert (response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][0] == "Manually enter the address of the incident"), "Expected 'Manually enter the address of the incident' to be equal"
        assert ("manualAddress" in response_payload["ReportData"][2]["IncidentLocation"][2]), "Expected manualAddress attribute"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"], list)), "Expected manualAddress to be a list"
        assert ("StreetName" in response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][1]), "Expected StreetName attribute"
        assert ("TownOrCity" in response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][1]), "Expected TownOrCity attribute"
        assert ("Postcode" in response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][1]), "Expected Postcode attribute"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][1]["StreetName"], str)), "Expected StreetName to be a string"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][1]["TownOrCity"], str)), "Expected TownOrCity to be a string"
        assert (isinstance(response_payload["ReportData"][2]["IncidentLocation"][2]["manualAddress"][1]["Postcode"], str)), "Expected Postcode to be a string"
        
        # check SearchReason drop down options
        assert (response_payload["ReportData"][3]["SearchReason"][0] == "SearchReason drop down options"), "Expected 'SearchReason drop down options' to be equal"
        assert (response_payload["ReportData"][3]["SearchReason"][1]["0"] == "Unknown"), "Expected 'Unknown' to be equal"
        assert (response_payload["ReportData"][3]["SearchReason"][1]["1"] == "suspision of drugs"), "Expected 'suspision of drugs' to be equal"
        assert (response_payload["ReportData"][3]["SearchReason"][1]["2"] == "Carrying a weapon"), "Expected 'Carrying a weapon' to be equal"
        assert (response_payload["ReportData"][3]["SearchReason"][1]["6"] == "History of carrying or using a weapon in the past"), "Expected 'History of carrying or using a weapon in the past' to be equal"
        assert (response_payload["ReportData"][3]["SearchReason"][1]["7"] == "In a location where crime is high"), "Expected 'In a location where crime is high' to be equal"
        
        # check NumberOfVictims drop down options
        assert (response_payload["ReportData"][4]["NumberOfVictims"][0] == "NumberOfVictims drop down options"), "Expected 'NumberOfVictims drop down options' to be equal"
        assert (isinstance(response_payload["ReportData"][4]["NumberOfVictims"][1], dict)), "Expected object to be a dictionary"
        assert (response_payload["ReportData"][4]["NumberOfVictims"][1]["0"] == "Unknown"), "Expected 'Unknown' to be equal"
        assert (response_payload["ReportData"][4]["NumberOfVictims"][1]["1"] == "1"), "Expected '1' to be equal"
        assert (response_payload["ReportData"][4]["NumberOfVictims"][1]["2"] == "2"), "Expected '2' to be equal"
        assert (response_payload["ReportData"][4]["NumberOfVictims"][1]["11"] == "10+"), "Expected '10+' to be equal"
        assert (response_payload["ReportData"][4]["NumberOfVictims"][1]["12"] == "15+"), "Expected '15+' to be equal"
        
        # check PoliceInformation functionality
        assert (response_payload["ReportData"][5]["PoliceInformation"][0] == "Infomration on the police officers and their conduct at the scene of the incident"), "Expected 'Infomration on the police officers and their conduct at the scene of the incident' to be equal"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"], list)), "Expected PoliceInformation object to be a list"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][1], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][2], dict)), "Expected object to be a dictionary"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3], dict)), "Expected object to be a dictionary"
        
        assert ("NumberOfPolice" in response_payload["ReportData"][5]["PoliceInformation"][1]), "Expected NumberOfPolice attribute"
        assert ("TypeOfSearch" in response_payload["ReportData"][5]["PoliceInformation"][2]), "Expected TypeOfSearch attribute"
        assert ("PoliceOfficerInformation" in response_payload["ReportData"][5]["PoliceInformation"][3]), "Expected PoliceOfficerInformation attribute"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"], list)), "Expected NumberOfPolice to be a list"
        assert (response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"][0] == "NumberOfPolice drop down options"), "Expected 'NumberOfPolice drop down options' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"][1]["0"] == "Unknown"), "Expected 'Unknown' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"][1]["1"] == "1 - 2"), "Expected '1 - 2' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"][1]["2"] == "3 - 4"), "Expected '3 - 4' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"][1]["6"] == "15+"), "Expected '15+' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][1]["NumberOfPolice"][1]["7"] == "Over 20"), "Expected 'Over 20' to be equal"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][2]["TypeOfSearch"], list)), "Expected TypeOfSearch to be a list"
        assert (response_payload["ReportData"][5]["PoliceInformation"][2]["TypeOfSearch"][0] == "TypeOfSearch drop down options"), "Expected 'TypeOfSearch drop down options' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][2]["TypeOfSearch"][1]["0"] == "Unknown"), "Expected 'Unknown' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][2]["TypeOfSearch"][1]["1"] == "Moderate"), "Expected 'Moderate' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][2]["TypeOfSearch"][1]["2"] == "Aggressive"), "Expected 'Aggressive' to be equal"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"], list)), "Expected PoliceOfficerInformation to be a list"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][0] == "Functionality to record single or multiple police officers"), "Expected 'Functionality to record single or multiple police officers' to be equal"
        
        assert ("additionalOfficerData" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1]), "Expected additionalOfficerData attribute"
        assert ("Unknown" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][2]), "Expected Unknown attribute"
        assert ("enterPoliceInfo" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]), "Expected enterPoliceInfo attribute"
        assert ("additionalOfficers" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]), "Expected additionalOfficers attribute"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1], dict)), "Expected object to be a dictionary"
        assert ("additionalOfficerData" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1]), "Expected addittionalOfficerData attribute"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1]["additionalOfficerData"], list)), "Expected additionalOfficers to be a list"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1]["additionalOfficerData"][0] == "additionalOfficerData drop down options"), "Expected 'additionalOfficerData drop down options' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1]["additionalOfficerData"][1]["0"] == "Unknown"), "Expected 'Unknown' to be equal"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][1]["additionalOfficerData"][1]["1"] == "additionalOfficers"), "Expected 'additionalOfficers' to be equal"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][2], dict)), "Expected object to be a dictionary"
        assert ("Unknown" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][2]), "Expected Unknown attribute"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][2]["Unknown"] == "Leave additionalOfficers empty"), "Expected 'Leave additionalOfficers empty' to be equal"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3], dict)), "Expected object to be a dictionary"
        assert ("enterPoliceInfo" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]),"Expected enterPoliceInfo attribute"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"], list)), "Expected PoliceOfficerInformation to be a list"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][0] == "Enter the police officer's badge number, name & station"), "Expected 'Enter the police officer\'s badge number, name & station' to be equal"
        
        assert ("PoliceBadgeNumber" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][1]), "Expected PoliceBadgeNumber attribute"
        assert ("PoliceOfficerName" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][1]), "Expected PoliceOfficerName attribute"
        assert ("PoliceStation" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][1]), "Expected PoliceStation attribute"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][1]["PoliceBadgeNumber"], str)), "Expected PoliceBadgeNumber to be a string"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][1]["PoliceOfficerName"], str)), "Expected PoliceOfficerName to be a string"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][3]["enterPoliceInfo"][1]["PoliceStation"], str)), "Expected PoliceStation to be a string"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4], dict)), "Expected object to be a dictionary"
        assert ("additionalOfficers" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]),"Expected enterPoliceInfo attribute"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"], list)), "Expected additionalOfficers to be a list"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1], dict)), "Expected additionalOfficers object to be a dictionary"
        assert (response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][0] == "Any additional police officer data is extended to enterPoliceInfo list"), "Expected 'Any additional police officer data is extended to enterPoliceInfo list' to be equal"
        
        assert ("PoliceBadgeNumber" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1]), "Expected PoliceBadgeNumber attribute"
        assert ("PoliceOfficerName" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1]), "Expected PoliceOfficerName attribute"
        assert ("PoliceStation" in response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1]), "Expected PoliceStation attribute"
        
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1]["PoliceBadgeNumber"], str)), "Expected PoliceBadgeNumber to be a string"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1]["PoliceOfficerName"], str)), "Expected PoliceOfficerName to be a string"
        assert (isinstance(response_payload["ReportData"][5]["PoliceInformation"][3]["PoliceOfficerInformation"][4]["additionalOfficers"][1]["PoliceStation"], str)), "Expected PoliceStation to be a string"
        
        # check VictimAge drop down options
        assert (response_payload["ReportData"][6]["VictimAge"][0] == "VictimAge drop down options"), "Expected 'VictimAge drop down options' to be equal"
        assert (response_payload["ReportData"][6]["VictimAge"][1]["0"] == "Unknown"), "Expected 'Unkown' to be equal"
        assert (response_payload["ReportData"][6]["VictimAge"][1]["1"] == "15 - 17"), "Expected '15 - 17' to be equal"
        assert (response_payload["ReportData"][6]["VictimAge"][1]["2"] == "18 - 24"), "Expected '18 - 24' to be equal"
        assert (response_payload["ReportData"][6]["VictimAge"][1]["7"] == "45+"), "Expected '45+' to be equal"
        assert (response_payload["ReportData"][6]["VictimAge"][1]["8"] == "50+"), "Expected '50+' to be equal"
        
        # check VictimGender drop down options
        assert (response_payload["ReportData"][7]["VictimGender"][0] == "VictimGender drop down options"), "Expected 'VictimGender drop down options' to be equal"
        assert (response_payload["ReportData"][7]["VictimGender"][1]["0"] == "Unknown"), "Expected 'Unkown' to be equal"
        assert (response_payload["ReportData"][7]["VictimGender"][1]["1"] == "Male"), "Expected 'Male' to be equal"
        assert (response_payload["ReportData"][7]["VictimGender"][1]["4"] == "Trans"), "Expected 'Trans' to be equal"
        assert (response_payload["ReportData"][7]["VictimGender"][1]["5"] == "A group of mixed genders"), "Expected 'A group of mixed genders' to be equal"
        
        # check VictimRace drop down options
        assert (response_payload["ReportData"][8]["VictimRace"][0] == "VictimRace drop down options"), "Expected 'VictimRace drop down options' to be equal"
        assert (response_payload["ReportData"][8]["VictimRace"][1]["0"] == "Unknown"), "Expected 'Unkown' to be equal"
        assert (response_payload["ReportData"][8]["VictimRace"][1]["1"] == "Arab"), "Expected 'Arab' to be equal"
        assert (response_payload["ReportData"][8]["VictimRace"][1]["4"] == "Mixed race"), "Expected 'Mixed race' to be equal"
        assert (response_payload["ReportData"][8]["VictimRace"][1]["5"] == "White"), "Expected 'White' to be equal"
        
        # check AddNotes functionality
        assert (response_payload["ReportData"][9]["AddNotes"][0] == "Option to add additional notes to the report"), "Expected 'Option to add additional notes to the report' to be equal"
        
        assert ("reportNotes" in response_payload["ReportData"][9]["AddNotes"][1]), "Expected reportNotes attribute"
        assert (isinstance(response_payload["ReportData"][9]["AddNotes"][1]["reportNotes"], list)), "Expected reportNotes to be a list"
        assert (isinstance(response_payload["ReportData"][9]["AddNotes"][1]["reportNotes"][0], dict)), "Expected reportNotes object to be a dictionary"
        assert ("notes" in response_payload["ReportData"][9]["AddNotes"][1]["reportNotes"][0]), "Expected notes attribute"
        assert (isinstance(response_payload["ReportData"][9]["AddNotes"][1]["reportNotes"][0]["notes"], str)), "Expected notes to be a string"
        
        
        assert ("additionalNotes" in response_payload["ReportData"][9]["AddNotes"][2]), "Expected additionalNotes attribute"
        assert (isinstance(response_payload["ReportData"][9]["AddNotes"][2]["additionalNotes"], list)), "Expected additionalNotes to be a list"
        assert (response_payload["ReportData"][9]["AddNotes"][2]["additionalNotes"][0] == "additionalNotes drop down options"), "Expected 'additionalNotes drop down options' to be equal"
        assert (response_payload["ReportData"][9]["AddNotes"][2]["additionalNotes"][1]["0"] == "No"), "Expected 'No' to be equal"
        assert (response_payload["ReportData"][9]["AddNotes"][2]["additionalNotes"][1]["1"] == "reportNotes"), "Expected 'reportNotes' to be equal"
        
        
        # check ReportEmail validtion funtionality
        assert (response_payload["ReportData"][10]["ReportEmail"][0] == "User must enter their email to validate the report"), "Expected 'User must enter their email to validate the report' to be equal"
        assert (isinstance(response_payload["ReportData"][10]["ReportEmail"][1], dict)), "Expected ReportEmail objeect to be a dictionary"
        assert ("reportEmail" in response_payload["ReportData"][10]["ReportEmail"][1]), "Expected ReportEmail attribute"
        assert (isinstance(response_payload["ReportData"][10]["ReportEmail"][1]["reportEmail"], str)), "Expected reportEmail to be a string"