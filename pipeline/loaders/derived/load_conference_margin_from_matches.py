import sys
from pathlib import Path 
import json 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_conference_margin_from_match(): 
    with open("data/raw/derived/conference_margin_from_matches_sample.json") as json_conference_margin_from_match: 
          result_json_conference_margin_from_match = json.load(json_conference_margin_from_match)
    return result_json_conference_margin_from_match

# print(load_conference_margin_from_match())