import sys
from pathlib import Path 
import pandas as pd
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.external.conference_strenght_ext import conference_strenght_ext

def parse_conference_strength_ext(raw_conference_strength): 
    list_conference_strength = []
    for i_conference_strength in raw_conference_strength: 
        dict_conference_strength = {
            "team": i_conference_strength["team"],
            "conference" : i_conference_strength["conference"],
            "conference_strength_score": i_conference_strength["conference_strength_score"]
        }

        list_conference_strength.append(dict_conference_strength)

    return list_conference_strength

# val = conference_strenght_ext()
# print(parse_conference_strength_ext(val))