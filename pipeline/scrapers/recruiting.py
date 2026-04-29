import sys
import os 

# recupération de mon project_root 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


# invitation de mon cfbd pour la récupération des données 
# from cfbd_client import get_recruiting

from pipeline.loaders.load_recruiting import load_recruiting

def fetch_get_recruiting(year): 
    data =  load_recruiting(year)
    if not data:
       print(f"Aucune donnée de recrutement trouvée pour {year}")
       return []
    return data 

