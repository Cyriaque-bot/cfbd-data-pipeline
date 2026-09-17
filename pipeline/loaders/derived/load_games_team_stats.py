import sys
from pathlib import Path 
import json

project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_games_team_stats(): 
    with open("data/raw/derived/merge_games_team_stats_sample.json") as json_games_team_stats: 
        result_games_team_stats = json.load(json_games_team_stats)
    return result_games_team_stats


# print(load_games_team_stats())