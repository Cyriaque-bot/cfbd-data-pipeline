import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.analytics.coach.scraper_coach_rating import scrape_coach_rating

def parse_coach_rating(raw_coach_rating): 
    list_coach_rating = []
    for i_coach_rating in raw_coach_rating: 
        dict_coach_rating = {
            "school": i_coach_rating["school"], 
            "season": int(i_coach_rating["season"]), 
            "coach_rating_score": float(i_coach_rating["coach_rating"])
        }
        list_coach_rating.append(dict_coach_rating)

    return list_coach_rating

# val = scrape_coach_rating()

# print(parse_coach_rating(val))