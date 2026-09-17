import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_game_advanced import load_game_advanced

def fetch_game_advanced():
    return load_game_advanced()

# print(fetch_game_advanced())