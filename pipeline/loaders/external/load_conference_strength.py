import sys
from pathlib import Path 
import pandas as pd
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_conference_strenght(): 
    with open("data/final/external/conference_strength.csv", "r") as read_conference: 
        result_load = read_conference
        #  result_conf = pd.read_csv(read_conference) 
        #  result_conf.to_json("val_conference", orient ="records", indent = 4)

    return result_load

print(load_conference_strenght())