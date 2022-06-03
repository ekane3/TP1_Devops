import requests
import json
import os

#api_key = "240aa650f4db4e154a07d0459c30a347"
#lat = "48.208176"
#lon = "16.373819"

lat = os.environ['LAT']
lon = os.environ['LON']
api_key = os.environ['API_KEY']

# create a function that returns the weather for a specific location using env lat and lon
def get_weather(lat, lon, api_key):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    response = requests.get(url)
    data = json.loads(response.text)
    return data

if __name__ == "__main__":
    print(get_weather(lat, lon, api_key))