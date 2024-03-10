import os
from flask import Flask, jsonify, request
# from stopsearch_service import new_report_service # causes circular import
from datetime import datetime

app = Flask(__name__)

@app.route("/new/"
           + "<reportEmail>/<formType>/<formDate>/<numberOfVictims>/<victimAge>"
           + "/<victimGender>/<victimRace>/<incidentStreetName>/<incidentTownOrCity>/"
           + "<incidentPostcode>/<searchReason>/<typeOfSearch>/<addNotes>/<numberOfPolice>/<obtainPoliceInfo>/"
           + "<policeBadgeNumber>/<policeOfficerName>/<policeStation>/<additionalOfficers>/<confirmEmail>", 
           methods=["POST"]) # validateEmail the last response
def new_report(
        reportEmail,
        formType,
        formDate,
        confirmEmail,
        numberOfVictims,
        victimAge,
        victimGender,
        victimRace,
        incidentStreetName,
        incidentTownOrCity,
        incidentPostcode,
        searchReason,
        typeOfSearch,
        addNotes,
        numberOfPolice,
        obtainPoliceInfo,
        policeBadgeNumber,
        policeOfficerName,
        policeStation,
        additionalOfficers,
        
    ) -> list[dict]:
    # get API attributes and convert to correct format
    report_email = str(reportEmail).lower()
    form_type = str(formType).lower()
    form_date = formDate
    number_of_victims = str(numberOfVictims).lower()
    victim_age = str(victimAge).lower()
    victim_gender = str(victimGender).lower()
    victim_race = str(victimRace).lower()
    street_name = str(incidentStreetName).lower()
    town_or_city = str(incidentTownOrCity).lower()
    postcode = str(incidentPostcode).lower()
    seacrh_reason = str(searchReason).lower()
    type_of_search = str(typeOfSearch).lower()
    add_notes = str(addNotes).lower()
    num_of_police = str(numberOfPolice).lower()
    get_police_info = str(obtainPoliceInfo).lower()
    police_badge = str(policeBadgeNumber).lower()
    police_officer = str(policeOfficerName).lower()
    police_station = str(policeStation).lower()
    additional_officers = str(additionalOfficers).lower()
    confirm_email = str(confirmEmail).lower()
    
    
    
    
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
        "CreateReport": "/new/",
        "FindReportByVictim": "/find/by/victim",
        "FindReportByWitness": "/find/by/witness",
    }
    app_pages["AppPages"].append(appPages)
    
    
    user_report_data = {
        "UserReportData": []
    }

    
    return jsonify(app_data, app_pages, status, user_report_data )