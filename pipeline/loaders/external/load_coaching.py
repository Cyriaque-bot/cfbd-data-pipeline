import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.coachings import fetch_coaching

def load_coaching(): 
    return fetch_coaching()

print(load_coaching())
