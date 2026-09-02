import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.analytics.team_strength.scraper_team_top25 import scraper_team_top25

def parse_team_top25(raw_team_top25): 
    list_team_top25 = []

    for i_team_top25 in raw_team_top25: 
       dict_team_top25 = {
       "school": i_team_top25["school"], 
       "top25_score": i_team_top25["top25_score"]
    }
       list_team_top25.append(dict_team_top25)

    return list_team_top25

# vajj = scraper_team_top25()

# print(parse_team_top25(vajj))