import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root)) 

from pipeline.loaders.cfbd.load_conference_affiliation import load_conference_affiliation

def fetch_conference_affiliation(): 
    return load_conference_affiliation()


# print(conference_affiliation())