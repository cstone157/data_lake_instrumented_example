import numpy as np
import pandas as pd

message_type = {
    "J0" : "System Information Exchange and Network Management Word",
    "J1" : "System Information Exchange and Network Management Word",
    "J2" : "PPLI Word",
    "J3" : "Surveillance Word",
    #"J4" : "",
    "J5" : "Anti-submarine Warfare Word",
    "J6" : "Amplification Word",
    "J7" : "Information Management Word",
    "J8" : "Information Management Word",
    "J9" : "Weapons Coordination and Management Word",
    "J10": "Weapons Coordination and Management Word",
    "J11": "Network Enabled Weapon Word",
    "J12": "Control Word",
    "J13": "Platform and System Status Word",
    "J14": "Control Word",
    "J15": "Threat Warning Word",
    "J16": "Mission Support",
    "J17": "Miscellaneous Word",
    "J27": "National Use Word",
    "J28": "National Use Word",
    "J29": "National Use Word",
    "J30": "National Use Word",
    "J31": "Miscellaneous Word",
}

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