@SearchByIDRoute
Feature: Test SearchByIDRoute route

    Scenario Outline: Get a report via the dataID
        Given the SearchByID route is running
        When a request is made to the SearchByID route with dataID: <data_id>
        Then the AppData information should be in the response.
        Then the AppPages information should be in the response.
        Then the status code data should be in the response.
        Then the Results should be in the response.
        Then the ReportEmail data object should be in the Results response payload in the expectd format.
        Then the VictimInformation data object should be in the Results response payload in the expected format.
        Then the PolicePublicRelations data object should be in the Results response payload in the expectd format.
        Then the PoliceInformation data object should be in the Results response payload in the expectd format.
    
    Examples:
        | data_id |
        | 1       |