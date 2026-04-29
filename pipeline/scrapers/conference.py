import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


from pipeline.loaders.load_conference import load_conference
def fetch_conference(year): 
    return load_conference()

#print(fetch_conference(load_conference))