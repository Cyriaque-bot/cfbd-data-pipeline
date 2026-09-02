from pathlib import Path
import sys



project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_teams_roster import load_team_roster

def fetch_team_roster(): 
    return load_team_roster()
