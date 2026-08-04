import sys
import json
from pathlib import Path 
import csv 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_epa import load_epa




def parse_epa(): 
    path_epa = "data/processed/external/epa_processed.csv"
    list_epa = []
    # taking my data from load_epa
    result_parse_epa = load_epa()
    for i in result_parse_epa: 
        dict_parse_epa = {
            "team": i["team"], 
            "season": int(i["season"]), 
            "off_epa": float(i["off_epa"]), 
            "def_epa": float(i["def_epa"]), 
            "net_epa": float(i["net_epa"]), 
            "success_rate":  float(i["success_rate"]), 
            "explosiveness": float(i["explosiveness"]), 
            "ppa": float(i["ppa"]), 
            "plays": int(i["plays"])
        }  
     
        list_epa.append(dict_parse_epa)

    with open(path_epa, "w", newline = "", encoding = "utf-8") as epa_csv: 
        epa_field = [
            "team", 
            "season", 
            "off_epa", 
            "def_epa", 
            "net_epa",
            "success_rate", 
            "explosiveness",
            "ppa", 
            "plays"
        ]

        write_epa = csv.DictWriter(epa_csv, fieldnames = epa_field)
        write_epa.writeheader()
        write_epa.writerows(list_epa)
               
       
       
   
    return f"🤸 le fichier a été copié avec success, vous pouvz vétifier {path_epa}"


