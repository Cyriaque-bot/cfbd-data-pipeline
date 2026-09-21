import sys
from pathlib import Path 
import json

project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def load_merge_games_havoc_stats(): 
    with open("data/raw/derived/merge_game_havoc_stats_sample.json") as json_games_havoc_stats: 
        result_games_havoc_stats = json.load(json_games_havoc_stats)
    return result_games_havoc_stats


# print(load_merge_games_havoc_stats())