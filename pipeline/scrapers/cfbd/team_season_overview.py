from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.cfbd.load_team_season_overview import load_team_season_overview

def fetch_team_season_overview(): 
    return load_team_season_overview()

# print(fetch_team_season_overwiew())