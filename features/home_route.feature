@HomeRoute
Feature: Test Home route

    Scenario: Retrieving all Home route results
        Given the Home route is running
        When a request is made to the Home route
        Then the AppData information should be in the response
        Then the AppPages information should be in the response
        Then the status code data should be in the response
        Then the ReportData should be in the response