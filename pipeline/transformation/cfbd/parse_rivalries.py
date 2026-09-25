import sys 
import os
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def parse_rivalries(raw_rivalries): 
    list_rivalries = []

    importance_map = {
          "Major": 1,
          "Moderate": 0.7, 
          "Minor": 0.4
    }
    for i_rivalries in raw_rivalries: 
     
  
            valdictrivalries = {
                    "category": i_rivalries["category"], 
                    "rivalrie_name": i_rivalries["rivalry_name"],
                    "team": i_rivalries["teams"][0].lower(), 
                    "opponent": i_rivalries["teams"][1].lower(), 
                    "victory_team": int(i_rivalries["wins_team_1"]), 
                    "victory_opponent": int(i_rivalries["wins_team_2"]), 
                    "ties": int(i_rivalries["ties"]),
                    "series_leader": i_rivalries["series_leader"],
                    "trophy": i_rivalries["trophy"], 
                    "first_played" : int(i_rivalries["first_played"]), 
                    "total_game": int(i_rivalries["total_games"]), 
                    "intensity" : importance_map.get(i_rivalries["importance"], 0.4)
            }
            list_rivalries.append(valdictrivalries) 
     
    return list_rivalries




# from pipeline.scrapers.cfbd.rivalries import load_rivalries
# valresulrivalriese = load_rivalries()
# print(parse_rivalries(valresulrivalriese))