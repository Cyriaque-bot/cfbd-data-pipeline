import sys 
import os
from pathlib import Path 

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))


def parse_rivalries(rawrivalries): 
    valistrivalries = []
    for i, j in rawrivalries.items(): 
        for k in j: 
            valdictrivalries = {
            "team": k["team"], 
            "opponent": k["opponent"], 
            "rivalrie_name": k["name"]
            }
       

            valistrivalries.append(valdictrivalries) 
     
    return valistrivalries




# from pipeline.scrapers.rivalries import load_rivalries
# valresulrivalriese = load_rivalries()
# print(parse_rivalries(valresulrivalriese))