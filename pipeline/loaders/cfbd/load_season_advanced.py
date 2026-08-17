import sys 
from pathlib import Path 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_season_advanced(): 
    with open("data/raw/cfbd/season_advanced.json") as jsonseason_advanced:
        valseason_advanced = json.load(jsonseason_advanced)

    return valseason_advanced

# print(load_season_advanced())