import sys
from pathlib import Path 
import csv


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_tv_rating import load_tv_rating

def parse_tv_rating(): 
    path_tv_rating = "data/processed/external/tv_rating_processed.csv"
    list_tv_rating = []

    result_tv_rating = load_tv_rating()

    for i in result_tv_rating: 
        dict_tv_rating = {
            "team": i["team"], 
            "season": int(i["season"]), 
            "avg_viewers": float(i["avg_viewers"]), 
            "peak_viewers": float(i["peak_viewers"]), 
            "prime_time_games":int(i["prime_time_games"]), 
            "network_exposure": float(i["network_exposure"]), 
            "tv_value_score": int(i["tv_value_score"]), 
            "market_size": float(i["market_size"]), 
            "network_importance": float(i["network_importance"])
        }
        list_tv_rating.append(dict_tv_rating)
  

    with open(path_tv_rating, "w", newline = "", encoding = "utf-8")as tv_rating_csv:
            tv_rating_fields = [
                "team", 
                "season",
                "avg_viewers",
                "peak_viewers", 
                "prime_time_games", 
                "network_exposure", 
                "tv_value_score", 
                "market_size", 
                "network_importance"
            ]

            write_tv_rating = csv.DictWriter(tv_rating_csv, fieldnames = tv_rating_fields)
            write_tv_rating.writeheader()
            write_tv_rating.writerows(list_tv_rating)
    return f"🤸félicitation le fichier a été compié dans {path_tv_rating}"

print(parse_tv_rating())