import numpy as np
import pandas as pd

file_path = ""

df = {
    "time": [],
    "col1": [],
    "col2": [],
    "col3": [],
    "col4": [],
    "col5": [],
    "col6": [],
    "col7": [],
    "col8": [],
    "col9": [],
}

uid = 0
line_num = 1

with open(file_path, 'r') as file:
    for line in file:
        if line_num > 2:
            df["time"].append(line[:10])
            df["col1"].append(line[:10])
            df["col2"].append(line[:10])
            df["col3"].append(line[:10])
            df["col4"].append(line[:10])
            df["col5"].append(line[:10])
            df["col6"].append(line[:10])
            df["col7"].append(line[:10])
            df["col8"].append(line[:10])
            df["col9"].append(line[:10])

        line_num += 1

df = pd.DataFrame(df)
df.head()