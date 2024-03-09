@ManualRoute
Feature: Test Manual route

    Scenario: Retrieving all Manual route results
        Given the Manual route is running
        When a request is made to the Manual route
        Then the AppData information should be in the response
        Then the AppPages information should be in the response
        Then the status code data should be in the response