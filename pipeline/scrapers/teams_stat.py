import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root) 

from pipeline.loaders.load_teams_stats import load_teams_stats
def fetch_teams_stat(year): 
    return load_teams_stats()

# print(fetch_teams_stat(2023))