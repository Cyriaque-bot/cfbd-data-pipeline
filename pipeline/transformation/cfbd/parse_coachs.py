import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.coachs import fetch_coach

def parse_coachs(raws_coachs): 
    list_parse_coachs = []
    for i_coachs in raws_coachs: 
        for j_coach in i_coachs["seasons"]: 

            dict_parse_coachs = {
                "school": j_coach["school"], 
                "season": int(j_coach["year"]), 
                "games": int(j_coach["games"]), 
                "wins": int(j_coach["wins"]), 
                "losses": int(j_coach["losses"]), 
                "ties": int(j_coach["ties"]),
                "winPercentage": float(j_coach["winPercentage"]), 
                "preseasonRank": int(j_coach["preseasonRank"]), 
                "postseasonRank":int(j_coach["postseasonRank"]), 
                "srs": float(j_coach["srs"]), 
                "spOverall": float(j_coach["spOverall"]), 
                "spOffense": float(j_coach["spOffense"]), 
                "spDefense": float(j_coach["spDefense"])
            }
        
            list_parse_coachs.append(dict_parse_coachs)

    return list_parse_coachs 

        


    # return valintercoachesone


# varcoache = fetch_coach()
# print(parse_coachs(varcoache))