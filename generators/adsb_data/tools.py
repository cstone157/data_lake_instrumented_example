import json
import os
import requests
import random

import numpy as np
import pandas as pd

class FakeAdsbProcess:
    def __init__(self, config_filepath="config.json", config_json=None):
        '''
        Construct our Fake Processor
        '''
        if config_json is None:
            with open(config_filepath, 'r') as file:
                self.config_json = json.load(file)
        else:
            self.config_json = config_json
        
        ## If our config has pending messages, then go ahead and append them to the beginning
        self.pending_messages = ([] if self.config_json.pending_messages is None else self.config_json.pending_messages)
        pass
    

    def read_api(self):
        '''
        Call the api and return only the data objects
        '''
        headers = {
            'accept' : 'application/json'
        }
        response = requests.get(self.config_json["api_feed"], headers = headers).json()
        return response[self.config_json["api_response_col"]]
    

    def save_objects_to_file(self, objects, save_path=None):
        '''
        Save the aircraft data to a json file
        '''
        with open((self.config_json["api_response_col"] if save_path is None else save_path), 'w', encoding='utf-8') as f:
            json.dump(objects, f, ensure_ascii=False, indent=4)
        




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
