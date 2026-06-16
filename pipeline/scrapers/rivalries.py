import sys
import os 
from pathlib import Path 


project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from pipeline.loaders.load_rivalries import load_rivalries
def fetch_rivalries(): 
    return load_rivalries()


# print(fetch_rivalries())