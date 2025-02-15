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

        ## Allow for input of variable number of arguments and accept them if passed
        # for key, value in kwargs.items():
        #     print(f"Key: {key}, Value: {value}")
        #     self[key] = value

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

        with open(file_path, 'r') as file:
            line_number = 0
            ## Skip of leading lines
            for line in file:
                ## TO-DO: comment me out, Print our current line, for trouble shooting
                print(line)

                line_number += 1
                if line_number > self.first_lines_skip:
                    break
            
            stop_at = self.max_lines + self.first_lines_skip

            for line in file:
                ## TO-DO: comment me out, Print our current line, for trouble shooting
                print(line)

                ## Check for our first line, since it's not really important

                ## Check if this is our time (hour) line, if so update our hour

                ## Parse the line if it starts with a timestamp 

                ## Parse the lines that start with a blank, thus append it to the previous line

                ## Increment our line number
                line_number += 1

                if line_number > stop_at:
                    break

        ## Return the dataframe
        return self.dataframe

derg_parser = DergParser(max_lines=5)