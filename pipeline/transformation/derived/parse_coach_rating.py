import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.derived.coach import fetch_coach_rating

def parse_coaching_rating(raw_derieved_coach_rating): 
    list_parse_coaching = []
    for i_coaching_rating in raw_derieved_coach_rating: 
        for j_coaching_rating in i_coaching_rating["seasons"]: 

            dict_parse_coaching = {
                "school": j_coaching_rating["school"], 
                "season": int(j_coaching_rating["year"]), 
                "games": int(j_coaching_rating["games"]), 
                "wins": int(j_coaching_rating["wins"]), 
                "losses": int(j_coaching_rating["losses"]), 
                "ties": int(j_coaching_rating["ties"]),
                "winPercentage": float(j_coaching_rating["winPercentage"]), 
                "preseasonRank": int(j_coaching_rating["preseasonRank"]), 
                "postseasonRank":int(j_coaching_rating["postseasonRank"]), 
                "srs": float(j_coaching_rating["srs"]), 
                "spOverall": float(j_coaching_rating["spOverall"]), 
                "spOffense": float(j_coaching_rating["spOffense"]), 
                "spDefense": float(j_coaching_rating["spDefense"])
            }
        
            list_parse_coaching.append(dict_parse_coaching)

    return list_parse_coaching 




# vallcoarating = fetch_coach_rating()

# print(parse_coaching_rating(vallcoarating))