import json 
import os 
import sys 


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


def load_team_game_stats(): 
    with open("data/raw/cfbd/team_game_stats_sample.json", "r") as teams_statsjson: 
        vallteamstats = json.load(teams_statsjson)
    return vallteamstats