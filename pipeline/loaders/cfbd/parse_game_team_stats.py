import json 
import os 
import sys 
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.game_team_stat import fetch_game_team_stats

def parse_game_team_stats(raw_game_team_stat): 
    val_game_team_stat = []
    
    for i_game_team_stats in raw_game_team_stat: 
        for key_game in i_game_team_stats["teams"]: 
            for key_game_stat, val_game_stat in key_game.items(): 
                if key_game_stat == "stats": 
                   for i in val_game_stat: 
                       for j_key , val_key in i.items(): 
                           if j_key == "category" and  j_key == "stat" : 
                             dict_intermediate = {
                                 "total_yards" : val_key, 
                                 "rushing_ards": val_key
                             }
                             return dict_intermediate   








val = fetch_game_team_stats()
print(parse_game_team_stats(val))