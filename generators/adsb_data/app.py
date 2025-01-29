import requests
import json

import numpy as np
import pandas as pd

def read_adsb_api():
    '''
    Call the adsb api and return only the aircraft
    '''
    headers = {
        'accept' : 'application/json'
    }
    response = requests.get('https://api.adsb.lol/v2/lat/34.05/lon/-118.25/dist/200', headers = headers).json()
    aircrafts = response["ac"]
    return aircrafts

def save_aircraft_to_file(aircrafts):
    '''
    Save the aircraft data to a json file
    '''
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(aircrafts, f, ensure_ascii=False, indent=4)

def open_aircraft_from_file():
    '''
    Open a json file and retrieve aircraft
    '''
    with open('data.json', 'r') as file:
        aircrafts = json.load(file)
    return aircrafts

aircrafts = open_aircraft_from_file()
keys = []

for aircraft in aircrafts:
    keys += [key for key in aircraft.keys()]
    keys = list(set(keys))

print(f"Keys that have been found: \n{keys}")

values = {}
for key in keys:
    values[key] = []

for aircraft in aircrafts:
    for key in keys:
        if key in aircraft:
            values[key].append(aircraft[key])
        else:
            values[key].append(None)

##df = pd.DataFrame({ 'msg_type': msg_type, 'flight': flight, 'alt_geom': alt_geom, 'emergency': emergency, })
df = pd.DataFrame(values)
print(df.head())