import sys
import os 

project_root =  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# from cfbd_client import get_rankings
from pipeline.loaders.load_rankings import load_rankings

def fetch_rankings(year):
    return load_rankings()

# print(fetch_rankings(2023))