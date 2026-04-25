import sys 
import os 

project_root =  os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



def parse_rankings(raws_ranking): 
    validctranking = []
    for i in raws_ranking:
        valistrankingone = {
            "season" : i["season"], 
            "week" : i["week"], 
            "poll" : i["poll"]
        }
        for j in i["ranks"]: 
            valistrankingtwo = {
            **valistrankingone, 
            "rank": j["rank"], 
            "school": j["school"], 
            "conference": j["conference"]
            }
            validctranking.append(valistrankingtwo)
    
    return validctranking

from pipeline.scrapers.rankings import fetch_rankings
valrankings = fetch_rankings(2023)
print(parse_rankings(valrankings))