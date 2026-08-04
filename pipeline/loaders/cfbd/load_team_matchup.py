import json 
import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



def team_matchups(): 
    with open("data/raw/cfbd/team_matchup_sample.json", "r") as jsontaemmatchup: 
        valljsontaemmatchup = json.load(jsontaemmatchup)
    return valljsontaemmatchup

# print(team_matchups())
     