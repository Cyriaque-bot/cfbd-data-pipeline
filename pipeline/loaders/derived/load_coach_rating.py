import sys 
from pathlib import Path
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_coach_ratings(): 
    with open("data/raw/cfbd/coaches_sample.json") as jsoncoacrating: 
        vallcoach_ratings = json.load(jsoncoacrating)
    return vallcoach_ratings

# print(load_coach_ratings())