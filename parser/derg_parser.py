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
            "time"   : {"start": 0,  "end": 8, "type": "time"},
            "meat1"  : {"start": 10, "end": 14, "type": "str"},
            "meta2"  : {"start": 15, "end": 21, "type": "str"},
            "jseries": {"start": 20, "end": 30, "type": "jseries"},
            "meta3"  : {"start": 30, "end": 37, "type": "str"},
            "meta4"  : {"start": 37, "end": 46, "type": "str"},
            "msg"    : {"start": 46,            "type": "str"},
        }
        ## We split the jseries into parts and these are the columns that we will use
        self.jseries_type1 = "jseries_1"
        self.jseries_type2 = "jseries_2"
        self.jseries_type3 = "jseries_3"

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
        df[self.jseries_type1] = []
        df[self.jseries_type2] = []
        df[self.jseries_type3] = []

        ## Open our file and start looping through the lines
        with open(file_path, 'r') as file:
            line_number = 1
            ## Skip of leading lines
            for line in file:
                ## TO-DO: comment me out, Print our current line, for trouble shooting
                print(f"skipping header lines: {line}")

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
                    hour = line[2:4]
                    #print(f"\n ============== \n Udating hour {hour} \n ============== \n") ## DELETE ME
                ## Parse the lines that start with a blank, thus append it to the previous line
                elif line.startswith(" "):
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
                value = line[self.parts[key]["start"]:self.parts[key]["end"]].strip()
            else:
                value = line[self.parts[key]["start"]:].strip()

            print(f"\t{key} --> {value}")

            print(f"{key}({type})\t\t {value}")
            if type == "str":
                ## If the type is str, go ahead and store it as a string
                dict[key].append(value)
            elif type == "jseries":
                ## if the type is jseries, go ahead and pass it to our jseries
                ##     type parser and deal with that
                dict[key].append(value)
                dict = self.parseJSeriesType(value, dict)
            elif type == "time":
                ## if the type is time, append hour to the beginning of the 
                ##     time data
                dict[key].append(f"{hour}:{value[3:]}")
        return dict
        ## =========================== End parseFullLine ==========================

    def parseJSeriesType(self, jtype, dict):
        """
        Given a JSeries message type, parse it into two halves
        """
        i = jtype.find(".")
        ## if there is no '.', then we are only 
        if i == -1:
            dict[self.jseries_type1].append(jtype)
            dict[self.jseries_type2].append(None)
            dict[self.jseries_type3].append(None)
        else:
            dict[self.jseries_type1].append(jtype[:i])
            tmp = jtype[i+1:]
            if tmp[-1] >= "0" and tmp[-1] <= "9":
                dict[self.jseries_type2].append(tmp)
                dict[self.jseries_type3].append(None)
            else:
                dict[self.jseries_type2].append(tmp[:-1])
                dict[self.jseries_type3].append(tmp[-1])



        return dict
        ## ========================== End parseJSeriesType ========================

derg_parser = DergParser(max_lines=5)
derg_parser.parse("fake_derg.derg")