import sys 
import os 
import json
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

def load_prime_time(): 
    with open("data/raw/cfbd/prime_time_sample.json") as json_prime_time:
         valprime_time = json.load(json_prime_time)
    return valprime_time

# print(load_prime_time())