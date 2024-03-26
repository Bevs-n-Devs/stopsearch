import json
from main import app
from behave import given, when, then

@given("the Manual route is running")
def manual_route_client(context):
    with app.app_context():
        context.client = app.test_client()

@when("a request is made to the Manual route")
def manual_route_request(context):
    with app.app_context():
        context.endpoint_url = "/docs"
        context.http_response = context.client.get(context.endpoint_url)