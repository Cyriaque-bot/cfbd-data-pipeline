import sys
from pathlib import Path 
import pandas as pd
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_conference_strength_ext import load_conference_strength_ext

def conference_strenght_ext():
    return load_conference_strength_ext()