from pathlib import Path
import sys

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_stats_player_season import load_stat_player

def fetch_stats_player_season(): 
    return load_stat_player()

# print(fetch_stats_player_season())