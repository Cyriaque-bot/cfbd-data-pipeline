import json 
import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def load_conference():
    with open("data/raw/cfbd/conference_sample.json") as jsonconference: 
        vallconference = json.load(jsonconference)
    return vallconference

# print(load_conference())