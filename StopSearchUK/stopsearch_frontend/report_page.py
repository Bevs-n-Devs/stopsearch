from flask import Flask, jsonify, request, render_template, url_for
from StopSearchUK import app
import geocoder
from ip2geotools.databases.noncommercial import DbIpCity

@app.route("/report", methods=['POST', 'GET'])
def report_page():
    if request.method == "GET":
        # If it's a GET request, render the template
        return render_template('homepage.html')
    else:
        
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
            "SearchByID": "/search/1",
            "ReportPage": "/report"
        }
        app_pages["AppPages"].append(appPages)
        
        
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
        
        # Access form data safely
        form_email = request.form["form_email"]
        
        # Store the form email in result_data
        result_data["ReportEmail"].append(form_email)
        
         # collect data from completed form
        form_email = request.form.get('form_email') # returns None if doesn't exist
        form_type = request.form.get('form_type')
        form_date = request.form.get('form_date')
        # form_confirm_email = request.form["confirm_email"]
        form_confirm_email = request.form["confirm_email"]
        # form_confirm_email = request.form.get('confirm_email')
        
        form_get_address = request.form.get('get_address')
        form_street_name = request.form.get('street_name')
        form_town_or_city = request.form.get('town_or_city')
        form_postcode = request.form.get('postcode')
        form_type_of_search = request.form.get('type_of_search')
        form_search_options = request.form.get('search_reason')
        
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
        
        # get_user_ip = request.remote_addr
        get_user_ip = request.environ['REMOTE_ADDR']
        # check if email matches
        if str(form_email) != str(form_confirm_email):
            print(f"form email: {form_email}", f"confirmed email: {form_confirm_email}")
            return {'EmailError': 'Email does not match.'}
        
        # if automaticAddress or manualAddress
        if form_get_address == 'automaticAddress':
            # get user IP address
            
            
            """
            192.168.0.1
            10.143.99.108
            172.16.0.1
            """
            # 192.168.0.126
            ip = '192.168.0.126'
            # user_ip = geocoder.ip("10.143.99.108")
            user_ip = geocoder.ip(get_user_ip)
            user_ip = geocoder.ip("8.8.8.8")
            if user_ip.ok:
                if user_ip.latlng == []:
                    return {'GeoLocation Error': 'Could not get latitude & longitude for your current address.'}
                # get address and update the form address details
                address = user_ip.address
                map_coordinates = user_ip.latlng # get latitude & longitude
                return jsonify(map_coordinates, address)
            else:
                return {'GeoLocation Error': 'Could not get the data for your current address.'}
            
            print(user_ip.address, user_ip.latlng)
            # print(request.remote_user)
            # user_ip = request.environ['REMOTE_ADDR']
            # get_ip = geocoder.ipinfo(location=user_ip)
        if form_get_address == 'manualAddress':
            user_ip = geocoder.ip(get_user_ip)
            # get_ip = geocoder.ipinfo(location=user_ip)
        
        # if 
        
        message = "POST request received and processed successfully!"
        
        # Return a JSON response containing the message and the form email
        # return jsonify(app_data, app_pages, status, results)
        return user_ip.json