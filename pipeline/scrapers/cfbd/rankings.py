from pathlib import Path
import sys


project_root =  Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

# from cfbd_client import get_rankings
from pipeline.loaders.cfbd.load_ranking import load_rankings

def fetch_rankings():
    return load_rankings()

