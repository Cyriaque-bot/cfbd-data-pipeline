import json 
import os 
import sys 


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)



def load_conference():
    with open("data/raw/conference_sample.json") as jsonconference: 
        vallconference = json.load(jsonconference)
    return vallconference