import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.team_roster import fetch_team_roster

def parse_team_roster(raw_team_roster): 
    list_team_roster = []

    for i_team_roster in raw_team_roster: 
        dict_team_roster = {
          "player_id": int(i_team_roster["id"]), 
          "team": i_team_roster["team"], 
          "position": i_team_roster["position"], 
          "year": int(i_team_roster["year"]), 
          "returning": int(i_team_roster["year"]) < 4 
        }
        list_team_roster.append(dict_team_roster)

    return list_team_roster


# result = fetch_team_roster()
# print(parse_team_roster(result))