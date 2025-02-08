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
        #self.pending_messages = (self.config_json["pending_messages"] if "pending_messages" in self.config_json.keys() else [])
        #self.objs = None
        self.objs = None
        self.msgs = []
        pass
    

    def read_api(self):
        '''
        Call the api and return only the data objects
        '''
        headers = {
            'accept' : 'application/json'
        }
        response = requests.get(self.config_json["api_feed"], headers = headers).json()
        self.objs = response[self.config_json["api_response_col"]]
        return self.objs
    

    def save_objects_to_file(self, objects, save_path=None):
        '''
        Save the aircraft data to a json file
        '''
        with open((self.config_json["api_datafile_export_location"] if save_path is None else save_path), 'w', encoding='utf-8') as f:
            json.dump(objects, f, ensure_ascii=False, indent=4)
    
    def open_objects_from_file(self, save_path=None):
        '''
        Open a json file and retrieve aircraft
        '''
        with open((self.config_json["api_datafile_export_location"] if save_path is None else save_path), 'r') as file:
            self.objs = json.load(file)
        return self.objs

    def convert_json_to_dataframe(self, json):
        '''
        Convert a array of dictionary objects (or json) into a data frame, we don't care about what keys we have
        '''
        '''counts = {}
        values = {}
        i = 0

        for obj in objects:
            for key in obj.keys():
                ## Check if we have a new key
                if key not in counts.keys():
                    counts[key] = i + 1
                    values[key] = [None] * i
                    values[key].append(obj[key])
                else:
                    counts[key] += 1
                    values[key].append(obj[key])
            i += 1

            ## Check to ensure that all of the keys have had a value added to them
            for key in counts.keys():
                if counts[key] < i:
                    counts[key] += 1
                    values[key].append(None)

        df = pd.DataFrame(values)
        return df
        '''
        df = pd.read_json(json, orient='records')
        return df





