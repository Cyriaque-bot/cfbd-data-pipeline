import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.nfls_ext import fetch_nfl_ext

def load_nfl_ext(): 
    return fetch_nfl_ext()

# print(load_nfl())