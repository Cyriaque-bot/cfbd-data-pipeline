import sys
from pathlib import Path 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))




from pipeline.scrapers.derived.merge_game_advanced_stats import fetch_merge_game_advanced_stats

def parse_merge_games_advanced_stats(raw_parse_merge_games_advanced_stats): 
    list_parse_merge_games_advanced_stats = []
    for i_parse_merge_games_advanced_stats in raw_parse_merge_games_advanced_stats: 
        dict_parse_merge_games_advanced_stats = {
            "game_id": i_parse_merge_games_advanced_stats["game_id"], 
            # "season": i_parse_merge_games_advanced_stats, 

            "team": i_parse_merge_games_advanced_stats["team"], 
            "team_conference": i_parse_merge_games_advanced_stats["home_conference"], 
            # "team_points": i_parse_merge_games_advanced_stats["home_points"], 
            "team_line_scores": i_parse_merge_games_advanced_stats["home_line_scores"], 
            "team_pregame_elo": i_parse_merge_games_advanced_stats["home_pregame_elo"], 
            "team_postgame_elo": i_parse_merge_games_advanced_stats["home_postgame_elo"], 
            "team_win_prob_postgame":i_parse_merge_games_advanced_stats["home_win_prob_postgame"], 

            # "opponent": i_parse_merge_games_advanced_stats["opponent"], 
            "opponent_conference": i_parse_merge_games_advanced_stats["away_conference"], 
            # "opponent_points": i_parse_merge_games_advanced_stats["away_points"], 
            "opponent_line_scores": i_parse_merge_games_advanced_stats["away_line_scores"], 
            "opponent_pregame_elo": i_parse_merge_games_advanced_stats["away_pregame_elo"], 
            "opponent_postgame_elo": i_parse_merge_games_advanced_stats["away_postgame_elo"], 
            "opponent_win_prob_postgame":i_parse_merge_games_advanced_stats["away_win_prob_postgame"], 

            "off_explosiveness": i_parse_merge_games_advanced_stats["off_explosiveness"], 
            "off_success_rate": i_parse_merge_games_advanced_stats["off_success_rate"], 
            "off_total_ppa": i_parse_merge_games_advanced_stats["off_total_ppa"], 
            "off_ppa": i_parse_merge_games_advanced_stats["off_ppa"], 
            "off_open_field_yards": i_parse_merge_games_advanced_stats["off_open_field_yards"], 
            "off_second_level_yards": i_parse_merge_games_advanced_stats["off_second_level_yards"], 
            "off_line_yards": i_parse_merge_games_advanced_stats["off_line_yards"], 
            "off_stuff_rate": i_parse_merge_games_advanced_stats["off_stuff_rate"], 
            "off_power_success": i_parse_merge_games_advanced_stats["off_power_success"], 
            "off_drives": i_parse_merge_games_advanced_stats["off_drives"], 
            "off_plays": i_parse_merge_games_advanced_stats["off_plays"], 

            "off_pass_explosiveness": i_parse_merge_games_advanced_stats["off_pass_explosiveness"], 
            "off_pass_success_rate": i_parse_merge_games_advanced_stats["off_pass_success_rate"], 
            "off_pass_total_ppa": i_parse_merge_games_advanced_stats["off_pass_total_ppa"], 
            "off_pass_ppa": i_parse_merge_games_advanced_stats["off_pass_ppa"], 

            "off_rush_explosiveness": i_parse_merge_games_advanced_stats["off_rush_explosiveness"],
            "off_rush_success_rate": i_parse_merge_games_advanced_stats["off_rush_success_rate"],
            "off_rush_total_ppa": i_parse_merge_games_advanced_stats["off_rush_total_ppa"],
            "off_rush_ppa": i_parse_merge_games_advanced_stats["off_rush_ppa"], 

            "off_passing_downs_explosiveness": i_parse_merge_games_advanced_stats["off_passing_downs_explosiveness"],
            "off_passing_downs_success_rate": i_parse_merge_games_advanced_stats["off_passing_downs_success_rate"],
            "off_passing_downs_ppa": i_parse_merge_games_advanced_stats["off_passing_downs_ppa"],

            "off_standard_downs_explosiveness": i_parse_merge_games_advanced_stats["off_standard_downs_explosiveness"],
            "off_standard_downs_success_rate": i_parse_merge_games_advanced_stats["off_standard_downs_success_rate"],
            "off_standard_downs_ppa": i_parse_merge_games_advanced_stats["off_standard_downs_ppa"], 


            "def_explosiveness": i_parse_merge_games_advanced_stats["def_explosiveness"], 
            "def_success_rate": i_parse_merge_games_advanced_stats["def_success_rate"], 
            "def_total_ppa": i_parse_merge_games_advanced_stats["def_total_ppa"], 
            "def_ppa": i_parse_merge_games_advanced_stats["def_ppa"], 
            "def_open_field_yards": i_parse_merge_games_advanced_stats["def_open_field_yards"], 
            "def_second_level_yards": i_parse_merge_games_advanced_stats["def_second_level_yards"], 
            "def_line_yards": i_parse_merge_games_advanced_stats["def_line_yards"], 
            "def_stuff_rate": i_parse_merge_games_advanced_stats["def_stuff_rate"], 
            "def_power_success": i_parse_merge_games_advanced_stats["def_power_success"], 
            "def_drives": i_parse_merge_games_advanced_stats["def_drives"], 
            "def_plays": i_parse_merge_games_advanced_stats["def_plays"], 

            "def_pass_explosiveness": i_parse_merge_games_advanced_stats["def_pass_explosiveness"], 
            "def_pass_success_rate": i_parse_merge_games_advanced_stats["def_pass_success_rate"], 
            "def_pass_total_ppa": i_parse_merge_games_advanced_stats["def_pass_total_ppa"], 
            "def_pass_ppa": i_parse_merge_games_advanced_stats["def_pass_ppa"], 

            "def_rush_explosiveness": i_parse_merge_games_advanced_stats["def_rush_explosiveness"],
            "def_rush_success_rate": i_parse_merge_games_advanced_stats["def_rush_success_rate"],
            "def_rush_total_ppa": i_parse_merge_games_advanced_stats["def_rush_total_ppa"],
            "def_rush_ppa": i_parse_merge_games_advanced_stats["def_rush_ppa"], 

            "def_passing_downs_explosiveness": i_parse_merge_games_advanced_stats["def_passing_downs_explosiveness"],
            "def_passing_downs_success_rate": i_parse_merge_games_advanced_stats["def_passing_downs_success_rate"],
            "def_passing_downs_ppa": i_parse_merge_games_advanced_stats["def_passing_downs_ppa"],

            "def_standard_downs_explosiveness": i_parse_merge_games_advanced_stats["def_standard_downs_explosiveness"],
            "def_standard_downs_success_rate": i_parse_merge_games_advanced_stats["def_standard_downs_success_rate"],
            "def_standard_downs_ppa": i_parse_merge_games_advanced_stats["def_standard_downs_ppa"] 

        }
        list_parse_merge_games_advanced_stats.append(dict_parse_merge_games_advanced_stats)

    return list_parse_merge_games_advanced_stats

# valftec = fetch_merge_game_advanced_stats()
# print(parse_merge_games_advanced_stats(valftec))