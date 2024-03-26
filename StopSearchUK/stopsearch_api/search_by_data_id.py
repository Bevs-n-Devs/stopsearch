import os
from flask import Flask, jsonify
from requests import request
from StopSearchUK import app
from StopSearchUK.stopsearch_service import new_report_service
from StopSearchUK.stopsearch_database.extension import LocalSession


@app.route("/search/<data_id>", methods=["POST"])
def search_by_dataID_route(data_id):
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
    
    get_data = new_report_service.get_data_by_data_id(data_id)
    
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
    
    
    for data in get_data:
        # add ReportedBy, FormType & FormDate to results
        user_data = {
            "dataID": data.dataID,
            "reportEmail": data.report_email,
            "confirmEmail": data.reported_by[0].confirm_email,
            "formType": data.reported_by[0].form_type[0].form_type,
            "formDate": data.reported_by[0].form_date[0].form_date,
            "formmatedDate": data.reported_by[0].form_date[0].formatted_date,
            "formattedWeekday": data.reported_by[0].form_date[0].formatted_weekday,
            "formattedMonth": data.reported_by[0].form_date[0].formatted_month,
            "formattedYear": data.reported_by[0].form_date[0].formatted_year,
            "formattedTime": data.reported_by[0].form_date[0].formatted_time,
        }
        result_data["ReportEmail"].append(user_data)
        
        # add VictimInformatio to results
        victim_info = {
            "numberOfVictims": data.victim_information[0].number_of_victims,
            "victimAge": data.victim_information[0].victim_age,
            "victimGender": data.victim_information[0].victim_gender,
            "victimRace": data.victim_information[0].victim_race,
            
        }
        result_data["VictimInformation"].append(victim_info)
        
        # add PolicePublicRelations and IncidentAddress to results
        police_public_info = {
            "searchReason": data.police_public_relations[0].search_reason,
            "typeOfSearch": data.police_public_relations[0].type_of_search,
            "additionalNotes": data.police_public_relations[0].additional_notes,
            "incidentStreetName": data.police_public_relations[0].incident_address[0].street_name,
            "incidentTownOrCity": data.police_public_relations[0].incident_address[0].town_or_city,
            "incidentPostcode": data.police_public_relations[0].incident_address[0].postcode,
            "incidentCountry": data.police_public_relations[0].incident_address[0].country,
        }
        result_data["PolicePublicRelations"].append(police_public_info)
        
        # add PoliceInformation and PoliceOfficerInformation to results
        police_info = {
            "numberOfPOlice": data.police_information[0].number_of_police,
            "getPoliceInfo": data.police_information[0].obtain_police_info,
            "policeBadgeNumber":  data.police_information[0].police_officer_information[0].police_badge_number,
            "policeOfficerName":  data.police_information[0].police_officer_information[0].police_officer_name,
            "policeOfficerStation":  data.police_information[0].police_officer_information[0].police_station,
            "getAdditionalOfficers":  data.police_information[0].police_officer_information[0].get_additional_officers,
        }
        result_data["PoliceInformation"].append(police_info)
    
    
    return jsonify(app_data, app_pages, status, results)
    