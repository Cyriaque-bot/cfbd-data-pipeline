from pathlib import Path 
import sys 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.cfbd.load_conference import load_conference
def fetch_conference(): 
    return load_conference()
