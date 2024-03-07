from flask import Flask, jsonify

app = Flask(__name__)

# picture the ReportData being used to show the user data
# if button is pressed then enter data in dict obj provided
# Example: PoliceOfficerInfo
# default None/NULL data as 'Unknown' string 

@app.route("/home")
def home():
    pages = {
        "0": "/",
        "1": "/docs",
        "2": "/home",
        "3": "/create/report/",
        "4": "/find/by/victim",
        "5": "/find/by/witness"
    }
    form_type = {
        "FormType": [
            "FormType drop down options",
            {
                "0": "victim",
                "1": "witness",
            }
        ] 
    }
    form_date = {
        "FormDate": [
            "FormDate drop down options",
            # formDate gets converted into formatedDate
            {
                "formDate": "date in DateTime format"
            },
            {
                "formattedDate": {
                    "formDate": "Date in verbose format: 1st - 31st",
                    "formMonth": "Month in a verbose format January: - Deceember",
                    "formYear": "Full format of year: 2024",
                    "formTime": "Time of when inicent occured",
                }
            }
        ]
    }
    incident_location = {
        "IncidentLocation": {
            "eneterAddress": [
                "enterAddress drop down options",
                {
                    "0": "automaticAddress",
                    "1": "manualAddress",
                }
            ],
            "automaticAddress": "Automatically obtain the users address from their phones IP address",
            "manualAddress": [
                "Manually enter the address of the incident",
                {
                    "StreetName": "Enter street name and town or city of where the incident occured.",
                    "TownOrCity": "Enter name of town or city of the incident",
                    "Postcode": "Enter the postcode of the incident",
                }
            ]
        }
    }
    search_reason = {
        "SearchReason": [
            "SearchReason drop down options",
            {
                "0": "Unknown",
                "1": "suspision of drugs",
                "2": "Carrying a weapon",
                "3": "Stolen goods",
                "4": "suspision of committing a crime",
                "5": "suspision of committing a serious or violent crime",
                "6": "History of carrying or using a weapon in the past",
                "7": "In a location where crime is high",
            }
        ]
    }
    number_of_victims = {
        "NumberOfVictims": [
            "NumberOfVictims drop down options",
            {
                "0": "Unknown",
                "1": "1",
                "2": "2",
                "3": "3",
                "4": "4",
                "5": "5",
                "6": "6",
                "7": "7",
                "8": "8",
                "9": "9",
                "10": "10",
                "11": "10+",
                "12": "15+",
            }
        ]
    }
    number_of_police = {
        "NumberOfPolice": [
            "NumberOfPolice drop down options",
            {
                "0": "Unknown",
                "1": "1 - 2",
                "2": "3 - 4",
                "3": "5 - 6",
                "4": "6+",
                "5": "10+",
                "6": "15+",
                "7": "Over 20"  
            }
        ]
    }
    type_of_search = {
        "TypeOfSearch": [
            "TypeOfSearch drop down options",
            {
                "0": "Unknown",
                "1": "Moderate",
                "2": "Aggressive"
            }
        ]
    }
    police_officer_information = {
        "PoliceOfficerInformation": {
            "additionalOfficerData": [
                "additionalOfficerData drop down options",
                {
                    "0": "Unknown",
                    "1": "additionalOfficers",
                }
            ],
            "Unknown": "Leave 'additionalOfficers' empty",
            "enterPoliceInfo": [
                "Enter the police officer's badge number, name & station",
                {
                    "PoliceBadgeNumber": "Enter police officer's badge number if available",
                    "PoliceOfficerName": "Enter police officer's name if available",
                    "PoliceStation": "Enter the police officer's station if available",
                }
            ]
            },
            "additionalOfficers": [
                "Any additional police officer data is extended to enterPoliceInfo list",
                {
                    "PoliceBadgeNumber": "...",
                    "PoliceOfficerName": "...",
                    "PoliceStation": "..."
                }
            ]
        }
    victim_age = {
        "VictimAge": [
            "VictimAge drop down options",
            {
                "0": "Unknown",
                "1": "15 - 17",
                "2": "18 - 24",
                "3": "25 - 30",
                "4": "31 - 35",
                "5": "35+",
                "6": "40+",
                "7": "45+",
                "8": "50+",
            }
        ]
    }
    victim_gender = {
        "VictimGender": [
            "VictimGender drop down options",
            {
                "0": "Unknown",
                "1": "Male",
                "2": "Female",
                "3": "Non-binary",
                "4": "Trans",
                "5": "A group of mixed genders",
            }
        ]
    }
    victim_race = {
        "VictimRace": [
            "VictimRace drop down options",
            {
                "0": "Unknown",
                "1": "Arab",
                "2": "Asian",
                "3": "Black",
                "4": "Mixed race",
                "5": "White",
            }
        ]
    }
    add_notes = {
        "AddNotes": {
            "additionalNotes": [
                "additionalNotes drop down options",
                {
                    # default set to No if
                    "0": "No",
                    "1": "reportNotes",
                }
            ], 
            "reportNotes": [
                {
                    "notes": "Additional notes goes here if possible"
                }
            ]
        }
    }
    report_email = {
        "ReportEmail": [
            "User must enter their email to validate the report",
            {
                "reportEmail": "An email needs to be entered to validate the report"
            }
        ]
    }
    
    
    
    home = {
        "App": "StopSearch UK",
        "Year": "2024",
        "Description": "An app developed to record and report incidents between the police and the public.",
        "Founder": "Daniella Rose + Akoto Tech",
        "AppPage": "/home",
        "Pages": [
            {
                "Index": pages["0"],
                "Manual": pages["1"],
                "HomePage": pages["2"],
                "CreateReport": pages["3"],
                "FindReportByVictim": pages["4"],
                "FindReportByWitness": pages["5"],
            }
        ],
        "ReportData": [
            "Complete the following questions on the report page.",
            form_type,
            form_date,
            incident_location,
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