from StopSearchUK import app
from flask import jsonify, request, render_template
from StopSearchUK.stopsearch_service import new_report_service
import StopSearchUK.utils as utils
from datetime import datetime
import geocoder

@app.route('/new/report', methods=['POST'])
def new_report_route():
    # If it's a POST request, process the form data
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
    
    # reportEmail = request.args.get('reportEmail') # returns None if nothing passed
    # formType = request.args.get('formType')
    # insert time, date (year is automatic)
    # date & time can be = to 'now' which will be:
    # datetime_obj = datetime.now(),
    # current_date = datetime_obj.date()
    # current_time = datetime_obj.time()
    
    # incidentDate = request.args.get('incidentDate')
    # incidentTime = request.args.get('incidentTime')
    # confirmEmail = request.args.get('confirmEmail')
    # numberOfVicims = request.args.get('numberOfVictims')
    # victimAge = request.args.get('victimAge')
    # victimGender = request.args.get('victimGender')
    # victimRace = request.args.get('victimRace')
    # additonalNotes = request.args.get('additionalNotes')
    # getAddress = request.args.get('getAddress')
    # incidentCountry = request.args('incidentCountry')
    # incidentStreetName = request.args.get('incidentStreetName')
    # incidentTownOrCity = request.args.get('incidentTownOrCity')
    # searchReason = request.args.get('searchReason')
    # typeOfSearch = request.args.get('typeOfSearch')
    # getPoliceInfo = request.args.get('getPoliceInfo')
    # getAdditionalOfficers = request.args.get('getAdditionalOfficers')
    # numberOfPolice = request.args.get('numberOfPolice')
    # policeBadgeNumber = request.args.get('policeBadgeNumber')
    # policeOfficerName = request.args.get('policeOfficerName')
    # policeOfficerStation = request.args.get('policeOfficerStation')
    
    if request.method == 'POST':
        # get data from form
        form_email = request.form.get('form_email') # returns None if doesn't exist
        form_type = request.form.get('form_type')
        form_date = request.form.get('form_date')
        form_confirm_email = request.form.get('confirm_email')
        
        form_get_address = request.form.get('get_address')
        form_street_name = request.form.get('street_name')
        form_town_or_city = request.form.get('town_or_city')
        form_postcode = request.form.get('postcode')
        form_type_of_search = request.form.get('type_of_search')
        form_search_options = request.form.get('search_reason')
        form_additional_notes = request.form.get('additional_notes')
        
        form_num_of_victims = request.form.get('number_of_victims')
        form_victim_age = request.form.get('victim_age')
        form_victim_gender = request.form.get('victim_gender')
        form_victim_race = request.form.get('victim_race')
        
        form_num_of_police = request.form.get('number_of_police')
        form_get_police_info = request.form.get('get_police_info')
        form_police_badge = request.form.get('police_officer_badge')
        form_police_name = request.form.get('police_officer_name')
        form_police_station = request.form.get('police_officer_station')
        form_additional_police = request.form.get('additional_police_info')
        
        # check if email is the same
        if form_email != form_confirm_email:
            email_error = 'Email does not match'
            return render_template('homepage.html', email_error=email_error)
        
        # date_time = datetime.fromtimestamp(form_date)
        get_date = utils.convert_datetime_to_string_and_parse_object(form_date=form_date)
    
        # print(datetime_object.strftime('%c').split(' '))
        
        
        report_email = {
            'formEmail': form_email,
            'formType': form_type,
            'formDate': form_date,
            'formattedDate': get_date[0][2],
            'formattedDay': get_date[0][0],
            'formattedMonth': get_date[0][1],
            'formattedYear': get_date[0][4],
            'formattedTime': get_date[0][3],
            'confirmEmail': form_confirm_email
        }
        result_data['ReportEmail'].append(report_email)
        
        
        # get the user's address - automaticAddress or manualAddress
        if form_get_address == 'automaticAddress':
            userIP = request.remote_addr
            print(f'user IP from request: {userIP}')
            user_ip = geocoder.ip(userIP)
            print(f'user IP from geocoder')
            user_data = user_ip.json
            print(f'user data from IP: {user_data}')
            print(user_data['ok'])
            
            if user_data['ok'] == False:
                address_error = 'Please select "Manual Address" and enter the address.\n\nUnfortunately we could not get the coordinates of your location.'
                return render_template('homepage.html', address_error=address_error)
            
            police_public = {
                'getAddress': form_get_address,
                'typeOfSearch': form_type_of_search,
                'searchReason': form_search_options,
                'incidentStreetName': user_data['address'],
                'incidentTownOrCity': user_data['city'],
                'incidentCountry': user_data['country'],
                'additionalNotes': form_additional_notes,
                'mapLatitude': user_ip.latlng[0],
                'mapLongtitude': user_ip.latlng[1]
            }
            result_data['PolicePublicRelations'].append(police_public)
        
        if form_get_address == 'manualAddress':
            # v. accurate with streetname + city/town 
            deafult_country = 'United Kingdom'
            user_cordinates = geocoder.arcgis(location=f'{form_street_name}, {form_town_or_city}, {form_postcode}, {deafult_country}')
            police_public = {
                'getAddress': form_get_address,
                'typeOfSearch': form_type_of_search,
                'searchReason': form_search_options,
                'incidentStreetName': form_street_name,
                'incidentTownOrCity': form_town_or_city,
                'incidentCountry': deafult_country,
                'additionalNotes': form_additional_notes,
                'mapLatitude': user_cordinates.latlng[0],
                'mapLongtitude': user_cordinates.latlng[1]
            }
            result_data['PolicePublicRelations'].append(police_public)
        
        if form_get_police_info == 'No':
            police_info = {
                'getPoliceInfo': form_get_police_info,
                'numberOfPOlice': form_num_of_police,
                'policeBadgeNumber': form_police_badge,
                'policeOfficerName': form_police_name,
                'policeOfficerStation': form_police_station,
                'getAdditionalOfficers': form_additional_police
            }
            result_data['PoliceInformation'].append(police_info)
        
        if form_get_police_info == 'Yes':
            if form_additional_police == 'No':
                police_info = {
                    'getPoliceInfo': form_get_police_info,
                    'numberOfPOlice': form_num_of_police,
                    'policeBadgeNumber': form_police_badge,
                    'policeOfficerName': form_police_name,
                    'policeOfficerStation': form_police_station,
                    'getAdditionalOfficers': form_additional_police
                }
                result_data['PoliceInformation'].append(police_info)
            police_info = {
                'getPoliceInfo': form_get_police_info,
                'numberOfPOlice': form_num_of_police,
                'policeBadgeNumber': form_police_badge,
                'policeOfficerName': form_police_name,
                'policeOfficerStation': form_police_station,
                'getAdditionalOfficers': form_additional_police
            }
            result_data['PoliceInformation'].append(police_info)
        
        
        victim_info = {
            'numberOfVictims': form_num_of_victims,
            'victimAge': form_victim_age,
            'victimGender': form_victim_gender,
            'victimRace': form_victim_race,
        }
        result_data['VictimInformation'].append(victim_info)
            
        # add form data to the database
        with app.app_context():
            user_data = new_report_service.create_new_report_email(form_email)
            
            user_reportedBy = new_report_service.create_new_report_by(
                confirm_email=form_confirm_email,
                new_report_email_id=user_data
            )
            user_formType = new_report_service.create_new_form_type(
                form_type=form_type,
                report_by_id=user_reportedBy
            )
            user_form_date = new_report_service.create_new_form_date(
                get_date=form_date,
                report_by_id=user_reportedBy
            )
            
            user_victim_info = new_report_service.create_new_victim_information(
                num_victims=form_num_of_victims,
                victim_age=form_victim_age,
                victim_gender=form_victim_gender,
                victim_race=form_victim_race,
                new_report_email_id=user_data
            )
            
            user_police_relations = new_report_service.create_new_police_public_relations(
                search_reason=form_search_options,
                search_type=form_type_of_search,
                notes=form_additional_notes,
                new_report_email_id=user_data
            )
            # update to add map cordinates
            user_incident_address = new_report_service.create_new_incident_address(
                address_type=form_get_address,
                street=form_street_name,
                town_city=form_town_or_city,
                postcode=form_postcode,
                police_public_id=user_police_relations
            )
            # add map cordnates 
            user_map_coordinates = new_report_service.create_new_map_coordinates(
                lat=float(police_public['mapLatitude']),
                lng=float(police_public['mapLongtitude']),
                incident_address_id=user_incident_address
            )
            
            user_police_info = new_report_service.create_new_police_information(
                num_police=form_num_of_police,
                get_police_info=form_get_police_info,
                new_report_email_id=user_data
            )
            
            user_police_officer_info = new_report_service.create_new_police_officer_information(
                badge_num=form_police_badge,
                police_name=form_police_name,
                police_station=form_police_station,
                more_officers=form_additional_police,
                new_police_information_id=user_police_info
            )
            
            
        if user_data:
            message = {
                'Message': 'Your form has been saved!'
            }
            return jsonify('hello from html page', results, message)

    return jsonify('something went wrong')