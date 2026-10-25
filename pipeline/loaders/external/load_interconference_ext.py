import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.interconferences_ext import fetch_interconference_ext

def load_interconference_ext(): 
    return fetch_interconference_ext()

# print(load_interconference())
