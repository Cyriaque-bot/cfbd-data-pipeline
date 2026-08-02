import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.external.epas import fetch_epa

def load_epa(): 
    return fetch_epa()



