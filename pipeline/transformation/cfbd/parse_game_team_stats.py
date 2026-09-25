import json 
import os 
import sys 
from pathlib import Path 
import re


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.game_team_stat import fetch_game_team_stats

def parse_game_team_stats(raw_game_team_stat): 
    val_list_game_team_one = [] 
    val_list_game_team_two = [] 
    val_final_game_team_list = []
    val_teams_one = {}
    val_teams_two = {}
    
    for i_game_team_stats in raw_game_team_stat:
                if len(i_game_team_stats["teams"]) == 0:
                   return "game been cancelled"
                elif len(i_game_team_stats["teams"]) == 1:
                   return "we got a bug because we got only one team"
                elif len(i_game_team_stats["teams"]) > 2: 
                   return "we got a bug because we got more than two team"
                
        # ma première étape avant tous les rassembler dans un dictionnaire        
                val_team_one_top = {
                   "game_id": int(i_game_team_stats["id"]), 
                   "team_id" : int(i_game_team_stats["teams"][0]["teamId"]), 
                   "team" : i_game_team_stats["teams"][0]["team"], 
                   "conference": i_game_team_stats["teams"][0]["conference"],
                   "home_away": i_game_team_stats["teams"][0]["homeAway"], 
                   "points":  int(i_game_team_stats["teams"][0]["points"]),
                }
                for i in i_game_team_stats["teams"][0]["stats"]: 
                        # val_teams_one.update({i["category"]: i["stat"]})
                    try: 
                        val_teams_one.update({i["category"]: int(i["stat"])})
                    except:
                            try: 
                                val_teams_one.update({i["category"]: float(i["stat"])})
                            except:
                                   val_teams_one.update({i["category"]: i["stat"]})        

                                   
                # new update 
                val_team_one_top.update(val_teams_one)
                # empty my dict
               
                val_list_game_team_one.append(val_team_one_top)
                val_teams_one.clear()

                # seconde step with ["teams"][1]

                val_team_two_top = {
                   "game_id": i_game_team_stats["id"], 
                   "team_id" : i_game_team_stats["teams"][1]["teamId"], 
                   "team" : i_game_team_stats["teams"][1]["team"], 
                   "conference": i_game_team_stats["teams"][1]["conference"],
                   "home_away": i_game_team_stats["teams"][1]["homeAway"], 
                   "points":  i_game_team_stats["teams"][1]["points"],
                }

                for i in i_game_team_stats["teams"][1]["stats"]: 
                       try:
                             val_teams_two.update({i["category"]: int(i["stat"])})
                       except:
                             try: 
                                   val_teams_two.update({i["category"]: float(i["stat"])})
                             except:
                                   val_teams_two.update({i["category"]: i["stat"]})
                # new update 
                val_team_two_top.update(val_teams_two)
                # empty my dict
               
                val_list_game_team_two.append(val_team_two_top)
                val_teams_two.clear()

   
    # update both list    
    val_int_game_team_list = val_list_game_team_one + val_list_game_team_two

        # uniformizing the name of all my key
    def camel_to_snake(normalisation): 
            val_insert_under = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', normalisation)
            val_insert_under_second = re.sub('([a-z0-9])([A-Z])', r'\1_\2', val_insert_under)
               
            return val_insert_under_second.lower()
    
    # reconstruction de la liste
    val_final_game_team_list = [
            {camel_to_snake(valnorml): valeur for valnorml, valeur in i.items()}
            for i in val_int_game_team_list
    ]
    
    return val_final_game_team_list
    

# val = fetch_game_team_stats()
# print(parse_game_team_stats(val))