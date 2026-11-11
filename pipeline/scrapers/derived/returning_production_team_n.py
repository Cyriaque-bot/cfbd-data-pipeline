import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.derived.load_returning_production_team_n import load_returning_production_team_n

def fetch_returning_production_team_n(): 
    return load_returning_production_team_n()

# print(fetch_returning_production_team())