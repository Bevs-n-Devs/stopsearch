import os
from flask import Flask, jsonify, request
from stopsearch_service import new_report_service
# from stopsearch_database.extensions import LocalSession
# from stopsearch_database.models import *
# from datetime import datetime

app = Flask(__name__)

@app.route("/search/all", methods=["POST"]) 
def search_all() -> list[dict]:
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
    
    # get information from database   
    get_data = new_report_service.get_all_data() 
    get_reported_by = new_report_service.get_all_reported_by_data()
    get_victim_information = new_report_service.get_all_victim_information_data()
    get_police_relations = new_report_service.get_all_police_public_relations_data()
    get_police_information = new_report_service.get_all_police_information_data()
    
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
    
    # get all Data info 
    for data in get_data:
        all_data = {
            "dataID": data[0].dataID,
            "reportEmail": data[0].report_email
        }
        result_data["ReportEmail"].append(all_data)
        
    # get all ReportedBy, FormType & FormDate info
    for data in get_reported_by:
        all_reported_by = {
            "reportedByID": data[0].reportedByID,
            "confirmEmail": data[0].confirm_email,
            "formTypeID": data[0].form_type[0].formTypeID,
            "formType": data[0].form_type[0].form_type,
            "formDateID": data[0].form_date[0].formDateID,
            # "formDate": data[0].form_date[0].form_date,
            "formmatedDate": data[0].form_date[0].formatted_date,
            "formattedWeekday": data[0].form_date[0].formatted_weekday,
            "formattedMonth": data[0].form_date[0].formatted_month,
            "formattedYear": data[0].form_date[0].formatted_year,
            "formattedTime": data[0].form_date[0].formatted_time,
        }
        result_data["ReportEmail"].append(all_reported_by)
    
    # get all VictimInformation info
    for data in get_victim_information:
        all_victim_info = {
            "victimInformationID": data[0].victimInformationID,
            "numberOfVictims": data[0].number_of_victims,
            "victimAge": data[0].victim_age,
            "victimGender": data[0].victim_gender,
            "victimRace": data[0].victim_race,
        }
        result_data["VictimInformation"].append(all_victim_info)
    
    # get all PolicePublicRelations and IncidentAddress info
    for data in get_police_relations:
        print(data[0])
        app_police_public_info = {
            "policePublicRelationsID": data[0].policePublicRelationsID,
            "searchReason": data[0].search_reason,
            "typeOfSearch": data[0].type_of_search,
            "additionalNotes": data[0].additional_notes,
            "incidentAddressID": data[0].incident_address[0].incidentAddressID,
            "incidentStreetName": data[0].incident_address[0].street_name,
            "incidentTownOrCity": data[0].incident_address[0].town_or_city,
            "incidentPostcode": data[0].incident_address[0].postcode,
            "incidentCountry": data[0].incident_address[0].country,
        }
        result_data["PolicePublicRelations"].append(app_police_public_info)
    
    # get all PoliceInformation and PoliceOfficerInformation
    for data in get_police_information:
        all_police_info = {
            "policeInformationID": data[0].policeInformationID,
            "numberOfPolice": data[0].number_of_police,
            "getPoliceInfo": data[0].obtain_police_info,
            "policeOfficerInformationID": data[0].police_officer_information[0].policeOfficerInformationID,
            "policeBadgeNumber": data[0].police_officer_information[0].police_badge_number,
            "policeOfficerName": data[0].police_officer_information[0].police_officer_name,
            "policeOfficerStation": data[0].police_officer_information[0].police_officer_station,
            "getAdditionalOfficers": data[0].police_officer_information[0].get_additional_officers,
            "additionalOffciersID": data[0].police_officer_information[0].additional_officer[0].additionalOfficerID,
            "policeBadgeNumber": data[0].police_officer_information[0].additional_officer[0].police_badge_number,
            "policeOfficerName": data[0].police_officer_information[0].additional_officer[0].police_officer_name,
            "policeOfficerStation": data[0].police_officer_information[0].additional_officer[0].police_station,
        }
        result_data["PoliceInformation"].append(all_police_info)
    
    return jsonify(app_data, app_pages, status, results)