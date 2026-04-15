import sys 
import os 
# Ajout de la racine du projet au path 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from cfbd_client import get_teams

def fetch_teams(year):
    """ Récupère les équipes d'une saison via le client CFBD"""
    return get_teams(year)


# Test manuel


# print(fetch_teams(2023))