import requests
import pprint
import json
import sys

import config as vars

# print( vars.ENDPOINT +
#     "?origin="+ vars.HOME +
#     "?destination="+ vars.WORK +
#     "?departure_time="+ vars.DEPARTURE_TIME + 
#     "?key="+ vars.KEY)

argDestination = sys.argv[1]
print(argDestination)

origin = vars.CULVER_CITY
destination = vars.argDestination

homeToWork = requests.get(
    vars.API_ENDPOINT +
    "?origin="+ origin +
    "&destination="+ destination +
    "&departure_time="+ vars.DEPARTURE_TIME + 
    "&key="+ vars.KEY
)

j = homeToWork.json()

pprint.pprint(j['routes'])

# pprint.pprint(json.loads(homeToWork.json))