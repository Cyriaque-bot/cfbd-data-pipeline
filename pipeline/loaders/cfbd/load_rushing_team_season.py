import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_rushing_team_season(): 
    with open("data/raw/cfbd/rushing_team_season_sample.json") as json_rushing_team_season: 
        result_json_rushing_team_season = json.load(json_rushing_team_season)
    return result_json_rushing_team_season

# print(load_rushing_team_season())