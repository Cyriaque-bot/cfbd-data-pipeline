import sys 
from pathlib import Path
import json 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_returning_production_player_n(): 
    with open("data/raw/derived/returning_production_player_n_sample.json") as json_returning_production_player_n: 
        result_json_returning_production_player_n = json.load(json_returning_production_player_n)
    return result_json_returning_production_player_n
