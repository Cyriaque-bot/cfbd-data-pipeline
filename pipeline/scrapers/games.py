import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)



from pipeline.loaders.load_games import load_games
def fecth_games(year): 
    return load_games()