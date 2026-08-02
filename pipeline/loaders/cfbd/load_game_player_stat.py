import json
import os 
import sys 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root)


def load_games_players():
    with open("data/raw/games_players_stats_sample.json", "r") as jsonvalldata:
         valdata  = json.load(jsonvalldata)

    return valdata