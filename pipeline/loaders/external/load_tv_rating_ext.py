import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.tv_ratings_ext import fetch_tv_rating_ext

def load_tv_rating_ext(): 
    return fetch_tv_rating_ext()

# print(fetch_tv_rating())