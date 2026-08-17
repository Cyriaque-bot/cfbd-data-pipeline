import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_ppa_team import load_ppa_team

def fetch_ppa_team(): 
    return load_ppa_team()

# print(fetch_ppa_team())