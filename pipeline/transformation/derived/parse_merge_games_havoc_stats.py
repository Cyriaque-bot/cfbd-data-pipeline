import sys
from pathlib import Path 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))




from pipeline.scrapers.derived.merge_game_havoc_stats import fetch_merge_game_havoc_stats

def parse_merge_games_havoc_stats(raw_parse_merge_games_havoc_stats): 
    list_merge_games_havoc_stats = []
    for i_merge_games_havoc_stats in raw_parse_merge_games_havoc_stats: 
        dict_parse_merge_games_advanced_stats = {
            "game_id": i_merge_games_havoc_stats["game_id"],
            # "season": i_merge_games_havoc_stats["season"], 
            "team": i_merge_games_havoc_stats["team"], 
            # "opponent": i_merge_games_havoc_stats["opponent"],

            "off_havoc_rate": i_merge_games_havoc_stats["off_havoc_rate"],
            "off_db_havoc_rate": i_merge_games_havoc_stats["off_db_havoc_rate"],
            "off_front_seven_havoc_rate": i_merge_games_havoc_stats["off_front_seven_havoc_rate"],
            "off_total_havoc_events": i_merge_games_havoc_stats["off_total_havoc_events"],
            "off_db_havoc_events":i_merge_games_havoc_stats["off_db_havoc_events"],
            "off_front_seven_havoc_events": i_merge_games_havoc_stats["off_front_seven_havoc_events"],
            
            "def_havoc_rate": i_merge_games_havoc_stats["def_havoc_rate"],
            "def_db_havoc_rate": i_merge_games_havoc_stats["def_db_havoc_rate"],
            "def_front_seven_havoc_rate": i_merge_games_havoc_stats["def_front_seven_havoc_rate"],
            "def_total_havoc_events": i_merge_games_havoc_stats["def_total_havoc_events"],
            "def_db_havoc_events":i_merge_games_havoc_stats["def_db_havoc_events"],
            "def_front_seven_havoc_events": i_merge_games_havoc_stats["def_front_seven_havoc_events"]

        }
        list_merge_games_havoc_stats.append(dict_parse_merge_games_advanced_stats)

    return  list_merge_games_havoc_stats

# val = fetch_merge_game_havoc_stats()
# print(parse_merge_games_havoc_stats(val))