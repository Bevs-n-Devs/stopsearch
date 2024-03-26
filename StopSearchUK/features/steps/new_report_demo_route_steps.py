import json
from main import app
from behave import given, when, then

@given("the NewReportDemo route is running")
def step_impl(context):
    with app.app_context():
        context.client = app.test_client()

@when("a request is made to the NewReportDemo route")
def step_impl(context):
    with app.app_context():
        context.endpoint_url = "/demo"
        context.http_response = context.client.get(context.endpoint_url)

@then("a Message should be in the response.")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[3]
        
        print(response_payload)
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert (isinstance(response_payload, dict)), "Expected response_payload to be a dictionary"
        
        assert ("Message" in response_payload), "Expected Message attribute"
        