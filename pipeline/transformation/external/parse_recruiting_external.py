import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_recruiting_external import load_recruiting_external

def parse_recruiting_external(): 
    list_recruiting_external = []
    result_recruiting_external = load_recruiting_external()
    # return result_recruiting_external
    for i in result_recruiting_external: 
        dict_recruiting_external = {
            "team": i["team"], 
            "season": int(i["season"]),
            "talent_composite": int(i["talent_composite"]), 
            "blue_chip_ratio": float(i["blue_chip_ratio"]),
            "stars_5": int(i["stars_5"]), 
            "stars_4": int(i["stars_4"]), 
            "stars_3": int(i["stars_3"]), 
            "transfers_in": int(i["transfers_in"]), 
            "transfers_out": int(i["transfers_out"]), 
            "avg_rating": float(i["avg_rating"])
        }
        list_recruiting_external.append(dict_recruiting_external)

    return list_recruiting_external

