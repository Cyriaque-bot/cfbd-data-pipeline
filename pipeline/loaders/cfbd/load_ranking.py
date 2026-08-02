import json 
import os 
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def load_rankings(): 
    with open("data/raw/rankings_sample.json") as rankingsjson: 
        valrankings = json.load(rankingsjson)
    return valrankings
