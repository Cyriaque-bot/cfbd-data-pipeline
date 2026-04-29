import os 
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


from pipeline.loaders.load_team_matchup import team_matchups

def fetch_load_team(year): 
    return team_matchups()

# print(fetch_load_team(2023))