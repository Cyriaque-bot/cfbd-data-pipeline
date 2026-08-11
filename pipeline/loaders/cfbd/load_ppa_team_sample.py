import json
from pathlib import Path
import sys

projec_root = Path(__file__).resolve().parents[3]
sys.path.append(str(projec_root))


def load_ppa_team():
    with open("data/raw/cfbd/ppa_teams_sample.json") as jsonppa_team:
        valljsonppateam = json.load(jsonppa_team)
    return valljsonppateam

# print(load_ppa_team())