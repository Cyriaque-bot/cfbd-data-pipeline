import sys
import json
from pathlib import Path 
import csv 



project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_nfl import load_nfl

def parse_nfl(): 
    path_nfl = "data/processed/external/nfl_processed.csv"
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

   

    with open(path_nfl, "w", newline = "", encoding = "utf-8") as nfl_csv: 

        nfl_field = [
            "team", 
            "season", 
            "nfl_players_active", 
            "nfl_players_total", 
            "nfl_draft_last5", 
            "nfl_value_score", 
            "nfl_starters", 
            "avg_nfl_rating"
        ]

        writer_nfl = csv.DictWriter(nfl_csv, fieldnames = nfl_field)
        writer_nfl.writeheader()
        writer_nfl.writerows(list_nfl)

    return f"🤸 coaching_processed.csv généré dans {path_nfl}"

