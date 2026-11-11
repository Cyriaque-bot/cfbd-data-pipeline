import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_punting_team_season(): 
    with open("data/raw/cfbd/punting_team_season_sample.json") as json_punting_team_season: 
        result_json_punting_team_season = json.load(json_punting_team_season)
    return result_json_punting_team_season


# print(load_punting_team_season())