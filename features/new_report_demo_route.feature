@NewReportDemoRoute
Feature: Test NewReportDemo route

    Scenario: Retrieving all NewReportDemo route results
        Given the NewReportDemo route is running
        When a request is made to the NewReportDemo route
        Then the AppData information should be in the response.
        Then the AppPages information should be in the response.
        Then the status code data should be in the response.
        Then the UserReportData should be in the response.
        Then the ReportEmail data object should be in the response payload in the expectd format.
        Then the ConfirmationEmail data object should also be in the response payload in the expected format.
        Then the ReportEmail and ConfirmationEmail should be the same in the response payload.
        Then the ReportedBy data object should be in the response payload in the expectd format.
        Then the VictimInfomation data object should be in the response payload in the expected format.
        Then the PolicePublicRelations data object should be in the response payload in the expectd format.
        Then the PoliceInformation data object should be in the response payload in the expectd format.