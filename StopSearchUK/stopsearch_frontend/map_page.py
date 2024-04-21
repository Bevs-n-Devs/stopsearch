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
        # extract coordinates using list comprehension
        coordinates = [(entry['mapLatitude'], entry['mapLongitude']) for entry in map_data[3]['MapData']]
        # print(coordinates)
    else:
        # Handle error
        coordinates = []



    # create start location for map
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude))
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=9,
    )

    # create frame for location data
    html_page = 'homepage.html'
    iframe = folium.IFrame(html=render_template(html_page), width=500, height=500)
    popup = folium.Popup(iframe, max_width=2650)
    # add the data to map pin

    # add the coodinates on the map
    for data in map_data[3]['MapData']:
        folium.Marker(
            location=[data['mapLatitude'], data['mapLongitude']],
            popup=popup,
            icon=folium.Icon(color='blue', icon_color='red', icon='home', prefix='fa')
        ).add_to(map)

    return map._repr_html_()