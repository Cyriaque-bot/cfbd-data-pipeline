import sys
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_merge_havoc_stats import load_merge_games_havoc_stats


def fetch_merge_game_havoc_stats(): 
    return load_merge_games_havoc_stats()



