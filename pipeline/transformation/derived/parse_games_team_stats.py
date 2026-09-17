import sys
from pathlib import Path 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))




from pipeline.scrapers.derived.games_team_stats import fetch_games_team_stats

def parse_games_team_stats(raw_parse_games_team_stats): 
    return  raw_parse_games_team_stats


# val = fetch_games_team_stats()
# print(parse_games_team_stats(val))