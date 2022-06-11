# TP1_Devops
## Author : Emile EKANE
## Date : 2020-06-09

## Docs
### Sujet : Renvoyer la météo d'un lieu en passant en variable d'environnement les coordonnées de la ville  

### 1ère étape : Créer le wrapper avec python
```python
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
```

### Etape 2 : Créer le Dockerfile
```dockerfile
#DockerFile to run my weather wrapper app
FROM python:latest

#Labels as key value pair
LABEL maintainer="ekane3.github.io"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /app as working directory
WORKDIR /app

# Now the structure looks like this '/app/app.py'

#To add the remote file to the root dir in container
COPY app.py ./

#From official image documentation
CMD ["python", "app.py"]
```	
#### Etape 3 : Créer l'image Docker
> After creating  both the script and the Dockerfile, we can now build the image.
     `docker build -t weatherapp .`
We verify if our image is built successfully by running the following command:
        `docker images`
We now have a new image called weatherapp.

We run our image using the following command:
        `docker run  
--env LAT="5.902785" --env LON="102.754175" --env API_KEY="240aa650f4db4e154a07d0459c30a347" weatherapp`  


After running the Docker Container, you will see the output meteo printed.

## Docker Hub

We create a repo on Docker Hub named weather_app.
Then we create a nice tag on this repo with the following command:
        `docker tag weatherapp:latest ekane3/weather_app:latest`  
And we do a push on our repo with the following command:
        `docker push ekane3/weather_app:latest`  

Link to the repo: [https://hub.docker.com/r/ekane3/weather_app/](https://hub.docker.com/r/ekane3/weather_app/)

#### Etape 4 : Utiliser Trivy 

Trivy is a tool that scans Docker images vulnerabilities on the DockerHub network and displays them in a table.

Install Trivy with the following command:
        `sudo apt-get install trivy`
Let's scan our image with the following command:
        `trivy --image ekane3/weather_app:latest`