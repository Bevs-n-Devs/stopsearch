from flask import Flask, jsonify, request, render_template, url_for
import requests

app = Flask(__name__)

@app.route("/report", methods=['GET', 'POST'])
def report_page() -> list[dict]:
    
    if request.method == "GET":
        # get from data from home api 
        home_api_url = "http://localhost:8000/home"
        res = requests.get(home_api_url)
        
        # get json response from api payload
        form_data =  res.json()
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
        
        return render_template(
            "homepage.html",
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
            get_additional_police_info_options=get_additional_police_info_options,
        )
    else:
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
        
        # collect data from completed form
        form_email = request.form.get('form_email') # returns None if doesn't exist
        result_data["ReportEmail"].append(form_email)
        form_type = request.form.get('form_type')
        result_data["ReportEmail"].append(form_type)
        form_date = request.form.get('form_date')
        result_data["ReportEmail"].append(form_date)
        form_confirm_email = request.form.get('confirm_email')
        result_data["ReportEmail"].append(form_confirm_email)
        
        form_get_address = request.form.get('get_address')
        result_data["PolicePublicRelations"].append(form_get_address)
        form_street_name = request.form.get('street_name')
        result_data["PolicePublicRelations"].append(form_street_name)
        form_town_or_city = request.form.get('town_or_city')
        result_data["PolicePublicRelations"].append(form_town_or_city)
        form_postcode = request.form.get('postcode')
        result_data["PolicePublicRelations"].append(form_postcode)
        form_type_of_search = request.form.get('type_of_search')
        result_data["PoliceInformation"].append(form_type_of_search)
        form_search_options = request.form.get('search_reason')
        result_data["PolicePublicRelations"].append(form_search_options)
        
        form_num_of_victims = request.form.get('number_of_victims')
        result_data["VictimInformation"].append(form_num_of_victims)
        form_victim_age = request.form.get('victim_age')
        result_data["VictimInformation"].append(form_victim_age)
        form_victim_gender = request.form.get('victim_gender')
        result_data["VictimInformation"].append(form_victim_gender)
        form_victim_race = request.form.get('victim_race')
        result_data["VictimInformation"].append(form_victim_race)
        
        form_num_of_police = request.form.get('number_of_police')
        result_data["PoliceInformation"].append(form_num_of_police)
        form_get_police_info = request.form.get('get_police_info')
        result_data["PoliceInformation"].append(form_get_police_info)
        form_police_badge = request.form.get('police_officer_badge')
        result_data["PoliceInformation"].append(form_police_badge)
        form_police_name = request.form.get('police_officer_name')
        result_data["PoliceInformation"].append(form_police_name)
        form_police_station = request.form.get('police_officer_station')
        result_data["PoliceInformation"].append(form_police_station)
        form_additional_police = request.form.get('additional_police_info')
        result_data["PoliceInformation"].append(form_additional_police)

        print(result_data)
        return "show form"