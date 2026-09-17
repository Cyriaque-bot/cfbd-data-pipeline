import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.game_havoc import fetch_game_havoc

def parse_game_havoc(raw_game_havoc): 
    list_game_havoc = []
    for i_game_havoc in raw_game_havoc: 
        dict_game_havoc = {
            "game_id": int(i_game_havoc["gameId"]), 
            "season": int(i_game_havoc["season"]), 
            "week": int(i_game_havoc["week"]), 
            "team": i_game_havoc["team"], 
            "opponent": i_game_havoc["opponent"],

            # offensive
            "off_db_havoc_rate": float(i_game_havoc["offense"]["dbHavocRate"]), 
            "off_front_seven_havoc_rate":  float(i_game_havoc["offense"]["frontSevenHavocRate"]), 
            "off_havoc_rate": float(i_game_havoc["offense"]["havocRate"]), 
            "off_db_havoc_events": int(i_game_havoc["offense"]["dbHavocEvents"]), 
            "off_front_seven_havoc_events": int(i_game_havoc["offense"]["frontSevenHavocEvents"]), 
            "off_total_havoc_events": int(i_game_havoc["offense"]["totalHavocEvents"]), 
            "off_total_plays": int(i_game_havoc["offense"]["totalPlays"]), 

            # defensive
            "def_db_havoc_rate": float(i_game_havoc["defense"]["dbHavocRate"]), 
            "def_front_seven_havoc_rate":  float(i_game_havoc["defense"]["frontSevenHavocRate"]), 
            "def_havoc_rate": float(i_game_havoc["defense"]["havocRate"]), 
            "def_db_havoc_events": int(i_game_havoc["defense"]["dbHavocEvents"]), 
            "def_front_seven_havoc_events": int(i_game_havoc["defense"]["frontSevenHavocEvents"]), 
            "def_total_havoc_events": int(i_game_havoc["defense"]["totalHavocEvents"]), 
            "def_total_plays": int(i_game_havoc["defense"]["totalPlays"]), 
        }

        list_game_havoc.append(dict_game_havoc)
    return list_game_havoc

# valhavoc = fetch_game_havoc()
# print(parse_game_havoc(valhavoc))