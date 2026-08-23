import sys 
import csv 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.external.recruiting_externals import fetch_recruiting_external

def parse_talent_score(raw_talent_score): 
    list_talent_score = []
    list_talent_composite = []

    # normalising talent composite
    for i_talent_score  in raw_talent_score: 
        val_talent_composite =  i_talent_score["talent_composite"] 
        list_talent_composite.append(val_talent_composite)

    # max_talent_composite and min_talent_composite
    max_talent_composite = max(list_talent_composite)
    min_talent_composite = min(list_talent_composite)

    for j_talent_score in raw_talent_score: 
        dict_talent_score = {
            "school": j_talent_score["team"], 
            "talent_score":round(( 0.35 * ((j_talent_score["talent_composite"] - min_talent_composite)/(max_talent_composite - min_talent_composite)) + 
                              0.15 * j_talent_score["blue_chip_ratio"] +
                              0.10 * j_talent_score["avg_rating"] + 
                              0.10 * ((j_talent_score["stars_5"])/ (j_talent_score["stars_5"] + j_talent_score["stars_4"] + j_talent_score["stars_3"])) + 
                              0.10 * ((j_talent_score["transfers_in"])/ (j_talent_score["transfers_in"] + j_talent_score["transfers_out"])) +
                              0.10 * j_talent_score["roster_value"] +
                              0.05 * j_talent_score["nfl_projection"] +
                              0.05 * j_talent_score["position_value"]
                            ) , 2
            )       
                            }  
        list_talent_score.append(dict_talent_score)
         
           
    

    return list_talent_score

valtalent_compo = fetch_recruiting_external()
print(parse_talent_score(valtalent_compo))