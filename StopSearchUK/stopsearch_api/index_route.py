from flask import Flask, jsonify
from StopSearchUK import app
from random import randint

@app.route("/")
def index_route() -> list[dict]:
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
    
    
    return jsonify(app_data, app_pages, status)