import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_returning_production_player_n import load_returning_production_player_n

def fetch_returning_production_player_n(): 
    return load_returning_production_player_n()