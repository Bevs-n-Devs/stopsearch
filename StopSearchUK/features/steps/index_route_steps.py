import json
from main import app
from behave import given, when, then

@given("the Index route is running")
def index_route_client(context):
    with app.app_context():
        context.client = app.test_client()

@when("a request is made to the Index route")
def index_route_request(context):
    with app.app_context():
        context.endpoint_url = "/"
        context.http_response = context.client.get(context.endpoint_url)


@then("the AppData information should be in the response.")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[0]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expetced object to a list"
        
        assert ("AppData" in response_payload), "Expected AppData attribute"
        assert (isinstance(response_payload["AppData"], list)), "Expected object to be a list"
        assert (isinstance(response_payload["AppData"][0], dict)), "Expected object to be a dictionary"
        
        assert ("App" in response_payload["AppData"][0]), "Expected App attribute"
        assert ("AppPage" in response_payload["AppData"][0]), "Expected AppPage attribute"
        assert ("Description" in response_payload["AppData"][0]), "Expected Description attribute"
        assert ("Founder" in response_payload["AppData"][0]), "Expected Founder attribute"
        assert ("Year" in response_payload["AppData"][0]), "Expected Year attribute"
        
        assert (isinstance(response_payload["AppData"][0]["App"], str)), "Expected App to be a string"
        assert (isinstance(response_payload["AppData"][0]["AppPage"], str)), "Expected AppPage to be a string"
        assert (isinstance(response_payload["AppData"][0]["Description"], str)), "Expected Description to be a string"
        assert (isinstance(response_payload["AppData"][0]["Founder"], str)), "Expected Founder to be a string"
        assert (isinstance(response_payload["AppData"][0]["Year"], str)), "Expected Year to be a string"
        
        assert (response_payload["AppData"][0]["App"] == "StopSearch UK"), "Expected both objects to be equal"
        assert (response_payload["AppData"][0]["AppPage"] == "/"), "Expected both objects to be equal"
        assert (response_payload["AppData"][0]["Description"] == "An app developed to record and report incidents between the police and the public."), "Expected both objects to be equal"
        assert (response_payload["AppData"][0]["Founder"] == "Daniella Rose + Akoto Tech"), "Expected both objects to be equal"
        assert (response_payload["AppData"][0]["Year"] == "2024"), "Expected both objects to be equal"


@then("the AppPages information should be in the response.")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[1]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expetced object to a list"
        
        assert ("AppPages" in response_payload), "Expected AppPages attribute"
        assert (isinstance(response_payload["AppPages"], list)), "Expected object to be a list"
        assert (isinstance(response_payload["AppPages"][0], dict)), "Expected object to be a dictionary"
        
        assert ("Index" in response_payload["AppPages"][0]), "Expected Index attribute"
        assert ("HomePage" in response_payload["AppPages"][0]), "Expected HomePage attribute"
        assert ("Manual" in response_payload["AppPages"][0]), "Expected Manual attribute"
        assert ("CreateReportDemo" in response_payload["AppPages"][0]), "Expected CreateReportDemo attribute"
        assert ("Demo" in response_payload["AppPages"][0]), "Expected Demo attribute"
        assert ("SearchAll" in response_payload["AppPages"][0]), "Expected SearchAll attribute"
        assert ("SearchByID" in response_payload["AppPages"][0]), "Expected SearchByID attribute"
        
        assert (isinstance(response_payload["AppPages"][0]["Index"], str)), "Expected Index to be a string"
        assert (isinstance(response_payload["AppPages"][0]["HomePage"], str)), "Expected HomePage to be a string"
        assert (isinstance(response_payload["AppPages"][0]["Manual"], str)), "Expected Manual to be a string"
        assert (isinstance(response_payload["AppPages"][0]["CreateReportDemo"], str)), "Expected CreateReport to be a string"
        assert (isinstance(response_payload["AppPages"][0]["Demo"], str)), "Expected Demo to be a string"
        assert (isinstance(response_payload["AppPages"][0]["SearchAll"], str)), "Expected SearchAll to be a string"
        assert (isinstance(response_payload["AppPages"][0]["SearchByID"], str)), "Expected SearchByID to be a string"
        
        assert (response_payload["AppPages"][0]["Index"] == "/"), "Expected both objects to be equal"
        assert (response_payload["AppPages"][0]["HomePage"] == "/home"), "Expected both objects to be equal"
        assert (response_payload["AppPages"][0]["Manual"] == "/docs"), "Expected both objects to be equal"
        assert (response_payload["AppPages"][0]["CreateReportDemo"] == "/new/"), "Expected both objects to be equal"
        assert (response_payload["AppPages"][0]["Demo"] == "/demo"), "Expected both objects to be equal"
        assert (response_payload["AppPages"][0]["SearchAll"] == "/search/all"), "Expected both objects to be equal"
        assert (response_payload["AppPages"][0]["SearchByID"] == "/search/1"), "Expected both objects to be equal"
        

@then("the status code data should be in the response.")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[2]
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected object to be a dictionary"
        
        assert ("Status" in response_payload), "Expected Status in payload"
        
        assert (isinstance(response_payload["Status"], int)), "Expected Status to be an integer"
        assert (response_payload["Status"] == 200),"Expected both objects to be equal"