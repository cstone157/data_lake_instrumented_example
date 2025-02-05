import json
import os
import requests
import random

import numpy as np
import pandas as pd

from tools import FakeAdsbProcess

process01 = FakeAdsbProcess('config.json')

'''
if os.path.exists('data.json'):
    ## Get my aircrafts from a file (temporary)
    aircrafts = tools.open_aircraft_from_file()
else:
    ## Pull the aircrafts from adsb and save to file
    aircrafts = tools.read_adsb_api()
    tools.save_aircraft_to_file(aircrafts)

## Convert the aircrafts into a dataframe
df = tools.convert_adsb_json_to_dataframe(aircrafts)

## Get our configuration
config = tools.get_config()

## Update our dataframe and include what the current status of our datapoints are
df["last_update"] = pd.to_datetime('now')

## Find the flights that don't have a flight, we are going to fake a seperate process for them
na_flight_df = df[df['flight'].isna()].copy()

## Find the flights that start with UA, since we are going to use them to pretend we have a process running in the background
ua_flights_df = df[df['flight'].notna()].copy()


## Add a initial status to the dataframe
ua_flights_df["status"] = config["initial_task"]
ua_flights_df["system_name"] = config["system_name"]
ua_flights_df["user"] = ""
ua_flights_df["role"] = ""

ua_flights_df["timestamp"] = pd.to_datetime('now')
ua_flights_df["timestamp_toupdate"] = pd.to_datetime('now')

## Go into our messages and use the config.json and calculate the next time for a "System/process update"
for index, row in ua_flights_df.iterrows():
    task = config["tasks"][row["status"]]
    next_tasks = task["next_status"]
    task_probability = random.random()

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

#print(messages_pending)
'''