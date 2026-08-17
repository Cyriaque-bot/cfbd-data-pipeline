import sys 
from pathlib import Path 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.loaders.cfbd.load_season_advanced import load_season_advanced

def fetch_season_advanced(): 
    return load_season_advanced()

# print(fetch_season_advanced())