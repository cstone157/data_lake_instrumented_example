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
counts = {}
values = {}
i = 0

for aircraft in aircrafts:
    for key in aircraft.keys():
        ## Check if we have a new key
        if key not in counts.keys():
            counts[key] = i + 1
            #if i > 0:
            #    values[key] = [None] * i
            #else:
            #    values[key] = []
            values[key] = [None] * i
            values[key].append(aircraft[key])

        else:
            counts[key] += 1
            values[key].append(aircraft[key])

    #keys += [key for key in aircraft.keys()]
    #keys = list(set(keys))

    i += 1
    ## Check to ensure that all of the keys have had a value added to them
    for key in counts.keys():
        if counts[key] < i:
            counts[key] += 1
            values[key].append(None)

#print(f"Keys that have been found: \n{keys}")
print(f"Number of values that have been found: \n{counts}\n")

#values = {}
#for key in keys:
#    values[key] = []
#
#for aircraft in aircrafts:
#    for key in keys:
#        if key in aircraft:
#            values[key].append(aircraft[key])
#        else:
#            values[key].append(None)

##df = pd.DataFrame({ 'msg_type': msg_type, 'flight': flight, 'alt_geom': alt_geom, 'emergency': emergency, })
df = pd.DataFrame(values)
print(df.head())

## Find the flights that don't have a flight, we are going to fake a seperate process for them
na_flight_df = df[df['flight'].isna()]
print(na_flight_df)

## Find the flights that start with UA, since we are going to use them to pretend we have a process running in the background
ua_flights_df = df[df['flight'].notna()]
print(ua_flights_df[ua_flights_df['flight'].str.startswith('UA')])