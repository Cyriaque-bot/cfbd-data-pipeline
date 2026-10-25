import sys
from pathlib import Path
import json


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))
def load_add_opponent_conference_strength(): 
    with open("data/raw/derived/add_opponent_conference_strength_sample.json") as json_add_opponent_conference: 
        result_add_json_opponent_conference  = json.load(json_add_opponent_conference)
    return result_add_json_opponent_conference

# print(load_add_opponent_conference_strength())