from pathlib import Path
import sys 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_conference_affiliation(): 
    with open("data/raw/cfbd/conference_affiliation_sample.json") as json_conference_affiliation: 
        result_conference_affiliation  = json.load(json_conference_affiliation)
    return result_conference_affiliation

# print(load_conference_affiliation())