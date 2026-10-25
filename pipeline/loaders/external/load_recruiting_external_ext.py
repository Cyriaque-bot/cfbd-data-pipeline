import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.external.recruiting_externals_ext import fetch_recruiting_external_ext

def load_recruiting_external_ext(): 
    return fetch_recruiting_external_ext()

# print(fetch_recruiting_external())