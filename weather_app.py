"""
Exercise : 
- Créer un repositoy github
- Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude
(passées en variable d'environnement) en utilisant openweather API dans le langage de
programmation de votre choix (bash, python, go, nodejs, etc)
- Packager son code dans une image Docker
- Mettre a disposition son image sur DockerHub
- Mettre a disposition son code dans un repository Github

- Mettre a disposition un lien vers son image sur le site de DockerHub

"""
import openweather
import requests
import json
import os
from datetime import datetime

# Create a client object with your API key
ow = openweather.OpenWeather()

# Get the weather for a specific location
# You can use the following variables to get the weather for a specific location
# lat = os.environ['LAT']
# lon = os.environ['LON']
# city = os.environ['CITY']
# country = os.environ['COUNTRY']
# ow.get_weather(lat, lon)

stations = ow.find_stations_near(
    7.0, # Longitude
    50.0, # Latitude
    100, # Radius in km
)

# iterate over the stations
for station in stations:
    print(station)

# get current weather at Cologne/Bonn airport
# (station id = 4885)

print(ow.get_weather(4885))

# historic weather
start_date = datetime(2013, 9, 10)
end_date = datetime(2013, 9, 15)

# default: hourly interval
print( ow.get_historic_weather(4885, start_date, end_date) )

# daily aggregates
print( ow.get_historic_weather(4885, start_date, end_date, "day") )