import sys 
from pathlib import Path
import json


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_team_top25(): 
    with open("data/raw/derived/team_top25_sample.json") as json_team_top25: 
         result_team_top25 = json.load(json_team_top25)
    return result_team_top25


# print(load_team_top25())