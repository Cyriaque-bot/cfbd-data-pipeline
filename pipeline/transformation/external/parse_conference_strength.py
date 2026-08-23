import sys
from pathlib import Path 
import pandas as pd
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.external.load_conference_strength import load_conference_strength

def parse_conference_stength(raw_conference_strength): 
    list_conference_strength = []
    for i_conference_strength in raw_conference_strength: 
        dict_conference_strength = {
            "conference" : i_conference_strength["conference"],
            "conference_strength_score": float(i_conference_strength["conference_strength_score"])
        }

        list_conference_strength.append(dict_conference_strength)

    return list_conference_strength

# val = load_conference_strength()
# print(parse_conference_stength(val))