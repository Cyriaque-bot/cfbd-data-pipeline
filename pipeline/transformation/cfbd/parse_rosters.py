from pathlib import Path
import sys


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.rosters import fetch_roster
def parse_rosters(rawsroster): 
    valrosterliste = []
    for i_roster in rawsroster: 
        valdictroster = { 
            "player_id": i_roster["id"], 
            "first_name": i_roster["firstName"], 
            "last_name": i_roster["lastName"], 
            "team": i_roster["team"], 
            "year": i_roster["year"],   
            "height": i_roster["height"], 
            "weight": i_roster["weight"], 
            "jersey": i_roster["jersey"],
            "position": i_roster["position"], 
            "home_city": i_roster["homeCity"],
            "home_state": i_roster["homeState"],
            "home_country": i_roster["homeCountry"],
            "recruit_ids": i_roster["recruitIds"]
        }

        valrosterliste.append(valdictroster)
    
    return valrosterliste



# valroster = fetch_roster()
# print(parse_rosters(valroster))