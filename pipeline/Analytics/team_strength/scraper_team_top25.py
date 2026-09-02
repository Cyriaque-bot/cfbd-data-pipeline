import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def scraper_team_top25(): 
    with open("data/raw/derived/team_top25_sample.json") as jsonteam_top25: 
        result_team_top25 = json.load(jsonteam_top25)
    return result_team_top25

# print(scraper_team_top25())