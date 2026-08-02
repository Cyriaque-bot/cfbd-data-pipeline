import os 
import sys
from pathlib import Path 

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_weather import load_weather

def fetch_weather(season): 
    return load_weather() 



# print(fetch_weather(2023))