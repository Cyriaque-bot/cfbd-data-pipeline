import sys 
import os 
# added project_root to the root of sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


# from cfbd_client import get_teams
from pipeline.loaders.load_teams import loads_teams

def fetch_teams(year):
    """ Récupère les équipes d'une saison via le client CFBD"""
    # return get_teams(year)
    return loads_teams()

