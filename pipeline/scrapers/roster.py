import sys 
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

# from cfbd_client import get_rosters
from pipeline.loaders.load_rosters import loads_rosters
""" recupère les joueurs d'une saison via le client CFBD."""
def fetch_players(year):  
    return loads_rosters()

# print(fetch_players(2023))