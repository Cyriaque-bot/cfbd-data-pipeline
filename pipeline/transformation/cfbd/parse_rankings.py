import sys 
import os
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



def parse_rankings(raws_ranking): 
    validctranking = []  
    for i_ranking in raws_ranking: 
        for key_ranking , val_ranking in i_ranking.items(): 
            if key_ranking == "polls": 
                for j_ranking in val_ranking: 
                    # print(j_ranking)
                    for keykranking, valkeykrankin in j_ranking.items(): 
                         if keykranking == "ranks": 
                            for l_kranking in valkeykrankin: 
                                valistrankingone = {
                                    "season": i_ranking["season"], 
                                    "week": i_ranking["week"], 
                                    "poll": j_ranking["poll"],
                                    "rank": l_kranking["rank"],
                                    "school": l_kranking["school"], 
                                    "conference": l_kranking["conference"]
                                }

                                validctranking.append(valistrankingone)  
    
    return validctranking

# from pipeline.scrapers.cfbd.rankings import fetch_rankings
# valrankings = fetch_rankings(2023)
# print(parse_rankings(valrankings))