from flask import Flask, jsonify

app = Flask(__name__)

# picture the ReportData being used to show the user data
# if button is pressed then enter data in dict obj provided
# Example: PoliceOfficerInfo
# default None/NULL data as 'Unknown' string

@app.route("/home")
def home() -> list[dict]:
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
        "CreateReport": "/create/report",
        "FindReportByVictim": "/find/by/victim",
        "FindReportByWitness": "/find/by/witness",
    }
    app_pages["AppPages"].append(appPages)
    
    report_data = {
        "ReportData": []
    }
    # data is linked to report_data
    data = {
        "Data": []
    }
    # reported_by is linked to data
    reported_by = {
        "ReportedBy": [
            "Information about the person who made the report",
        ]
    }
    
    # victim_informtion is linked to data
    victim_information = {
        "VictimInformation": [
            "Information about the victims involved in the incident",
        ]
    }
    
    # police_public_relations is linked to data
    police_public_relations = {
        "PolicePublicRelations": [
            "Information between the public and police involded in the incident",
        ]
    }
    
    # police_info is linked to data    
    police_info = {
        "PoliceInformation": [
            "Infomration on the police officers and their conduct at the scene of the incident",
        ]
    }
    
    report_data["ReportData"].append(data)
    data["Data"].append(reported_by)
    data["Data"].append(victim_information)
    data["Data"].append(police_public_relations)
    data["Data"].append(police_info)
    
    # add FormType to Data[0]["ReportedBy"]
    form_type = {
        "FormType": [
            "FormType drop down options",
            {
                "0": "victim",
                "1": "witness",
            }
        ] 
    }
    reported_by["ReportedBy"].append(form_type)
    
    # add FormDate to Data[0]["ReportedBy"]
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
    reported_by["ReportedBy"].append(form_date)
    
    # add ReportEmail to Data[0]["ReportedBy"]
    report_email = {
        "ReportEmail": [
            "User must enter their email to validate the report",
            {
                "reportEmail": "An email needs to be entered to validate the report"
            }
        ]
    }
    reported_by["ReportedBy"].append(report_email)
    
    # add NumberOfVictims to Data[1]["Victiminformation"]
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
    victim_information["VictimInformation"].append(number_of_victims)
    
    # add VictimAge to Data[1]["Victiminformation"]
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
    victim_information["VictimInformation"].append(victim_age)
    
    # add VictimGender to Data[1]["Victiminformation"]
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
    victim_information["VictimInformation"].append(victim_gender)
    
    # add VictimRace to Data[1]["Victiminformation"]
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
    victim_information["VictimInformation"].append(victim_race)
    
    # add IncidentLocation to Data[2]["PolicePublicRelations"]
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
    police_public_relations["PolicePublicRelations"].append(incident_location)
    
    # add SearchReason to Data[2]["PolicePublicRelations"]
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
    police_public_relations["PolicePublicRelations"].append(search_reason)
    
    
    # add TypeOfSearch to Data[2]["PolicePublicRelations"]
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
    police_public_relations["PolicePublicRelations"].append(type_of_search)
    
    # add AddNotes to Data[2]["PolicePublicRelations"]
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
    police_public_relations["PolicePublicRelations"].append(add_notes)
    
    
    # add NumberOfPolice to Data[2]["PoliceInformation"]
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
    
    # add PoliceOfficerInformation to PoliceInformation
    police_officer_information = {
        "PoliceOfficerInformation": [
            "Functionality to record single or multiple police officers",
            {
                "obtainPoliceInfo": [
                    "Drop down options to find out if user obtained the police officer's details",
                    {
                        "0": "N",
                        "1": "Y",
                    }
                ]
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
                "AdditionalInfo": [
                    "Drop down options to find out if user wants to enter exra police officer(s)",
                    {
                        "0": "N",
                        "1": "Y",
                    },
                ]
            },
            {
                "additionalOfficers": [
                    "Any additional police officer data is extended to enterPoliceInfo list",
                    {
                        "additionalInfo": "Y or N",
                        "PoliceBadgeNumber": "...",
                        "PoliceOfficerName": "...",
                        "PoliceStation": "..."
                    }
                ]
            }
        ]
    }
    police_info["PoliceInformation"].append(police_officer_information)
    
    return jsonify(app_data, app_pages, status, report_data)