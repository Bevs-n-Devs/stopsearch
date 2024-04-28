from flask import jsonify
from StopSearchUK import app
from StopSearchUK.stopsearch_service import search_engine_service
from random import randint


@app.route("/search/all")
def search_all_reports_route() -> list[dict]:
    
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    # return all results to user
    results = {
        "Results": []
    }

    with app.app_context():
        # get data from all reports from db
        get_all_reports = search_engine_service.search_all_reports()

        for data in get_all_reports:

            result_data = {
                "ReportedBy": {
                    "dataID": data[0],
                    "reportedBy": data[1],
                    "formattedDate": data[2],
                    "formattedMonth": data[3],
                    "formattedYear": data[4],
                    "formattedTime": data[5],
                },
                "VictimInformation": {
                    "numberOfVictims": data[6],
                    "victimAge": data[7],
                    "victimRace": data[8],
                    "victimGender": data[9],
                },
                "PolicePublicRelations": {
                    "searchReason": data[10],
                    "typeOfSearch": data[11],
                    "additionalNotes": data[12],
                    "streetName": data[13],
                    "townOrCity": data[14],
                    "longitude": data[15],
                    "latitude": data[16],
                },
                "PoliceInformation": {
                    # write data here
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)
    

@app.route("/search/<data_id>")
def search_reports_by_data_id_route(data_id: int):
    data_id = int(data_id)
    app_data = {
        "AppData": []
    }
    app_pages = {
        "AppPages": []
    }
    status = {
        "Status": 200
    }
    
    appData = {
        "App": "StopSearch UK",
        "AppPage": "/",
        "Description": "An app developed to record and report incidents between the police and the public.",
        "Founder": "Daniella Rose + Akoto Tech",
        "Year": "2024",
    }
    app_data["AppData"].append(appData)
    
    appPages = {
        "Index": "/",
        "Manual": "/docs",
        "HomePage": "/home",
        "CreateReportDemo": "/new/",
        "Demo": "/demo",
        "SearchAll": "/search/all",
        "SearchByID": "/search/1",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        # get data from all reports from db
        get_result = search_engine_service.search_report_by_data_id(data_id)
        for data in get_result:

            result_data = {
                "ReportedBy": {
                    "dataID": data[0],
                    "reportedBy": data[1],
                    "formattedDate": data[2],
                    "formattedMonth": data[3],
                    "formattedYear": data[4],
                    "formattedTime": data[5],
                },
                "VictimInformation": {
                    "numberOfVictims": data[6],
                    "victimAge": data[7],
                    "victimRace": data[8],
                    "victimGender": data[9],
                },
                "PolicePublicRelations": {
                    "searchReason": data[10],
                    "typeOfSearch": data[11],
                    "additionalNotes": data[12],
                    "streetName": data[13],
                    "townOrCity": data[14],
                    "longitude": data[15],
                    "latitude": data[16],
                },
                "PoliceInformation": {
                    # write data here
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)