import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.loaders.external.load_top25 import load_top25

def parse_top25(): 
    list_top25 = []

    result_top25 = load_top25()

    # more elegant way to do 
    def to_int_or_nr(valuenr): 
        return None if valuenr == "NR" else int(valuenr)

    for i in result_top25: 
        
        dict_top25 = {
            "team": i["team"], 
            "season": int(i["season"]), 
            "ap_rank": to_int_or_nr(i["ap_rank"]),
            "coaches_rank": to_int_or_nr(i["coaches_rank"]), 
            "weeks_ranked": int(i["weeks_ranked"]), 
            "weeks_top10": int(i["weeks_top10"]),
            "final_rank": to_int_or_nr(i["final_rank"]), 
            "rank_value_score": int(i["rank_value_score"])
    
        }
      
    
        list_top25.append(dict_top25)

    return list_top25


print(parse_top25())