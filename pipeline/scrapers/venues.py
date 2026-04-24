import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

# from cfbd_client import get_venues
from pipeline.loaders.load_venues import loads_venues

def fecth_venues(year): 
    # return get_venues()
     return loads_venues()
# print(fecth_venues())