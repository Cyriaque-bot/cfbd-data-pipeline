import sys 
import os 

# J'ajoute la racine du projet au path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

# from cfbd_client import get_coaches
from pipeline.loaders.load_coaches import loads_coaches

def fetch_coaches(year):
    # recupère les coach d'une saison via le client CFBD
    # return get_coaches (year)
    return loads_coaches()
# test manuel 
# if __name__ == "__main__":
# print(fetch_coaches(2023))

