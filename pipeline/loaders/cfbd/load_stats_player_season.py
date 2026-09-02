import sys
from pathlib import Path 
import json


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_stat_player(): 
    with open("data/raw/cfbd/stats_player_season_sample.json", "r") as jsonseasonplayer: 
        result_stat_player = json.load(jsonseasonplayer)
    return result_stat_player

# print(load_stat_player())