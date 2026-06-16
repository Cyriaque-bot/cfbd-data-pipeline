import sys
from pathlib import Path  
import json 
import os


root_project = Path(__file__).resolve().parents[2]
sys.path.append(str(root_project))

def load_rivalries(): 
    with open("data/raw/rivalries_sample.json") as jsonrivalries: 
        valrivalries = json.load(jsonrivalries)
    return valrivalries


# print(load_rivalries())