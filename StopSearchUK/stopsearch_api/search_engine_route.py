from flask import jsonify, request
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
        "SearchByID": f"/search/{randint(1,5)}",
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

        result_data = {
            "ReportedBy": {
                "dataID": get_result[0],
                "reportedBy": get_result[1],
                "formattedDate": get_result[2],
                "formattedMonth": get_result[3],
                "formattedYear": get_result[4],
                "formattedTime": get_result[5],
            },
            "VictimInformation": {
                "numberOfVictims": get_result[6],
                "victimAge": get_result[7],
                "victimRace": get_result[8],
                "victimGender": get_result[9],
            },
            "PolicePublicRelations": {
                "searchReason": get_result[10],
                "typeOfSearch": get_result[11],
                "additionalNotes": get_result[12],
                "streetName": get_result[13],
                "townOrCity": get_result[14],
                "longitude": get_result[15],
                "latitude": get_result[16],
            },
            "PoliceInformation": {
                "numberOfPolice": get_result[17],
                "obtainPoliceInfo": get_result[18],
                "policeBadgeNumber": get_result[19],
                "policeOfficerName": get_result[20],
                "policeStation": get_result[21],
            },
        }
        results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)

@app.route("/search/formType/<form_type>")
def search_report_by_form_type(form_type: str):
    form_type = str(form_type)
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_form_type(form_type)

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)

@app.route("/search/victimAge/<victim_age>")
def search_report_by_victim_age(victim_age: str):
    victim_age = str(victim_age)
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_victim_age(victim_age)

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)

@app.route("/search/victimGender/<victim_gender>")
def search_report_by_victim_gender(victim_gender: str):
    victim_gender = str(victim_gender)
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_victim_gender(victim_gender)

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)
    
@app.route("/search/victimRace/<victim_race>")
def search_report_by_victim_race(victim_race: str):
    victim_race = str(victim_race)
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_victim_race(victim_race)

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)
    
@app.route("/search/searchType/<search_type>")
def search_report_by_search_type(search_type: str):
    search_type = str(search_type)
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_search_type(search_type)

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)
    
@app.route("/search/searchReason/<search_reason>")
def search_report_by_search_reason(search_reason: str):
    search_reason = str(search_reason)
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_search_reason(search_reason)

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)
    
@app.route("/search/90Days")
def search_report_by_search_by_90_days():
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_last_90_days()

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)

@app.route("/search/6Months")
def search_report_by_search_by_6_months():
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_last_6_months()

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)
    
@app.route("/search/12Months")
def search_report_by_search_by_12_months():
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_last_12_months()

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)

@app.route("/search/30Days")
def search_report_by_search_by_30_days():
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
        "SearchByID": f"/search/{randint(1,5)}",
        "ReportPage": "/report",
        "MapPage": "/map",
        "MapData": "/map-data"
    }
    app_pages["AppPages"].append(appPages)

    results = {
        "Results": []
    }

    with app.app_context():
        get_results = search_engine_service.search_report_by_last_30_days()

        for data in get_results:

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
                    "numberOfPolice": data[17],
                    "obtainPoliceInfo": data[18],
                    "policeBadgeNumber": data[19],
                    "policeOfficerName": data[20],
                    "policeStation": data[21],
                },
            }
            results["Results"].append(result_data)
            
        return jsonify(app_data, app_pages, status, results)