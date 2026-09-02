import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def scrape_coach_rating(): 

    with open("data/raw/derived/coach_rating_sample.json") as jsoncoach_rating: 
        result_coach_rating = json.load(jsoncoach_rating)

    return result_coach_rating

# print(scrape_coach_rating())