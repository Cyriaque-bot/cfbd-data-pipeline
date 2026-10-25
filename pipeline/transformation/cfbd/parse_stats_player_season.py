import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.stats_player_season import fetch_stats_player_season

def parse_stats_player_season(raw_stats_player_season): 
    list_stats_player_season = []

    for i_stats_player_season in raw_stats_player_season: 
        dict_stats_player_season = {
            "season": i_stats_player_season["season"], 
            "player_id": i_stats_player_season["playerId"], 
            "player": i_stats_player_season["player"], 
            "position": i_stats_player_season["position"], 
            "team": i_stats_player_season["team"], 
            "conference": i_stats_player_season["conference"], 
            "category": i_stats_player_season["category"], 
            "stat_type": i_stats_player_season["statType"], 
            "stat": i_stats_player_season["stat"]
        }
        list_stats_player_season.append(dict_stats_player_season)

    return list_stats_player_season

# val = fetch_stats_player_season()
# print(parse_stats_player_season(val))