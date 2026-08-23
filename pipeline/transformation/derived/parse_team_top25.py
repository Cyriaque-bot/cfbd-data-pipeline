import sys
from pathlib import Path 
import pandas as pd
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_team_top25 import load_team_top25

def parse_team_top25(raw_team_top): 
    list_team_top25 = []

    for i_team_top25 in raw_team_top: 
        dict_team_top = {
            "team_id" : int(i_team_top25["id"]), 
            "school" : i_team_top25["school"], 
            "top25_rank": i_team_top25["top25_rank"], 
            "top25_score":  float(i_team_top25["top25_score"])
        }
        list_team_top25.append(dict_team_top)
        
    return list_team_top25

val = load_team_top25()
print(parse_team_top25(val)) 