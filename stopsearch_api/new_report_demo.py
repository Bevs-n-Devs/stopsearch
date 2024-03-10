import os
from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route("/new/", methods=["POST"])
def new_report_demo() -> list[dict]:
    # add fake report params here
    # follow the same design as homepage
    report_email_ = str("someone@email.com").lower()
    form_type_ = str("witness").lower()
    form_date_ = datetime.datetime.now()
    number_of_victims_ = str("3").lower()
    victim_age_ = str("18 - 24").lower()
    victim_gender_ = str("Male").lower()
    victim_race_ = str("Unkown").lower()
    street_name_ = str("Hengist Street").lower()
    town_or_city_ = str("Manchester").lower()
    postcode_ = str("M18 7EL").lower()
    seacrh_reason_ = str("Carrying a weapon").lower()
    type_of_search_ = str("Aggressive").lower()
    add_notes_ = str("Some additional notes about the incident..").lower()
    num_of_police_ = str("5 - 6").lower()
    get_police_info_ = str("Y").lower()
    police_badge_ = str("ABC1234567").lower()
    police_officer_name_ = str("John Doe").lower()
    police_station_ = str("Longsight").lower()
    additional_officers_ = str("N").lower()
    confirm_email_ = str("someone@email.com").lower()
    
    app_data = {
        "AppData": []
    }
    app_pages = {
        "AppPages": []
    }
    status = {
        "Status": 200
    }
    user_report_data = {
        "UserReportData": []
    }
    reported_by = {
        "ReportedBy": []
    }
    victim_information = {
        "VictimInformation": []
    }
    police_public_relations = {
        "PolicePublicRelations": []
    }
    police_information = {
        "PoliceInformation": []
    }
    form_type = {
        "FormType": []
    }
    form_date = {
        "FormDate": []
    }
    confirm_email = {
        "ConfirmEmail": []
    }
    number_of_victims = {
        "NumberOfVictims": []
    }
    victim_age = {
        "VictimAge": []
    }
    victim_gender = {
        "VictimGender": []
    }
    victim_race = {
        "VictimRace": []
    }
    incident_locatoin = {
        "IncidentLocation": []
    }
    seacrh_reason = {
        "SearchReason": []
    }
    type_of_search = {
        "TypeOfSearch": []
    }
    add_notes = {
        "AdditionalNotes": []
    }
    num_of_police = {
        "NumberOfPolice": []
    }
    police_officer_information = {
        "PoliceOfficerInfomration": []
    }
    get_police_info = {
        "ObtainPoliceInfo": []
    }
    police_info = {
        "PoliceInfo": []
    }
    additional_info = {
        "AdditionalInfo": []
    }
    additional_officers = {
        "AdditionalOfficers": []
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
    
    
    report_email = {
        "ReportEmail": report_email_
    }
    # add users email to ReportEmail
    user_report_data["UserReportData"].append(report_email)
    
    # add data to ReportedBy
    form_type["FormType"].append(form_type_)
    reported_by["ReportedBy"].append(form_type)
    
    # add datetime object to FormDate
    form_date["FormDate"].append({"formDate": form_date_})
    reported_by["ReportedBy"].append(form_date)
    
    # add formatted date to FormDate
    converted_date: list = form_date_.strftime("%c").split(" ")
    incident_weekday = converted_date[0]
    incident_month = converted_date[1]
    incident_date = converted_date[2]
    incident_time = converted_date[3]
    incident_year = converted_date[4]
    formatted_date = {
        "formattedDate": int(incident_date),
        "formattedWeekday": incident_weekday,
        "formattedMonth": incident_month,
        "formattedYear": int(incident_year),
        "formattedTime": incident_time,
    }
    form_date["FormDate"].append(formatted_date)
    
    confirm_email["ConfirmEmail"].append(confirm_email_)
    
    reported_by["ReportedBy"].append(confirm_email)
    user_report_data["UserReportData"].append(reported_by)
    
    user_report_data["UserReportData"].append(victim_information)
    
    user_report_data["UserReportData"].append(police_public_relations)
    
    user_report_data["UserReportData"].append(police_information)
    
    # add data to VictimInfomation list
    victim_information["VictimInformation"].append({
        "NumberOfVictims": number_of_victims_,
        "VictimAge": victim_age_,
        "VictimGender": victim_gender_,
        "VictimRace": victim_race_,
    })
    
    # add data to PolicePublicRelations list
    incident_locatoin["IncidentLocation"].append({
        "StreetName": street_name_,
        "TownOrCity": town_or_city_,
        "PostCode": postcode_,
    })
    police_public_relations["PolicePublicRelations"].append(incident_locatoin)
    
    police_public_relations["PolicePublicRelations"].append({
        "SearchReason": seacrh_reason_,
        "TypeOfSearch": type_of_search_,
        "AdditionalNotes": add_notes_,
    })
    
    # add data to PoliceInformation
    police_officer_information["PoliceOfficerInfomration"].append({
        "NumberOfPolice": num_of_police_,
        "ObtainPoliceInformation": get_police_info_,
        "PoliceBadgeNumber": police_badge_,
        "PoliceOfficerName": police_officer_name_,
        "PoliceStation": police_station_,
        "additionalInfo": additional_officers_
    })
    police_information["PoliceInformation"].append(police_officer_information)
    
    additional_info["AdditionalInfo"].append({
        "AdditionalInfo": additional_officers_,
        "PoliceBadgeNumber": "null",
        "PoliceOfficerName": "null",
        "PoliceStation": "null",
        "additionalInfo": "null",
    })
    police_information["PoliceInformation"].append(additional_info)
    
    return jsonify(app_data, app_pages, status, user_report_data)