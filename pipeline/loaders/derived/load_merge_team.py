import sys
from pathlib import Path 
import json


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_merge_team(): 
    with open("data/raw/derived/merge_team_sample.json") as json_merge_team: 
        result_merge_team = json.load(json_merge_team)
    return result_merge_team

# print(load_merge_team())