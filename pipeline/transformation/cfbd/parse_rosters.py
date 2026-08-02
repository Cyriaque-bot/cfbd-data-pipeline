import sys
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


def parse_rosters(rawsroster): 
    valrosterliste = []
    for i in rawsroster: 
        valdictroster = { 
            "player_id": i["id"], 
            "first_name": i["first_name"], 
            "last_name": i["last_name"], 
            "team": i["team"], 
            "position": i["position"], 
            "jersey": i["jersey"],
            "height": i["height"], 
            "weight": i["weight"], 
            "year": i["year"], 
            "home_city": i["home_city"],
            "home_state": i["home_state"],
            "home_country": i["home_country"]
        }
        valrosterliste.append(valdictroster)
    
    return valrosterliste


from pipeline.scrapers.roster import fetch_players
valroster = fetch_players(2023)
print(parse_rosters(valroster))