import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.derived.load_team_top25 import load_team_top25

def fetch_team_top25(): 
    return load_team_top25()

# print(fetch_team_top25()) 