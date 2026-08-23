import sys 
from pathlib import Path
import csv


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_recruiting_external import load_recruiting_external

def parse_recruiting_external(): 
    path_recruiting_external = "data/processed/external/recruiting_external_processed.csv"
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
            "avg_rating": float(i["avg_rating"]), 
            "roster_value": float(i["roster_value"]), 
            "nfl_projection": float(i["nfl_projection"]), 
            "position_value": float(i["position_value"])
        }
        list_recruiting_external.append(dict_recruiting_external)

    with open(path_recruiting_external, "w", newline = "", encoding = "utf-8") as recruiting_external_csv: 

        recruiting_external_field = [
            "team", 
            "season", 
            "talent_composite",
            "blue_chip_ratio",
            "stars_5", 
            "stars_4", 
            "stars_3", 
            "transfers_in", 
            "transfers_out", 
            "avg_rating", 
            "roster_value", 
            "nfl_projection", 
            "position_value"
        ]

        writer_recruiting_external = csv.DictWriter(recruiting_external_csv, fieldnames = recruiting_external_field)
        writer_recruiting_external.writeheader()
        writer_recruiting_external.writerows(list_recruiting_external)

    return f"le fichier à été copié avec succès vous pouvez le vérifier dans {path_recruiting_external}"

# print(parse_recruiting_external())
