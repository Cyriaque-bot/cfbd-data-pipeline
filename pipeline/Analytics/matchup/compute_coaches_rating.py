import sys 
from pathlib import Path
import json
import pandas as pd 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.coach import fetch_coach_rating
from pipeline.transformation.derived.parse_coach_rating import parse_coaching_rating


def compute_coach_rating(raw_coaching_list): 
    list_compute_coach_rating_int = []
    for i_compute_coach_rating in raw_coaching_list: 
       

        dict_compute_coach_rating = {
            "int_school": i_compute_coach_rating["school"], 
            "int_season": i_compute_coach_rating["season"], 
            "int_games": i_compute_coach_rating["games"],
            "int_wins": i_compute_coach_rating["wins"], 
            "int_losses": i_compute_coach_rating["losses"], 
            "int_ties": i_compute_coach_rating["ties"], 
            "int_win_percentage": i_compute_coach_rating["winPercentage"], 
            "int_preseasonRank": i_compute_coach_rating["preseasonRank"],
            "int_postseasonRank": i_compute_coach_rating["postseasonRank"], 
            "int_srs": i_compute_coach_rating["srs"], 
            "int_spOverall": i_compute_coach_rating["spOverall"],
            "int_spOffense": i_compute_coach_rating["spOffense"],
            "int_spDefense": i_compute_coach_rating["spDefense"],
            "coach_rating": None 
        }
        list_compute_coach_rating_int.append(dict_compute_coach_rating)

    #################### min max for srs ,sp , ranking  #####################

    # min max for srs 
    list_srs = []
    for i_list_srs in list_compute_coach_rating_int: 
        list_srs.append(i_list_srs["int_srs"])
    max_list_srs = max(list_srs)
    min_list_srs = min(list_srs)
  
    # min max  for sp 
    list_spOverall = []
    for i_list_spOverall in list_compute_coach_rating_int: 
        list_spOverall.append(i_list_spOverall["int_spOverall"])
    max_list_spOverall = max(list_spOverall)
    min_list_spOverall = min(list_spOverall)

 

    #################### Normalization for srs ,sp , ranking  #####################

    # Normalization for srs
    if max_list_srs == min_list_srs: 
        normalized_srs_deno = 0.5
    else: 
        normalized_srs_deno = max_list_srs - min_list_srs

    # Normalization for spOverall
    if max_list_spOverall == min_list_spOverall:
        normalized_spOverall_deno = 0.5
    else:
        normalized_spOverall_deno = max_list_spOverall - min_list_spOverall

  
 

    
    list_compute_coach_rating_final = []

    for i_final_list in list_compute_coach_rating_int: 
        dict_final_list = {
            "school": i_final_list["int_school"], 
            "season": i_final_list["int_season"],  
            "coach_rating": round
                                  ( 0.40 * i_final_list["int_win_percentage"] 
                                  + 0.20 * (i_final_list["int_wins"]/ i_final_list["int_games"])
                                  + 0.15 * ((i_final_list["int_srs"] - min_list_srs)/ normalized_srs_deno)
                                  + 0.15 * ((i_final_list["int_spOverall"] - min_list_spOverall)/ normalized_spOverall_deno)
                                  + 0.10 * ((i_final_list["int_preseasonRank"] - i_final_list["int_postseasonRank"])/ i_final_list["int_preseasonRank"]), 
                                  3
            ) 
            
        }
        list_compute_coach_rating_final.append(dict_final_list)

     
    with open("data/raw/derived/coach_rating_sample.json", "w") as jsonwritecoach: 
        json.dump(list_compute_coach_rating_final, jsonwritecoach, indent = 4)
  
          
    return list_compute_coach_rating_final


        

     


# vallfetc = fetch_coach_rating()
# valparse = parse_coaching_rating(vallfetc)

# print(compute_coach_rating(valparse))
