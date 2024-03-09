from flask import Flask, jsonify

app = Flask(__name__)

# picture the ReportData being used to show the user data
# if button is pressed then enter data in dict obj provided
# Example: PoliceOfficerInfo
# default None/NULL data as 'Unknown' string

@app.route("/home")
def home():
    app_data = {
        "AppData": []
    }
    app_pages = {
        "AppPages": []
    }
    status = {
        "Status": 200
    }
    report_data = {
        "ReportData": []
    }
    police_info = {
        "PoliceInformation": [
            "Infomration on the police officers and their conduct at the scene of the incident",
        ]
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
        "CreateReport": "/create/report",
        "FindReportByVictim": "/find/by/victim",
        "FindReportByWitness": "/find/by/witness",
    }
    app_pages["AppPages"].append(appPages)
    
    # add FormType to ReportData
    form_type = {
        "FormType": [
            "FormType drop down options",
            {
                "0": "victim",
                "1": "witness",
            }
        ] 
    }
    report_data["ReportData"].append(form_type)
    
    # add FormDate to ReportData
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
                    "formMonth": "Month in a verbose format January: - December",
                    "formYear": "Full format of year: 2024",
                    "formTime": "Time of when inicent occured",
                }
            }
        ]
    }
    report_data["ReportData"].append(form_date)
    
    # add IncidentLocation to ReportData
    incident_location = {
        "IncidentLocation": [
            "Automatically obtain the users address from their phones IP address",
            {
                "addressOptions": [
                    "addressOptions drop down options",
                   {
                        "0": "automaticAddress",
                        "1": "manualAddress",
                    } 
                ]
            },
            {
                "manualAddress": [
                    "Manually enter the address of the incident",
                    {
                        "StreetName": "Enter street name and town or city of where the incident occured.",
                        "TownOrCity": "Enter name of town or city of the incident",
                        "Postcode": "Enter the postcode of the incident",
                    }
                ]
            },
        ]
    }
    report_data["ReportData"].append(incident_location)
    
    # add SearchReason to ReportData
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
    report_data["ReportData"].append(search_reason)
    
    # add NumberOfVictims to ReportData
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
    report_data["ReportData"].append(number_of_victims)
    
    # add NumberOfPolice to PoliceInformation
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
    police_info["PoliceInformation"].append(number_of_police)
    
    # add TypeOfSearch to PoliceInformation
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
    police_info["PoliceInformation"].append(type_of_search)
    
    # add PoliceOfficerInformation to PoliceInformation
    police_officer_information = {
        "PoliceOfficerInformation": [
            "Functionality to record single or multiple police officers",
            {
                "additionalOfficerData": [
                    "additionalOfficerData drop down options",
                    {
                        "0": "Unknown",
                        "1": "additionalOfficers",
                    }
                ],
            },
            {
                "Unknown": "Leave additionalOfficers empty",
            },
            {
                "enterPoliceInfo": [
                    "Enter the police officer's badge number, name & station",
                    {
                        "PoliceBadgeNumber": "Enter police officer's badge number if available",
                        "PoliceOfficerName": "Enter police officer's name if available",
                        "PoliceStation": "Enter the police officer's station if available",
                    }
                ]
            },
            {
                "additionalOfficers": [
                    "Any additional police officer data is extended to enterPoliceInfo list",
                    {
                        "PoliceBadgeNumber": "...",
                        "PoliceOfficerName": "...",
                        "PoliceStation": "..."
                    }
                ]
            }
        ]
    }
    police_info["PoliceInformation"].append(police_officer_information)
    
    # add PoliceInformation to ReportData
    report_data["ReportData"].append(police_info)
    
    # add VictimAge to ReportData
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
    report_data["ReportData"].append(victim_age)
    
    # add VictimGender to ReportData
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
    report_data["ReportData"].append(victim_gender)
    
    # add VictimRace to ReportData
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
    report_data["ReportData"].append(victim_race)
    
    # add AddNotes to ReportData
    add_notes = {
        "AddNotes": [
            "Option to add additional notes to the report",
            {
                "reportNotes": [
                    {
                        "notes": "Additional notes goes here if possible"
                    }
                ]
            },
            {
                "additionalNotes": [
                    "additionalNotes drop down options",
                    {
                        # default set to No if
                        "0": "No",
                        "1": "reportNotes",
                    }
                ], 
            },
        ]
    }
    report_data["ReportData"].append(add_notes)
    
    # add ReportEmail to ReportData
    report_email = {
        "ReportEmail": [
            "User must enter their email to validate the report",
            {
                "reportEmail": "An email needs to be entered to validate the report"
            }
        ]
    }
    report_data["ReportData"].append(report_email)
    
    
    
    return jsonify(app_data, app_pages, status, report_data)