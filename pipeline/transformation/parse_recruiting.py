import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


def parse_recruiting(rawrecruiting): 
    vallisterecruiting = []
    for i in rawrecruiting: 
        valdictrecruiting = {
        "year": i["year"], 
        "team": i["team"], 
        "rank": i["rank"], 
        "points": i["points"],
        "commits": i["commits"]
        }
        vallisterecruiting.append(valdictrecruiting)
    
    return vallisterecruiting

from pipeline.scrapers.recruiting import fetch_get_recruiting
result = fetch_get_recruiting(2023)
print(parse_recruiting(result))