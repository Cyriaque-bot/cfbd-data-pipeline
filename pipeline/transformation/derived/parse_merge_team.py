import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str())

from pipeline.scrapers.derived.merge_team import fetch_merge_team


def parse_merge_team(raw_merge_team): 
    list_raw_merge_team = []

    for i_merge_team in raw_merge_team: 
        dict_merge_team = {
            # temporal columns
            "game_id": i_merge_team["game_id"], 
            "season": i_merge_team["season"], 
            "week": i_merge_team["week"], 
            "season_type": i_merge_team["season_type"], 
            "start_date": i_merge_team["start_date"], 
             # matchs columns
            "completed": i_merge_team["completed"], 
            "neutral_site": i_merge_team["neutral_site"], 
            "conference_game": i_merge_team["conference_game"], 
            "venue": i_merge_team["venue"],
            # team and opponent
            "team_id": i_merge_team["team_id"], 
            "team": i_merge_team["team"], 
            "team_side": i_merge_team["team_side"], 
            "team_conference": i_merge_team["team_conference"], 
            "team_points": i_merge_team["team_points"], 

            "opponent_id": i_merge_team["opponent_id"], 
            "opponent": i_merge_team["opponent"], 
            "opponent_conference": i_merge_team["opponent_conference"], 
            "opponent_points": i_merge_team["opponent_points"],

            # stats brutes
            "yards_total": i_merge_team["yards_total"], 
            "rushing_yards": i_merge_team["rushing_yards"], 
            "passing_yards": i_merge_team["passing_yards"], 
            "turnovers": i_merge_team["turnovers"], 
            "third_down_pct": i_merge_team["third_down_pct"], 
            "fourth_down_pct": i_merge_team["fourth_down_pct"], 
            "yards_per_play": i_merge_team["yards_per_play"], 

            # advanced stats offense
            "off_explosiveness": i_merge_team["off_explosiveness"], 
            "off_success_rate": i_merge_team["off_success_rate"], 
            "off_total_ppa": i_merge_team["off_total_ppa"], 
            "off_ppa": i_merge_team["off_ppa"], 
            "off_open_field_yards": i_merge_team["off_open_field_yards"], 
            "off_second_level_yards": i_merge_team["off_second_level_yards"], 
            "off_line_yards": i_merge_team["off_line_yards"], 
            "off_stuff_rate": i_merge_team["off_stuff_rate"], 
            "off_power_success": i_merge_team["off_power_success"], 
            "off_drives": i_merge_team["off_drives"], 
            "off_plays": i_merge_team["off_plays"],

            "off_pass_explosiveness": i_merge_team["off_pass_explosiveness"], 
            "off_pass_success_rate": i_merge_team["off_pass_success_rate"], 
            "off_pass_total_ppa": i_merge_team["off_pass_total_ppa"], 
            "off_pass_ppa": i_merge_team["off_pass_ppa"], 

            "off_rush_explosiveness": i_merge_team["off_rush_explosiveness"], 
            "off_rush_success_rate": i_merge_team["off_rush_success_rate"], 
            "off_rush_total_ppa": i_merge_team["off_rush_total_ppa"], 
            "off_rush_ppa": i_merge_team["off_rush_ppa"], 

            "off_passing_downs_explosiveness": i_merge_team["off_passing_downs_explosiveness"], 
            "off_passing_downs_success_rate": i_merge_team["off_passing_downs_success_rate"], 
            "off_passing_downs_ppa": i_merge_team["off_passing_downs_ppa"],

            "off_standard_downs_explosiveness": i_merge_team["off_standard_downs_explosiveness"], 
            "off_standard_downs_success_rate": i_merge_team["off_standard_downs_success_rate"], 
            "off_standard_downs_ppa": i_merge_team["off_standard_downs_ppa"],

            # advanced stats defense
            "def_explosiveness": i_merge_team["def_explosiveness"], 
            "def_success_rate": i_merge_team["def_success_rate"], 
            "def_total_ppa": i_merge_team["def_total_ppa"], 
            "def_ppa": i_merge_team["def_ppa"], 
            "def_open_field_yards": i_merge_team["def_open_field_yards"], 
            "def_second_level_yards": i_merge_team["def_second_level_yards"], 
            "def_line_yards": i_merge_team["def_line_yards"], 
            "def_stuff_rate": i_merge_team["def_stuff_rate"], 
            "def_power_success": i_merge_team["def_power_success"], 
            "def_drives": i_merge_team["def_drives"], 
            "def_plays": i_merge_team["def_plays"],

            "def_pass_explosiveness": i_merge_team["def_pass_explosiveness"], 
            "def_pass_success_rate": i_merge_team["def_pass_success_rate"], 
            "def_pass_total_ppa": i_merge_team["def_pass_total_ppa"], 
            "def_pass_ppa": i_merge_team["def_pass_ppa"], 

            "def_rush_explosiveness": i_merge_team["def_rush_explosiveness"], 
            "def_rush_success_rate": i_merge_team["def_rush_success_rate"], 
            "def_rush_total_ppa": i_merge_team["def_rush_total_ppa"], 
            "def_rush_ppa": i_merge_team["def_rush_ppa"], 

            "def_passing_downs_explosiveness": i_merge_team["def_passing_downs_explosiveness"], 
            "def_passing_downs_success_rate": i_merge_team["def_passing_downs_success_rate"], 
            "def_passing_downs_ppa": i_merge_team["def_passing_downs_ppa"],

            "def_standard_downs_explosiveness": i_merge_team["def_standard_downs_explosiveness"], 
            "def_standard_downs_success_rate": i_merge_team["def_standard_downs_success_rate"], 
            "def_standard_downs_ppa": i_merge_team["def_standard_downs_ppa"],

            # havoc
            "off_havoc_rate": i_merge_team["off_havoc_rate"],
            "off_db_havoc_rate": i_merge_team["off_db_havoc_rate"],
            "off_front_seven_havoc_rate": i_merge_team["off_front_seven_havoc_rate"],
            "off_total_havoc_events": i_merge_team["off_total_havoc_events"],
            "off_db_havoc_events":i_merge_team["off_db_havoc_events"],
            "off_front_seven_havoc_events": i_merge_team["off_front_seven_havoc_events"], 

            "def_havoc_rate": i_merge_team["def_havoc_rate"],
            "def_db_havoc_rate": i_merge_team["def_db_havoc_rate"],
            "def_front_seven_havoc_rate": i_merge_team["def_front_seven_havoc_rate"],
            "def_total_havoc_events": i_merge_team["def_total_havoc_events"],
            "def_db_havoc_events":i_merge_team["def_db_havoc_events"],
            "def_front_seven_havoc_events": i_merge_team["def_front_seven_havoc_events"]
            
        }
        list_raw_merge_team.append(dict_merge_team)

    return list_raw_merge_team


# valfetch = fetch_merge_team()

# print(parse_merge_team(valfetch))