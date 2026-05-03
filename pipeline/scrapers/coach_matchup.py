import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root) 

from pipeline.loaders.load_coach_matchup import load_coach_matchup

def fetch_coach_matchup(year): 
    return load_coach_matchup()

# print(fetch_coach_matchup(2023))