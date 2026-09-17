import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.game_advanced import fetch_game_advanced

def parse_game_advanced(raw_game_advanced): 
    list_raw_game_advanced = []
    for i_raw_game_advanced in raw_game_advanced: 
        dict_raw_game_advanced = {
            "game_id": int(i_raw_game_advanced["gameId"]), 
            "season": int(i_raw_game_advanced["season"]),
            "week": int(i_raw_game_advanced["week"]), 
            "team": i_raw_game_advanced["team"], 
            "opponent": i_raw_game_advanced["opponent"],

            # offense - global metrics 
            "off_explosiveness": float(i_raw_game_advanced["offense"]["explosiveness"]), 
            "off_success_rate": float(i_raw_game_advanced["offense"]["successRate"]),
            "off_total_ppa": float(i_raw_game_advanced["offense"]["totalPPA"]),
            "off_ppa": float(i_raw_game_advanced["offense"]["ppa"]),
            "off_open_field_yards": float(i_raw_game_advanced["offense"]["openFieldYards"]), 
            "off_second_level_yards": float(i_raw_game_advanced["offense"]["secondLevelYards"]),
            "off_line_yards": float(i_raw_game_advanced["offense"]["lineYards"]),
            "off_stuff_rate": float(i_raw_game_advanced["offense"]["stuffRate"]), 
            "off_power_success": float(i_raw_game_advanced["offense"]["powerSuccess"]), 
            "off_drives": int(i_raw_game_advanced["offense"]["drives"]),
            "off_plays": int(i_raw_game_advanced["offense"]["plays"]),
            # offense - passing plays
            "off_pass_explosiveness" : float(i_raw_game_advanced["offense"]["passingPlays"]["explosiveness"]),
            "off_pass_success_rate" : float(i_raw_game_advanced["offense"]["passingPlays"]["successRate"]),
            "off_pass_total_ppa" : float(i_raw_game_advanced["offense"]["passingPlays"]["totalPPA"]),
            "off_pass_ppa" : float(i_raw_game_advanced["offense"]["passingPlays"]["ppa"]),
            # offense - rushing plays
            "off_rush_explosiveness" : float(i_raw_game_advanced["offense"]["rushingPlays"]["explosiveness"]),
            "off_rush_success_rate" : float(i_raw_game_advanced["offense"]["rushingPlays"]["successRate"]),
            "off_rush_total_ppa" : float(i_raw_game_advanced["offense"]["rushingPlays"]["totalPPA"]),
            "off_rush_ppa" : float(i_raw_game_advanced["offense"]["rushingPlays"]["ppa"]),
            # offense - passing down
            "off_passing_downs_explosiveness" : float(i_raw_game_advanced["offense"]["passingDowns"]["explosiveness"]),
            "off_passing_downs_success_rate" : float(i_raw_game_advanced["offense"]["passingDowns"]["successRate"]),
            "off_passing_downs_ppa" : float(i_raw_game_advanced["offense"]["passingDowns"]["ppa"]),
            # offense - standard down
            "off_standard_downs_explosiveness" : float(i_raw_game_advanced["offense"]["standardDowns"]["explosiveness"]),
            "off_standard_downs_success_rate" : float(i_raw_game_advanced["offense"]["standardDowns"]["successRate"]),
            "off_standard_downs_ppa" : float(i_raw_game_advanced["offense"]["standardDowns"]["ppa"]),


            # defensive
            "def_explosiveness": float(i_raw_game_advanced["defense"]["explosiveness"]), 
            "def_success_rate": float(i_raw_game_advanced["defense"]["successRate"]),
            "def_total_ppa": float(i_raw_game_advanced["defense"]["totalPPA"]),
            "def_ppa": float(i_raw_game_advanced["defense"]["ppa"]),
            "def_open_field_yards": float(i_raw_game_advanced["defense"]["openFieldYards"]), 
            "def_second_level_yards": float(i_raw_game_advanced["defense"]["secondLevelYards"]),
            "def_line_yards": float(i_raw_game_advanced["defense"]["lineYards"]),
            "def_stuff_rate": float(i_raw_game_advanced["defense"]["stuffRate"]), 
            "def_power_success": float(i_raw_game_advanced["defense"]["powerSuccess"]), 
            "def_drives": int(i_raw_game_advanced["defense"]["drives"]),
            "def_plays": int(i_raw_game_advanced["defense"]["plays"]),

            # defensive - passing plays
            "def_pass_explosiveness" : float(i_raw_game_advanced["defense"]["passingPlays"]["explosiveness"]),
            "def_pass_success_rate" : float(i_raw_game_advanced["defense"]["passingPlays"]["successRate"]),
            "def_pass_total_ppa" : float(i_raw_game_advanced["defense"]["passingPlays"]["totalPPA"]),
            "def_pass_ppa" : float(i_raw_game_advanced["defense"]["passingPlays"]["ppa"]),
            # defensive - rushing plays
            "def_rush_explosiveness" : float(i_raw_game_advanced["defense"]["rushingPlays"]["explosiveness"]),
            "def_rush_success_rate" : float(i_raw_game_advanced["defense"]["rushingPlays"]["successRate"]),
            "def_rush_total_ppa" : float(i_raw_game_advanced["defense"]["rushingPlays"]["totalPPA"]),
            "def_rush_ppa" : float(i_raw_game_advanced["defense"]["rushingPlays"]["ppa"]),
            # defensive - passing down
            "def_passing_downs_explosiveness" : float(i_raw_game_advanced["defense"]["passingDowns"]["explosiveness"]),
            "def_passing_downs_success_rate" : float(i_raw_game_advanced["defense"]["passingDowns"]["successRate"]),
            "def_passing_downs_ppa" : float(i_raw_game_advanced["defense"]["passingDowns"]["ppa"]),
            # defensive - standard down
            "def_standard_downs_explosiveness" : float(i_raw_game_advanced["defense"]["standardDowns"]["explosiveness"]),
            "def_standard_downs_success_rate" : float(i_raw_game_advanced["defense"]["standardDowns"]["successRate"]),
            "def_standard_downs_ppa" : float(i_raw_game_advanced["defense"]["standardDowns"]["ppa"])
        }
        list_raw_game_advanced.append(dict_raw_game_advanced)

    return list_raw_game_advanced


# val = fetch_game_advanced()
# print(parse_game_advanced(val))