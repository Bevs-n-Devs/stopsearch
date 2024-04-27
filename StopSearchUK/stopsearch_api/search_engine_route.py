from flask import jsonify
from StopSearchUK import app
from StopSearchUK.stopsearch_service import search_engine_service


@app.route("/search/all")
def search_all_route() -> list[dict]:
    # get data from service function
    all_reports_query = search_engine_service.search_all_reports()
    
    # create data to be returned back to the user
    app_data = {
        "AppData": []
    }
    app_pages = {
        "AppPages": []
    }
    status = {
        "Status": 200
    }
    
    # add data to AppData
    appData = {
        "App": "StopSearch UK",
        "AppPage": "/",
        "Description": "An app developed to record and report incidents between the police and the public.",
        "Founder": "Daniella Rose + Akoto Tech",
        "Year": "2024",
    }
    app_data["AppData"].append(appData)
    
    # add data to AppPages
    appPages = {
        "Index": "/",
        "Manual": "/docs",
        "HomePage": "/home",
        "CreateReportDemo": "/new/",
        "Demo": "/demo",
        "SearchAll": "/search/all",
        "SearchByID": "/search/1"
    }
    app_pages["AppPages"].append(appPages)

    # return all results to user
    results = {
        "Results": []
    }
    result_data = {
        "ReportEmail": [],
        "VictimInformation": [],
        "PolicePublicRelations": [],
        "PoliceInformation": []
    }
    results["Results"].append(result_data)

    # get data from all reports
    for data in all_reports_query:
        pass