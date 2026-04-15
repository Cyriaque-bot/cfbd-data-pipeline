import sys
import os 

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Chemin vers le fichier actuel Y:/.../pipeline/scrapers/matches.py
# Le dossier cu fichier Y:/.../pipeline/scrapers
# remonter d'un dossier os.path.join(os.path.dirname(__file__), "..")
# convertir en chemin absolue os.path.abspath(...)
# et donc en définitive il contient le chemin exact du dossier racine du projet, celui ou se trouve cfbd_client.py
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from cfbd_client import get_games

""" recupère les matchs d'une saison via le client CFBD."""
def fetch_matches(year):
    data = get_games(year)
    return data 


# test manuel (Je peux le supprimer plus tard)
if __name__ == "__main__":
    print(fetch_matches(2023))


# print("sys.path =")
# for p in sys.path:
#     print("  ", p)
