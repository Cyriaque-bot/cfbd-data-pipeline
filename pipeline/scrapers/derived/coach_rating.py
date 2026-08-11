import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_coach_rating import load_coach_ratings


def fetch_coach_rating(): 
    return load_coach_ratings()

