import numpy as np
import pandas as pd

class DergParser:
    def __init__(self, **kwargs):
        """
        Initialize our parser, I'm using an object to give myself some flexibility
        """
        ## Initialize a pointer for the dataframe that we build so we can get it back
        ##     later.
        self.dataframe = None

        ## What is the prefix that we 
        self.time_line_prefix = "**"

        ## How many lines should we skip from the front of the file
        self.first_lines_skip = 1

        ## Max number of lines to read (after skipped) into our dataframe
        self.max_lines = None
        if "max_lines" in kwargs.keys():
            self.max_lines = kwargs["max_lines"]

        ## So that this doesn't need to get changed when I move this to production, 
        ##     go ahead and make these parameters
        self.parts = {
            "time"   : {"start": 0,  "end": 12, "type": "time"},
            "meat1"  : {"start": 12, "end": 22, "type": "str"},
            "jseries": {"start": 22, "end": 31, "type": "jseries"},
            "meta2"  : {"start": 31, "end": 38, "type": "str"},
            "meta3"  : {"start": 38, "end": 10, "type": "str"},
            "msg"    : {"start": 47,            "type": "str"},
        }

        ## Allow for input of variable number of arguments and accept them if passed
        # for key, value in kwargs.items():
        #     print(f"Key: {key}, Value: {value}")
        #     self[key] = value
        ## ============================= End __init__ =============================

    def parse(self, file_path):
        """
        Parse a derge file
        """
        if file_path is None:
            raise Exception("Sorry, no file passed to the derg parser.") 
            return None
        
        ## What is our current hour
        hour = "00"
        df = {}

        ## Build our dataframe results
        for key in self.parts.keys():
            df[key] = []
        ## Add the two columns for the jseries parts
        df["jseries_1"] = []
        df["jseries_2"] = []

        ## Open our file and start looping through the lines
        with open(file_path, 'r') as file:
            line_number = 0
            ## Skip of leading lines
            for line in file:
                ## TO-DO: comment me out, Print our current line, for trouble shooting
                print(line)

                line_number += 1
                if line_number > self.first_lines_skip:
                    break
            
            stop_at = None
            if self.max_lines is not None:
                stop_at = self.max_lines + self.first_lines_skip

            for line in file:
                ## TO-DO: comment me out, Print our current line, for trouble shooting
                print(line)

                ## Check if this is our time (hour) line, if so update our hour
                if line.startswith(self.time_line_prefix):
                    hour = line[3:5]

                ## Parse the lines that start with a blank, thus append it to the previous line
                if line.startswith(" "):
                    print("-> Continuation line")
                ## Parse the line if it starts with a timestamp 
                else:
                    print("Message line")
                    df = self.parseFullLine(line, df, hour=hour)

                ## Increment our line number
                line_number += 1

                print(f"hour {hour}")

                if stop_at is not None and line_number > stop_at:
                    break

        print("Print the dataframe results")
        print(df)

        ## Return the dataframe
        return self.dataframe
        ## =============================== End parse ==============================

    def parseFullLine(self, line, dict, hour="00"):
        """
        Parse a full line
        """
        for key in self.parts.keys():
            type = self.parts[key]["type"]
            value = ""
            
            ## If there is no end
            if "end" in self.parts[key]:
                value = line[self.parts[key]["start"]:self.parts[key]["end"]]
            else:
                value = line[self.parts[key]["start"]:]

            print(f"{key}({type})\t\t {value}")
            if type == "str":
                ## If the type is str, go ahead and store it as a string
                dict[key].append(value)
            elif type == "jseries":
                ## if the type is jseries, go ahead and pass it to our jseries
                ##     type parser and deal with that
                dict[key].append(value)
            elif type == "time":
                ## if the type is time, append hour to the beginning of the 
                ##     time data
                dict[key].append(f"{hour}:{value}")
        return dict
        ## =========================== End parseFullLine ==========================

    def parseJSeriesType(self, jtype, dict):
        """
        Given a JSeries message type, parse it into two halves
        """
        return dict
        ## ========================== End parseJSeriesType ========================

derg_parser = DergParser(max_lines=5)
derg_parser.parse("fake_derg.derg")