import json
from main import app
from behave import given, when, then


@given("the NewReport route is running")
def step_impl(context):
    with app.app_context():
        context.client = app.test_client()
        

@when("a request is made to the NewReport with the correct parameters")
def step_impl(context):
    with app.app_context():
        formType = "witness"
        formDate = "2024-03-01"
        context.endpoint_url = f"/create/new/{formType}/{formDate}"
        context.http_response = context.client.get(context.endpoint_url)


@then("the UserReportData should be in the response")
def step_impl(context):
    with app.app_context():
        context.response_payload = json.loads(context.http_response.data)
        response_payload = context.response_payload[3] # UserReportData
        
        assert (isinstance(context.response_payload, list)), "Expected object to be a list"
        assert ("UserReportData" in response_payload), "Expected UserResponseData in payload"
        
        assert (isinstance(response_payload, dict)),"Expected object to be a dictionary"
        assert (isinstance(response_payload["UserReportData"], list))
        
        # check FormType
        form_type_dict = response_payload["UserReportData"][0]
        assert ("FormType" in form_type_dict), "Expected FormType attribute in form_type_dict"
        assert (isinstance(form_type_dict, dict)), "Expected form_type_dict to be a dictionary"
        assert (isinstance(form_type_dict["FormType"], str)), "Expected object in FormType to be a string"
        print(form_type_dict["FormType"])
        assert (form_type_dict["FormType"] == "witness"), "Expected FormType to be equal to 'witness'"
        
        # check FormDate
        form_date_dict = response_payload["UserReportData"][1]
        assert ("FormDate" in form_date_dict), "Expected FormDate attribute in form_date_dict"
        assert (isinstance(form_date_dict, dict)), "Expected form_date_dict to be a dictionary"
        assert (isinstance(form_date_dict["FormDate"], str)), "Expected object in FormDate to be a string"
        assert (form_date_dict["FormDate"] == "2024-03-01"), "Expected FormDate to be be equal to '2024-03-01'"
        