import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.tv_ratings import fetch_tv_rating

def load_tv_rating(): 
    return fetch_tv_rating()

# print(fetch_tv_rating())