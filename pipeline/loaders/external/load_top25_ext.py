import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.top25s_ext import fetch_top25_ext

def load_top25_ext(): 
    return fetch_top25_ext()


# print(load_top25())