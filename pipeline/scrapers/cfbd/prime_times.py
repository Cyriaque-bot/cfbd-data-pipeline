import sys 
# import os 
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_prime_time import load_prime_time

def fetch_prime_time(): 
    return load_prime_time()

