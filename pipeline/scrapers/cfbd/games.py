import os 
import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.cfbd.load_game import load_games
def fetch_games(): 
    return load_games()