import json 
import sys
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_team_season_overview():
    with open("data/raw/cfbd/team_season_overview_sample.json") as json_load_season_overwiew: 
        result_season_overwiew = json.load(json_load_season_overwiew)
    return result_season_overwiew

# print(load_season_overwiew())