@NewReportDemoRoute
Feature: Test NewReportDemo route

    Scenario: Retrieving all NewReportDemo route results
        Given the NewReportDemo route is running
        When a request is made to the NewReportDemo route
        Then the AppData information should be in the response.
        Then the AppPages information should be in the response.
        Then the status code data should be in the response.
        Then a Message should be in the response.
     