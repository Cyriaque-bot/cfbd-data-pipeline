import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_returning_production_player_n_1 import load_returning_production_player_n_1

def fetch_returning_production_player_n_1(): 
    return load_returning_production_player_n_1()

# print(returning_production_player())