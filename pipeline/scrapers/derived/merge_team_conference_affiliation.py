import sys
from pathlib import Path
import json


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_merge_team_conference_affiliation import load_merge_team_conference_affiliation

def fetch_merge_team_conference_affiliation(): 
    return load_merge_team_conference_affiliation()

# print(fetch_merge_team_conference_affiliation())