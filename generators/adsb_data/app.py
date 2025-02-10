import json
import os
import requests
import random

import numpy as np
import pandas as pd

from tools import FakeAdsbProcess

## Retrieve the config.json from the files
config_filepath = 'config.json'
with open(config_filepath, 'r') as file:
    config_json = json.load(file)


## Retrieve the api data from api
# headers = {
#     'accept' : 'application/json'
# }
# response = requests.get(config_json["api_feed"], headers = headers).json()
# json_objs = response[config_json["api_response_col"]]
#with open((config_json["current_objects"]), 'w', encoding='utf-8') as f:
#    json.dump(json_objs, f, ensure_ascii=False, indent=4)

## (Substituting the data.json for the time being to save amount of API calls)
#with open((config_json["current_objects"]), 'r') as file:
#    json_objs = json.load(file)
## Convert to a dataframe
#df = pd.read_json(json_objs[0], orient='records')
df = pd.read_json(config_json["current_objects"], orient='records')
#print(df.columns)
# print(df[df.columns[:10]].head())
# print(df[df.columns[11:20]].head())
# print(df[df.columns[21:30]].head())
# print(df[df.columns[31:40]].head())
# print(df[df.columns[41:]].head())

## Filter down to only the colums we care about
df = df[config_json["api_colums"].keys()]
df = df.rename(columns=config_json["api_colums"])


## Filter down to only the ones we want to see



## Generate the initial messages from the api
## Loop till done
    ## Wait the specified amount of time
    ## Generate the next batch of messages, based upon probablility and config
    ## If we have waited long enough call the api again and then filter down to only the columns we care about
## If the messages are asked for go ahead and pass them over a tcp connection to who ever called for them

