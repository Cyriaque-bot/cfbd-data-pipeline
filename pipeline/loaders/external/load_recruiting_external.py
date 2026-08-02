import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.recruiting_externals import fetch_recruiting_external

def load_recruiting_external(): 
    return fetch_recruiting_external()

# print(fetch_recruiting_external())