import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.top25s import fetch_top25

def load_top25(): 
    return fetch_top25()


# print(load_top25())