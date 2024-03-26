@NewReportRoute
Feature: Test NewReport route

    Scenario: Sending data to create a new report
        Given the NewReport route is running
        When a request is made to the NewReport with the correct parameters
        Then the AppData information should be in the response
        Then the AppPages information should be in the response
        Then the status code data should be in the response
        Then the UserReportData should be in the response 
