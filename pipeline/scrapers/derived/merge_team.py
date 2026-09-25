import sys
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.derived.load_merge_team import load_merge_team

def fetch_merge_team(): 
    return load_merge_team()
# print(fetch_merge_team())