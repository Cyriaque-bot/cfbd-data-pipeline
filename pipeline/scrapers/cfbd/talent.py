import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.cfbd.load_talent import load_talent

def fetch_talent():
    return load_talent()


# print(fetch_talent())