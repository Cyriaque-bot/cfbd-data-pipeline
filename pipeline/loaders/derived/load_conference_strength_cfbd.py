import sys
from pathlib import Path
import json 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_conference_strength_cfbd(): 
    with open("data/raw/derived/conference_strength_cfbd_sample.json") as json_conference_strength_cfbd: 
         result_conferene_strength  = json.load(json_conference_strength_cfbd)

    return result_conferene_strength


# print(load_conference_strength_cfbd())