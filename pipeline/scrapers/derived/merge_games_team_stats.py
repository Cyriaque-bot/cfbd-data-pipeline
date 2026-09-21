import sys
from pathlib import Path 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_merge_games_team_stats import load_merge_games_team_stats

def fetch_merge_games_team_stats(): 
    return load_merge_games_team_stats()

# print(fetch_games_team_stats())