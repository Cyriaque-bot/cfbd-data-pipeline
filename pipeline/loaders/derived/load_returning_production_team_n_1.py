import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_returning_production_team_n_1(): 
    with open("data/raw/derived/returning_production_team_n_1_sample.json") as json_rereturning_production_team_n_1: 
        result_rereturning_production_team_n_1 =  json.load(json_rereturning_production_team_n_1) 
    return result_rereturning_production_team_n_1
# print(load_returning_production_team_n_1())