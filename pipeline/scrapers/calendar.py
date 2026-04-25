import sys 
import os 

# J'ajoute la racine du projet au path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


from pipeline.loaders.load_calendar import load_calendar

def fetch_calendar(year): 
    return load_calendar(year)