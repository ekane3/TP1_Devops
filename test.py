import requests
import json

api_key = "240aa650f4db4e154a07d0459c30a347"
lat = "48.208176"
lon = "16.373819"

url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = json.loads(response.text)
print(data)