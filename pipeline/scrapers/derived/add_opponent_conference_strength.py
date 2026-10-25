import sys
from pathlib import Path



project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.derived.load_add_opponent_conference_strength import load_add_opponent_conference_strength

def fetch_add_opponent_conference_strength(): 
    return load_add_opponent_conference_strength()

# print(add_opponent_conference_strength())