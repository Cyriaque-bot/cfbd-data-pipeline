import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.cfbd.load_coach import load_coach

def fetch_coach():
    return load_coach()

# print(fetch_coach())