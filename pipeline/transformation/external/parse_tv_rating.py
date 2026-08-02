import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_tv_rating import load_tv_rating

def parse_tv_rating(): 
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
            "tv_value_score": int(i["tv_value_score"])
        }
        list_tv_rating.append(dict_tv_rating)

    return list_tv_rating