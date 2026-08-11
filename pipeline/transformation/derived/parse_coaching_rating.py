import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.derived.coach_rating import fetch_coach_rating

def parse_coaching_rating(raw_derieved_coach_rating): 
    list_parse_coaching = []
    for i_coching_rating in raw_derieved_coach_rating: 
        dict_parse_coaching = {
            "school": i_coching_rating["school"], 
            "season": int(i_coching_rating["season"]), 
            "games": int(i_coching_rating["games"]), 
            "wins": int(i_coching_rating["wins"]), 
            "losses": int(i_coching_rating["losses"]), 
            "conference_wins": int(i_coching_rating["conference_wins"]), 
            "conference_losses": int(i_coching_rating["conference_losses"]), 
            "bowl_wins":int(i_coching_rating["bowl_wins"]), 
            "bowl_losses": int(i_coching_rating["bowl_losses"]), 
            "career_wins": int(i_coching_rating["career_wins"]), 
            "career_losses": int(i_coching_rating["career_losses"])
        }
        
        list_parse_coaching.append(dict_parse_coaching)

    return list_parse_coaching 




# vallcoarating = fetch_coach_rating()

# print(parse_coaching_rating(vallcoarating))