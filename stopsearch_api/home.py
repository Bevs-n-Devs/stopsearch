from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/home")
def home():
    form_type = {
        "FormType": {
            "0": "victim",
            "1": "witness",
        }
    }
    form_date = {
        "FormDate": {
            "0": "datime format",
        }
    }
    incident_location = {
        "IncidentLocation": {
            "0": "Enter street name and town or city of where the incident occured.",
        }
    }
    incident_postcode = {
        "IncidentPostcode": {
            "0": "Enter the postcode where the incident occured.",
        }
    }
    search_reason = {
        "SearchReason": {
            "0": "Unknown",
            "1": "suspision of drugs",
            "2": "Carrying a weapon",
            "3": "Stolen goods",
            "4": "suspision of committing a crime",
            "5": "suspision of committing a serious or violent crime",
            "6": "History of carrying or using a weapon in the past",
            "7": "In a location where crime is high",
        }
    }
    number_of_victims = {
        "NumberOfVictims": {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "10",
            "10": "10+",
            "11": "15+",
        }
    }
    number_of_police = {
        "NumberOfPolice": {
            "0": "1 - 2",
            "1": "3 - 4",
            "2": "5 - 6",
            "3": "6+",
            "4": "10+",
            "5": "15+",
            "6": "Over 20"
        }
    }
    type_of_search = {
        "TypeOfSearch":{
            "0": "Unknown",
            "1": "Moderate",
            "2": "Aggressive"
        }
    }
    police_officer_information = {
        "PoliceOfficerInformation": {
            "0": "Yes",
            "1": "No",
            "If Yes": {
                "PoliceBadgeNumber": "Enter police officer's badge number if available",
                "PoliceOfficerName": "Enter police officer's name if available",
                "PoliceStation": "Enter the police officer's station if available"
            }
        }
    }
    victim_age = {
        "VictimAge": {
            "0": "15 - 17",
            "1": "18 - 24",
            "2": "25 - 30",
            "3": "31 - 35",
            "4": "35+",
            "5": "40+",
            "6": "45+",
            "7": "50+"
        }
    }
    victim_gender = {
        "VictimGender": {
            "0": "I don\'t know",
            "1": "Male",
            "2": "Female",
            "3": "Non-binary",
            "4": "Trans",
            "5": "A group of mixed genders",
        }
    }
    victim_race = {
        "VictimRace": {
            "0": "Arab",
            "1": "Asian",
            "2": "Black",
            "3": "Mixed race",
            "4": "White",
        }
    }
    add_notes = {
        "AddNotes": {
            "0": "Additional notes goes here if possible"
        }
    }
    report_email = {
        "ReportEmail": {
            "0": "An email needs to be entered to validate the report"
        }
    }
    
    
    
    home = {
        "App": "Stop Search UK",
        "Instructions": "Complete the following questions on the report page.",
        "Report Page": "/create/report",
        "Report Questions": [
            form_type,
            form_date,
            incident_location,
            incident_postcode,
            search_reason,
            number_of_victims,
            number_of_police,
            type_of_search,
            police_officer_information,
            victim_age,
            victim_gender,
            victim_race,
            add_notes,
            report_email
        ],
        
    }
    status = {"status": 200}
    return jsonify(home, status)