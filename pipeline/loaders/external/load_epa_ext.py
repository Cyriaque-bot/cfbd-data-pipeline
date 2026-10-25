import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.external.epas_ext import fetch_epa_ext

def load_epa_ext(): 
    return fetch_epa_ext()



