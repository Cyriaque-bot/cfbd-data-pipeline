import json
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root)

def loads_teams(): 
   with open("data/raw/teams_sample.json", "r") as jsonteams: 
        valdata = json.load(jsonteams)

   return valdata