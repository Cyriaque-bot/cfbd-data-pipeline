import sys
from pathlib import Path 
import csv

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_interconference import load_interconference

def parse_interconference(): 
    path_inteconference = "data/processed/external/inteconference_processed.csv"
    list_interconference = []

    result_interconference = load_interconference()

    for i in result_interconference: 
        dict_interconference = {
            "conference": i["conference"], 
            "season": int(i["season"]), 
            "wins_vs_power5": int(i["wins_vs_power5"]), 
            "losses_vs_power5": int(i["losses_vs_power5"]), 
            "wins_vs_group5": int(i["wins_vs_group5"]), 
            "losses_vs_group5": int(i["losses_vs_group5"]),
            "avg_margin_power5": float(i["avg_margin_power5"]), 
            "avg_margin_group5": float(i["avg_margin_group5"]), 
            "interconf_value_score": int(i["interconf_value_score"])
        }

        list_interconference.append(dict_interconference)

    with open(path_inteconference, "w", newline = "") as interconference_csv: 
        interconference_field = [
            "conference", 
            "season", 
            "wins_vs_power5", 
            "losses_vs_power5", 
            "wins_vs_group5", 
            "losses_vs_group5", 
            "avg_margin_power5", 
             "avg_margin_group5",
            "interconf_value_score"
           ]
        writer_interconference = csv.DictWriter(interconference_csv, fieldnames = interconference_field)
        writer_interconference.writeheader()
        writer_interconference.writerows(list_interconference)
        
    return f"🤸 inteconference_processed.csv généré dans {path_inteconference}"
