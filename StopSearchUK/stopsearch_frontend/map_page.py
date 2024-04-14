import os
import folium
from flask import Flask
from StopSearchUK import app
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
load_dotenv()

@app.route("/map")
def stopsearch_map_page():
    latitude = '51.49667998379874'
    longitude = '-0.10402997960522953'
    start_location = (float(latitude), float(longitude)) 
    map = folium.Map(
        location=start_location,
        tiles="OpenStreetMap",
        zoom_start=9,
    )
    # geolocator 
    return map._repr_html_()