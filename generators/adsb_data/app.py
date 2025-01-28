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
msg_type, flight, alt_geom, emergency = [], [], [], []

for aircraft in aircrafts:
    if 'type' in aircraft:
        msg_type.append(aircraft['type'])
    else:
        msg_type.append("")

    if 'flight' in aircraft:
        flight.append(aircraft['flight'])
    else:
        flight.append("")

    if 'alt_geom' in aircraft:
        alt_geom.append(aircraft['alt_geom'])
    else:
        alt_geom.append("")

    if 'emergency' in aircraft:
        emergency.append(aircraft['emergency'])
    else:
        emergency.append("")


df = pd.DataFrame({ 'msg_type': msg_type, 'flight': flight, 'alt_geom': alt_geom, 'emergency': emergency, })
print(df.head())