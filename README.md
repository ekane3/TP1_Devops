# TP1_Devops
## Author : Emile EKANE

## Notation
- Code disponible sur Github
- Dockerfile qui build
- Docker image disponible sur DockerHub
- API qui renvoie la météo en utilisant la commande suivante en utilisant votre image :
```bash
docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY=****
maregistry/api:1.0.0
```
## Bonus
- 0 CVE (trivy) `trivy image maregistry/api:1.0.0`
- 0 lint errors on Dockerfile (hadolint) `docker run --rm -i hadolint/hadolint < Dockerfile`
- Aucune données sensibles stockées dans l'image (i.e: openweather API key)

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

On crée une repo sur Docker Hub nommée weather_app.
Ensuite on se crée un joli tag sur cette repo avec la commande suivante:
        `docker tag weatherapp:latest ekane3/weather_app:latest`
Et on effectue un push sur notre repo avec la commande suivante:
        `docker push ekane3/weather_app:latest`

Link to the repo: [https://hub.docker.com/r/ekane3/weather_app/](https://hub.docker.com/r/ekane3/weather_app/)