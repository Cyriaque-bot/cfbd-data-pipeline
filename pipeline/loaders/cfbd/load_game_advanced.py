import sys
from pathlib import Path
import json 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_game_advanced(): 
    with open("data/raw/cfbd/game_advanced_sample.json") as json_game_advanced: 
        result_game_advanced = json.load(json_game_advanced)
    return result_game_advanced

# print(load_game_advanced())