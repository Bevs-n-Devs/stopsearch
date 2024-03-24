from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route("/report", methods=["GET", "POST"])
def report_page() -> list[dict]:
    if request.method == "GET":
        
        # get from data from home api 
        home_api_url = "http://localhost:8000/home"
        res = requests.get(home_api_url)
        
        form_data =  res.json()
        
        automatic_address = form_data[3]["ReportData"][0]["Data"][3]["PolicePublicRelations"][1]["IncidentLocation"][1]["addressOptions"][1]["0"]
        manual_address = form_data[3]["ReportData"][0]["Data"][3]["PolicePublicRelations"][1]["IncidentLocation"][1]["addressOptions"][1]["1"]
        
        # form type form data
        form_type_options = form_data[3]["ReportData"][0]["Data"][1]["ReportedBy"][1]["FormType"][1] # '0': victim, '1': witness
        
        # victim information form data 
        num_victims_dropdown = form_data[3]["ReportData"][0]["Data"][2]["VictimInformation"][1]["NumberOfVictims"][1] # '0': 'Unknown', '1': '1', ... '11': '10+', '12': '15+' 
        victim_age_dropdown = form_data[3]["ReportData"][0]["Data"][2]["VictimInformation"][2]["VictimAge"][1] # '0': 'Unknown', '1': '15 - 17', ... '7': '45+', '8': '50+'
        victim_gender_dropdown = form_data[3]["ReportData"][0]["Data"][2]["VictimInformation"][3]["VictimGender"][1] # '0': 'Unknown', '1': 'Male', ... , '5': A group of mixed genders
        victim_race_dropdown = form_data[3]["ReportData"][0]["Data"][2]["VictimInformation"][4]["VictimRace"][1] # '0': 'Unknown', '1': 'Arab', ..., '5': 'White'
        
        # police public relations form data
        location_options = form_data[3]["ReportData"][0]["Data"][3]["PolicePublicRelations"][1]["IncidentLocation"][1]["addressOptions"][1] # '0': automaticAddress, '1': manualAddress
        search_reason_dropdown = form_data[3]["ReportData"][0]["Data"][3]["PolicePublicRelations"][2]["SearchReason"][1] # '0': 'Unknown', '1': 'suspision of drugs', ..., '7': 'In a location where crime is high'
        type_of_search_dropdown = form_data[3]["ReportData"][0]["Data"][3]["PolicePublicRelations"][3]["TypeOfSearch"][1] # '0': 'Unknown', '1': 'Moderate', '2': 'Aggressive'
        add_notes_options = form_data[3]["ReportData"][0]["Data"][3]["PolicePublicRelations"][4]["AddNotes"][2]["additionalNotes"][1] # '0': 'No', '1': 'reportNotes
        
        # police information form data
        num_police_dropdown = form_data[3]["ReportData"][0]["Data"][4]["PoliceInformation"][1]["NumberOfPolice"][1] # '0': 'Unknown', '1': '1 - 2', ..., '6': '15+', '7': 'Over 20
        get_police_officer_info_options = form_data[3]["ReportData"][0]["Data"][4]["PoliceInformation"][2]["PoliceOfficerInformation"][1]["obtainPoliceInfo"][1] # '0': no, '1': yes
        get_additional_police_info_options = form_data[3]["ReportData"][0]["Data"][4]["PoliceInformation"][2]["PoliceOfficerInformation"][3]["AdditionalInfo"][1] # '0': no, '1': yes
        
        result = num_police_dropdown
        # print(add_notes_options)
        
        return render_template(
            "homepage.html",
            result=result,
            form_type_options=form_type_options,
            num_victims_dropdown=num_victims_dropdown,
            victim_age_dropdown=victim_age_dropdown,
            victim_gender_dropdown=victim_gender_dropdown,
            victim_race_dropdown=victim_race_dropdown,
            location_options=location_options,
            search_reason_dropdown=search_reason_dropdown,
            type_of_search_dropdown=type_of_search_dropdown,
            add_notes_options=add_notes_options,
            num_police_dropdown=num_police_dropdown,
            get_police_officer_info_options=get_police_officer_info_options,
            get_additional_police_info_options=get_additional_police_info_options
        )
    