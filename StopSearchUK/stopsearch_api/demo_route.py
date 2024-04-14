# this route mimics getting data from a user to create a report in the database
# this temp route just enters the data into the database WITHOUT doing any logic - get address coordinates etc

from flask import jsonify
from StopSearchUK import app
from StopSearchUK.stopsearch_service import new_report_service
from StopSearchUK import utils
from datetime import datetime

@app.route("/demo", methods=["POST"]) 
def demo_route() -> list[dict]:
    # pretend we have taken data from URL to create form
    reportEmail = "tikvenowe@va.bj"
    formType = "witness"
    numberOfVictims = "2"
    victimAge = "18 - 24"
    victimGender = "female"
    victimRace = "asian"
    addressType = "manualaddress"  # or automaticAddress
    incidentStreetName = "62 Broadwater Road"
    incidentTownOrCity = "London"
    searchReason = "Suspision of Drugs"
    typeOfSearch = "aggressive"
    addNotes = "1HYNjrM5HVTbAN9tPZj0hyaLhdcomoYWGmNg0nyvH91Kr"
    numberOfPolice = "10+"
    getPoliceInfo = 1
    policeBadgeNumber = "ABC12345"
    policeOfficerName = "Bill Mitchell"
    policeStation = "Ozopazba station"
    additionalOfficers = 0
    confirmEmail = "tikvenowe@va.bj"
    
    # only in test 
    formDate = datetime.now()
    formatted_date = utils.convert_datetime_to_string_and_parse_object(formDate)
    
    # get API attributes and convert to correct format
    user_report_email_ = str(reportEmail).lower()
    user_form_type_ = str(formType).lower()
    user_form_date_ = formatted_date
    user_num_of_victims_ = str(numberOfVictims).lower()
    user_victim_age_ = str(victimAge).lower()
    user_victim_gender_ = str(victimGender).lower()
    user_victim_race_ = str(victimRace).lower()
    user_street_name_ = str(incidentStreetName).lower()
    user_town_or_city_ = str(incidentTownOrCity).lower()
    user_seacrh_reason_ = str(searchReason).lower()
    user_type_of_search_ = str(typeOfSearch).lower()
    user_add_notes_ = str(addNotes).lower()
    user_num_of_police_ = str(numberOfPolice).lower()
    user_obtain_police_info_ = int(getPoliceInfo)
    user_police_badge_ = str(policeBadgeNumber).lower()
    user_police_officer_ = str(policeOfficerName).lower()
    user_police_station_ = str(policeStation).lower()
    user_additional_officers_ = int(additionalOfficers)
    user_confirm_email_ = str(confirmEmail).lower()
    
    # create database models
    # Lvl 1
    with app.app_context():
        user_data = new_report_service.create_new_report_email(user_report_email_)
        
        user_reported_by = new_report_service.create_new_report_by(
            confirm_email=user_confirm_email_,
            new_report_email_id=user_data
        )
        
        user_form_type = new_report_service.create_new_form_type(
            form_type=user_form_type_,
            report_by_id=user_reported_by
        )
        
        user_form_date = new_report_service.create_new_form_date(
            get_date=user_form_date_,
            report_by_id=user_reported_by
        )
        
        user_victim_info = new_report_service.create_new_victim_information(
            num_victims=user_num_of_victims_,
            victim_age=user_victim_age_,
            victim_gender=user_victim_gender_,
            victim_race=user_victim_race_,
            new_report_email_id=user_data
        )
        
        user_police_relations = new_report_service.create_new_police_public_relations(
            search_reason=user_seacrh_reason_,
            search_type=user_type_of_search_,
            notes=user_add_notes_,
            new_report_email_id=user_data
        )
        
        user_incident_address = new_report_service.create_new_incident_address(
            address_type=addressType,
            street=user_street_name_,
            town_city=user_town_or_city_,
            police_public_id=user_police_relations
        )
        
        user_police_info = new_report_service.create_new_police_information(
            num_police=user_num_of_police_,
            get_police_info=user_obtain_police_info_,
            new_report_email_id=user_data
        )

        user_police_officer_info = new_report_service.create_new_police_officer_information(
            badge_num=user_police_badge_,
            police_name=user_police_officer_,
            police_station=user_police_station_,
            more_officers=user_additional_officers_,
            new_police_information_id=user_police_info
        )
    
    # create response
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
    
    
    
    return jsonify(app_data, app_pages, status, {"Message": "You report has been created"})