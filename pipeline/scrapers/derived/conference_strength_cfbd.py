import pandas as pd 
from pathlib import Path 
import sys 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.derived.load_conference_strength_cfbd import load_conference_strength_cfbd

def fetch_conference_strength_cfbd(): 
    return  load_conference_strength_cfbd()

# print(conference_strength_cfbd())