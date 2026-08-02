import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.interconferences import fetch_interconference

def load_interconference(): 
    return fetch_interconference()

# print(load_interconference())
