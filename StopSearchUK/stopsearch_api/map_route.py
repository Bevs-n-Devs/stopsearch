from StopSearchUK import app
from flask import jsonify, request
from StopSearchUK.stopsearch_service import map_service
import StopSearchUK.utils as utils
from datetime import datetime
import geocoder
from random import randint

@app.route('/mmap-data')
def map_data():
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

    results = {
        "MapData": []
    }

    with app.app_context():
        # get all the map data from db
        get_map_data = map_service.get_all_map_data()

        for data in get_map_data:
            # put data in dict, it needs to be in the same order
            result = {
                'dataID': data[0],
                'formType': data[1],
                'formattedDate': data[2],
                'formattedMonth': data[3],
                'formattedYear': data[4],
                'formattedTime': data[5],
                'numberOfVictims': data[6],
                'victimAge': data[7],
                'victimRace': data[8],
                'victimGender': data[9],
                'searchReason': data[10],
                'typeOfSearch': data[11],
                'streetName': data[12],
                'townOrCity': data[13],
                'mapLatitude': data[14],
                'mapLongitude': data[15],
                'numberOfPolice': data[16]
            }
            results['MapData'].append(result)

        # results['Results'].append(get_map_data)

    if get_map_data:
        return jsonify(app_data, app_pages, status, results)