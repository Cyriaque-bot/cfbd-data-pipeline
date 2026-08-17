import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.talent import fetch_talent

def parse_talent(raw_talent): 
    list_talent = []
    for i_talent in raw_talent: 
        dict_talent = {
            "school": i_talent["team"], 
            "season": int(i_talent["year"]), 
            "talent_score": float(i_talent["talent"])
        }
        list_talent.append(dict_talent)

    return list_talent


# valtaelnt = fetch_talent()
# print(parse_talent(valtaelnt))