import sys
import json
from pathlib import Path 



project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_nfl import load_nfl

def parse_nfl(): 

    list_nfl = []
    result_nfl = load_nfl()

    for i in result_nfl: 
        dict_nfl = {
            "team": i["team"], 
            "season": int(i["season"]), 
            "nfl_players_active": int(i["nfl_players_active"]), 
            "nfl_players_total": int(i["nfl_players_total"]), 
            "nfl_draft_last5": int(i["nfl_draft_last5"]), 
            "nfl_value_score": int(i["nfl_value_score"]), 
            "nfl_starters": int(i["nfl_starters"]), 
            "avg_nfl_rating": float(i["avg_nfl_rating"])
        }
        list_nfl.append(dict_nfl)

    return list_nfl

print(parse_nfl())
 