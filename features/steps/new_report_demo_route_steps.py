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
        context.endpoint_url = "/new/"
        context.http_response = context.client.get(context.endpoint_url)

@then("the UserReportData should be in the response.")
def step_impl(context):
    with app.app_context:
        pass

@then("the ReportEmail data object should be in the response payload in the expectd format.")
def step_impl(context):
    with app.app_context():
        pass
    
@then("the ConfirmationEmail data object should also be in the response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        pass

@then("the ReportEmail and ConfirmationEmail should be the same in the response payload.")
def step_impl(context):
    with app.app_context():
        pass
    
@then("the ReportedBy data object should be in the response payload in the expectd format.")
def step_impl(context):
    with app.app_context():
        pass

@then("the VictimInfomation data object should be in the response payload in the expected format.")
def step_impl(context):
    with app.app_context():
        pass

@then("the PolicePublicRelations data object should be in the response payload in the expectd format.")
def step_impl(context):
    with app.app_context():
        pass

@then("the PoliceInformation data object should be in the response payload in the expectd format.")
def step_impl(context):
    with app.app_context():
        pass