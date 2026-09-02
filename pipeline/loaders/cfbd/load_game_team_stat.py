import json 
import os 
import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def load_game_team_stats(): 
    with open("data/raw/cfbd/game_team_stats_sample.json", "r") as teams_statsjson: 
        vallteamstats = json.load(teams_statsjson)
    return vallteamstats

# print(load_game_team_stats())