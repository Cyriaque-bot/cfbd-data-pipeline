import sys 
from pathlib import Path

# added project_root to the root of sys.path
project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


# from cfbd_client import get_teams
from pipeline.loaders.cfbd.load_team import loads_teams

def fetch_teams(year):
    """ Récupère les équipes d'une saison via le client CFBD"""
    # return get_teams(year)
    return loads_teams()

# print(fetch_teams(all))