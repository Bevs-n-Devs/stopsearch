import os
import folium
import requests
from flask import Flask
from StopSearchUK import app
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
from flask import render_template
load_dotenv()

@app.route("/map")
def stopsearch_map_page():

    # make a request to the /map-data API
    map_data_response = requests.get('http://localhost:8000/map-data')
    
    # check if the response is valid
    if map_data_response.status_code == 200:
        # turn response into json object
        map_data = map_data_response.json()
    else:
        # Handle error
        return {"Error": "Map failed to load data"}
    
    


    # create start location for map
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude))
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=7,
    )

    # loop through map_data to display data in map
    for data in map_data[3]['MapData']:
        # create frame for location data
        map_data_pinpoint = 'map_data.html'
        iframe = folium.IFrame(
            html=render_template(
                map_data_pinpoint,
                data_id=data['dataID'],
                form_type=data['formType'],
                formmatted_date=data['formattedDate'],
                formatted_month=data['formattedMonth'],
                formatted_year=data['formattedYear'],
                formatted_time=data['formattedTime'],
                street_name=data['streetName'],
                town_or_city=data['townOrCity'],
                longitude=data['mapLongitude'],
                latitude=data['mapLatitude'],
                victim_age=data['victimAge'],
                victim_gender=data['victimGender'],
                victim_race=data['victimRace'],
                number_of_victims=data['numberOfVictims'],
                number_of_police=data['numberOfPolice'],
                type_of_search=data['typeOfSearch'],
                search_reason=data['searchReason']


            ),
            width=500,
            height=500
        )

        popup = folium.Popup(iframe, max_width=2650)

        # add the coordinates on the map
        folium.Marker(
            location=[float(data['mapLatitude']), float(data['mapLongitude'])],  # Convert to float
            popup=popup,
            icon=folium.Icon(color='blue', icon_color='red', icon='home', prefix='fa')
        ).add_to(map)

    return map._repr_html_()