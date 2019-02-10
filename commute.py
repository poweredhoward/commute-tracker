import requests
import pprint
import json


homeToWork = requests.get(
    "https://maps.googleapis.com/maps/api/directions/json?" +
    "origin=14851+W+Sunset+Blvd+90272&" +
    "destination=540+W+Woodbury+Rd+91001&"+
    "departure_time=now&"+
    "key=AIzaSyAstItVHmWt5mJ4HSotWOSIT4s4Y_4UBfs"
)

j = homeToWork.json()

pprint.pprint(j['routes'])

# pprint.pprint(json.loads(homeToWork.json))