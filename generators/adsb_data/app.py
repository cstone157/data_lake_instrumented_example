import json
import os
import requests


import numpy as np
import pandas as pd

def get_config():
    '''
    Return the config of our application
    '''
    with open('config.json', 'r') as file:
        return json.load(file)

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

def convert_adsb_json_to_dataframe(aircrafts):
    counts = {}
    values = {}
    i = 0

    for aircraft in aircrafts:
        for key in aircraft.keys():
            ## Check if we have a new key
            if key not in counts.keys():
                counts[key] = i + 1
                values[key] = [None] * i
                values[key].append(aircraft[key])
            else:
                counts[key] += 1
                values[key].append(aircraft[key])
        i += 1

        ## Check to ensure that all of the keys have had a value added to them
        for key in counts.keys():
            if counts[key] < i:
                counts[key] += 1
                values[key].append(None)

    df = pd.DataFrame(values)
    return df

if os.path.exists('data.json'):
    ## Get my aircrafts from a file (temporary)
    aircrafts = open_aircraft_from_file()
else:
    ## Pull the aircrafts from adsb and save to file
    aircrafts = read_adsb_api()
    save_aircraft_to_file(aircrafts)

## Convert the aircrafts into a dataframe
df = convert_adsb_json_to_dataframe(aircrafts)

## Get our configuration
config = get_config()

## Update our dataframe and include what the current status of our datapoints are
df["last_update"] = pd.to_datetime('now')

## Find the flights that don't have a flight, we are going to fake a seperate process for them
na_flight_df = df[df['flight'].isna()]

## Find the flights that start with UA, since we are going to use them to pretend we have a process running in the background
ua_flights_df = df[df['flight'].notna()]


## Add a initial status to the dataframe
ua_flights_df["status"] = config["initial_task"]
ua_flights_df["system_name"] = config["system_name"]
ua_flights_df["timestamp"] = pd.to_datetime('now')
ua_flights_df["initial_time"] = 0

## Build up our log of messages until we are called then purge them
messages_pending = []
for index, row in ua_flights_df.iterrows():
    msg = {}
    msg["last_update"] = row["last_update"]
    msg["status"] = row["status"]
    msg["system_name"] = row["system_name"]
    msg["timestamp"] = row["timestamp"]
    msg["flight"] = row["flight"]
    msg["r_msg"] = row["r"]
    msg["t_msg"] = row["t"]
    msg["emergency"] = row["emergency"]
    msg["category"] = row["category"]
    msg["lat"] = row["lat"]
    msg["lon"] = row["lon"]
    
    messages_pending.append(msg)

print(messages_pending)