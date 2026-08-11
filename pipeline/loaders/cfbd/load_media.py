import json
from pathlib import Path 
import sys


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def load_media(): 
    with open("data/raw/cfbd/media_sample.json") as jsonmedia: 
        vallmedia = json.load(jsonmedia)
    return vallmedia


# print(load_media())