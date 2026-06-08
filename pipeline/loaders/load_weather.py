import json 
import os
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

def load_weather(): 
    with open("data/raw/weather_sample.json", "r") as jsonweather: 
        valweathers = json.load(jsonweather)
    return valweathers 

# print(load_weather())   
   