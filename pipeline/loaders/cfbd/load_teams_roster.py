import sys 
import json
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_team_roster(): 
    with open("data/raw/cfbd/teams_roster_sample.json") as jsonroster: 
        result_roster = json.load(jsonroster)
    return result_roster

# print(load_team_roster())