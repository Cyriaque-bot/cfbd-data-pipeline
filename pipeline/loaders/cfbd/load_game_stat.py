import json 
import os
import sys

# Create the schemas 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

# define a function to load my jsondata

def load_games_stat(year, week): 
    with open("data/raw/games_stats.json") as jsongamestat: 
        valgames_stat = json.load(jsongamestat)

    return valgames_stat