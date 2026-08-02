import json
import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root) 


def load_coach_matchup(): 
   with open("data/raw/coach_matchup_sample.json") as jsoncoachlatchup: 
      valcoach_matchup = json.load(jsoncoachlatchup)
   return valcoach_matchup