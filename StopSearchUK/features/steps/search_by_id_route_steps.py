import json
from main import app
from behave import given, when, then

@given("the SearchByID route is running")
def step_impl(context):
    with app.app_context():
        context.client = app.test_client()

@when("a request is made to the SearchByID route with dataID: {data_id: d}")
def step_impl(context, data_id):
    with app.app_context():
        context.endpoint_url = f"/search/{data_id}"
        context.http_response = context.client.get(context.endpoint_url)

@then("the Results should be in the response.")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[3]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected response_payload object to be a dictionary"
        
        assert ("Results" in response_payload), "Expected Results attribute"
        assert (isinstance(response_payload["Results"], list)), "Expected Results to be a list"
        
    
@then("the ReportEmail data object should be in the Results response payload in the expectd format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]
        
        assert (isinstance(response_payload, dict)), "Expected response_payload object to be a dictionary"
        assert ("ReportEmail" in response_payload["Results"][0]), "Expected ReportEmail attribute"
        assert (isinstance(response_payload["Results"][0]["ReportEmail"], list)), "Expected ReportEmail to be a list"
        assert (isinstance(response_payload["Results"][0]["ReportEmail"][0], dict)), "Expectd object to be a dictionary"
        
        assert ("dataID" in response_payload["Results"][0]["ReportEmail"][0]), "Expected dataID attribute"
        assert ("confirmEmail" in response_payload["Results"][0]["ReportEmail"][0]), "Expected confirmEmail attribute"
        assert ("formType" in response_payload["Results"][0]["ReportEmail"][0]), "Expected formType attribute"
        assert ("formmatedDate" in response_payload["Results"][0]["ReportEmail"][0]), "Expected formmatedDate attribute"
        
        assert (isinstance(response_payload["Results"][0]["ReportEmail"][0]["dataID"], int)), "Expected dataID to be an integer"
        assert (isinstance(response_payload["Results"][0]["ReportEmail"][0]["confirmEmail"], str)), "Expected confirmEmail to be a string"
        assert (isinstance(response_payload["Results"][0]["ReportEmail"][0]["formType"], str)), "Expected formType to be a string"
        assert (isinstance(response_payload["Results"][0]["ReportEmail"][0]["formmatedDate"], str)), "Expected formmatedDate to be a string"

@then("the VictimInformation data object should be in the Results response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]
        
        assert (isinstance(response_payload, dict)), "Expected response_payload object to be a dictionary"
        assert ("VictimInformation" in response_payload["Results"][0]), "Expected VictimInformation attribute"
        assert (isinstance(response_payload["Results"][0]["VictimInformation"], list)), "Expected object to be a list"
        assert (isinstance(response_payload["Results"][0]["VictimInformation"][0], dict)), "Expected object to be a dictionary"
        
        assert ("numberOfVictims" in response_payload["Results"][0]["VictimInformation"][0]), "Expected numberOfVictims attribute"
        assert ("victimAge" in response_payload["Results"][0]["VictimInformation"][0]), "Expected victimAge attribute"
        assert ("victimGender" in response_payload["Results"][0]["VictimInformation"][0]), "Expected victimGender attribute"
        assert ("victimRace" in response_payload["Results"][0]["VictimInformation"][0]), "Expected victimRace attribute"
        
        assert (isinstance(response_payload["Results"][0]["VictimInformation"][0]["numberOfVictims"], str)), "Expected numberOfVictims to be a string"
        assert (isinstance(response_payload["Results"][0]["VictimInformation"][0]["victimAge"], str)), "Expected victimAge to be a string"
        assert (isinstance(response_payload["Results"][0]["VictimInformation"][0]["victimGender"], str)), "Expected victimGender to be a string"
        assert (isinstance(response_payload["Results"][0]["VictimInformation"][0]["victimRace"], str)), "Expected victimRace to be a string"


@then("the PolicePublicRelations data object should be in the Results response payload in the expectd format.")
def step_imp(context):
    with app.app_context():
        response_payload = context.response_payload[3]
        
        assert (isinstance(response_payload, dict)), "Expected response_payload object to be a dictionary"
        assert ("PolicePublicRelations" in response_payload["Results"][0]), "Expected PolicePublicRelations attribute"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"], list)), "Expected object to be a list"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0], dict)), "Expected object to be a dict"
        
        assert ("typeOfSearch" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected typeOfSearch attribute"
        assert ("searchReason" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected searchReason attribute"
        assert ("incidentTownOrCity" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected incidentTownOrCity attribute"
        assert ("incidentStreetName" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected incidentStreetName attribute"
        assert ("incidentPostcode" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected incidentPostcode attribute"
        assert ("incidentCountry" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected incidentCountry attribute"
        assert ("additionalNotes" in response_payload["Results"][0]["PolicePublicRelations"][0]), "Expected additionalNotes attribute"
        
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["typeOfSearch"], str)), "Expected typeOfSearch to be a string"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["searchReason"], str)), "Expected searchReason to be a string"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["incidentTownOrCity"], str)), "Expected incidentTownOrCity to be a string"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["incidentStreetName"], str)), "Expected incidentStreetName to be a string"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["incidentPostcode"], str)), "Expected incidentPostcode to be a string"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["incidentCountry"], str)), "Expected incidentCountry to be a string"
        assert (isinstance(response_payload["Results"][0]["PolicePublicRelations"][0]["additionalNotes"], str)), "Expected additionalNotes to be a string"


@then("the PoliceInformation data object should be in the Results response payload in the expectd format.")
def step_impl(context):
    with app.app_context():
        response_payload = context.response_payload[3]
        
        assert (isinstance(response_payload, dict)), "Expected response_payload object to be a dictionary"
        assert ("PoliceInformation" in response_payload["Results"][0]), "Expected PoliceInformation attribute"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"], list)), "Expected object to be a list"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0], dict)), "Expected object to be a dict"
        
        assert ("getAdditionalOfficers" in response_payload["Results"][0]["PoliceInformation"][0]), "Expected getAdditionalOfficers attribute"
        assert ("getPoliceInfo" in response_payload["Results"][0]["PoliceInformation"][0]), "Expected getPoliceInfo attribute"
        assert ("numberOfPOlice" in response_payload["Results"][0]["PoliceInformation"][0]), "Expected numberOfPOlice attribute"
        assert ("policeBadgeNumber" in response_payload["Results"][0]["PoliceInformation"][0]), "Expected policeBadgeNumber attribute"
        assert ("policeOfficerName" in response_payload["Results"][0]["PoliceInformation"][0]), "Expected policeOfficerName attribute"
        assert ("policeOfficerStation" in response_payload["Results"][0]["PoliceInformation"][0]), "Expected policeOfficerStation attribute"
        
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0]["getAdditionalOfficers"], int)), "Expected getAdditionalOfficers to be an integer"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0]["getPoliceInfo"], int)), "Expected getPoliceInfo to be an integer"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0]["numberOfPOlice"], str)), "Expected numberOfPOlice to be a string"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0]["policeBadgeNumber"], str)), "Expected policeBadgeNumber to be a string"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0]["policeOfficerName"], str)), "Expected policeOfficerName to be a string"
        assert (isinstance(response_payload["Results"][0]["PoliceInformation"][0]["policeOfficerStation"], str)), "Expected policeOfficerStation to be a string"
