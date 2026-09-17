import sys
from pathlib import Path
import json 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_game_havoc(): 
    with open("data/raw/cfbd/game_havoc_sample.json") as json_game_havoc: 
        result_game_havoc = json.load(json_game_havoc)
    return result_game_havoc

# print(load_game_havoc())