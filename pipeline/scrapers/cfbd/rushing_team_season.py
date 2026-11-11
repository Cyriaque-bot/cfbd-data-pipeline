import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.cfbd.load_rushing_team_season import load_rushing_team_season

def fetch_rushing_team_season(): 
    return load_rushing_team_season()

# print(fetch_rushing_team_season())