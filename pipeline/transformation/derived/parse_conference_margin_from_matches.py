import sys
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.derived.conference_margin_from_matches import fetch_conference_margin

def parse_conference_margin(raw_conference_margin): 
    list_conference_margin = []

    for i_conference_margin in raw_conference_margin: 
        dict_conference_margin = {
            "team_conference_id": i_conference_margin["team_conference_id"], 
            "opponent_margin": i_conference_margin["opponent_margin"]
        }
        list_conference_margin.append(dict_conference_margin)
    return list_conference_margin


# vall = fetch_conference_margin()
# print(parse_conference_margin(vall))