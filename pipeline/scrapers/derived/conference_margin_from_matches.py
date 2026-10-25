import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.derived.load_conference_margin_from_matches import load_conference_margin_from_match

def fetch_conference_margin(): 
    return load_conference_margin_from_match()

# print(fetch_conference_margin())