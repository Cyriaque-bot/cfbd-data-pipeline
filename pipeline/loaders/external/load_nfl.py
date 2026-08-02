import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.nfls import fetch_nfl

def load_nfl(): 
    return fetch_nfl()

# print(load_nfl())