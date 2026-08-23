import sys
from pathlib import Path 
import pandas as pd
import json
import numpy as np

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_conference_strength(): 
    with open("data/final/external/conference_strength.csv", "r") as read_conference: 
    #  result_load = read_conference.read()
        result_load = pd.read_csv(read_conference)

    #  replace all the nan by null
        result_load = result_load.replace({np.nan: None})
    #  conversion en liste de dictionnaire
    dict_list_result_load = result_load.to_dict(orient = "records")

    return dict_list_result_load

# print(load_conference_strength())
#  result_conf = pd.read_csv(read_conference) 
        #  result_conf.to_json("val_conference", orient ="records", indent = 4)