import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_game_havoc import load_game_havoc

def fetch_game_havoc():
    return load_game_havoc()
