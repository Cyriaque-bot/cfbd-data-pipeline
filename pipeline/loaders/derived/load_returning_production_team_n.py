import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_returning_production_team_n(): 
    with open("data/raw/derived/returning_production_team_n_sample.json") as json_returning_production_team_n: 
        result_returning_production_team_n = json.load(json_returning_production_team_n)
    return result_returning_production_team_n

# print(load_returning_production_team_n())