@IndexRoute
Feature: Test Index Index route

    Scenario: Retrieving all Index route results
        Given the Index route is running
        When a request is made to the Index route
        Then the AppData information should be in the response.
        Then the AppPages information should be in the response.
        Then the status code data should be in the response.