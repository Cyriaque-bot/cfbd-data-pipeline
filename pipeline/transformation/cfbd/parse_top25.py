import sys 
from pathlib import Path 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.rankings import fetch_rankings

def parse_top25(raw_top25): 
    listmaxweek = []
    for i in raw_top25: 
         listmaxweek.append(i["week"])
    # return max(listmaxweek)
    list_top25 = []
    for i_top25 in raw_top25: 
        for j_top25 in i_top25["polls"]:
            if j_top25["poll"] == "AP Top 25": 
                for k_top25 in j_top25["ranks"]: 
                    if i_top25["week"] == max(listmaxweek):
                        dict_top25 = {
                            "team_id": int(k_top25["teamId"]),
                            "season" : i_top25["season"], 
                            "school" :  k_top25["school"], 
                            "top25_rank": int(k_top25["rank"]), 
                            "top25_score": float(1 - (k_top25["rank"])/25)       
                        }

                        list_top25.append(dict_top25)
    return list_top25


# vafetcf = fetch_rankings(2023)
# print(parse_top25(vafetcf))