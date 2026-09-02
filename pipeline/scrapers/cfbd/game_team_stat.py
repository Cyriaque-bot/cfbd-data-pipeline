import os 
import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_game_team_stat import load_game_team_stats
def fetch_game_team_stats(): 
    return load_game_team_stats()

# print(fetch_teams_stat(all))