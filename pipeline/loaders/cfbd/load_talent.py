import sys 
from pathlib import Path 
import json


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_talent(): 
    with open("data/raw/cfbd/talent_sample.json") as jsontalent:
        valltalent = json.load(jsontalent)
    return valltalent


# print(load_talent())