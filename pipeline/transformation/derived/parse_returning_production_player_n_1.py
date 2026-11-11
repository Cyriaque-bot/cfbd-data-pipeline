import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.returning_production_player_n_1 import fetch_returning_production_player_n_1

def parse_returning_production_player_n_1(raw_returning_production_player): 
    list_returning_production_player_n_1 = []

    for i_returning_production_player in raw_returning_production_player: 
        # create a function to replace column value  by 0 in case of missing
        def missing_values_cases(val): 
            return i_returning_production_player.get(val, 0)
        
        dict_returning_production_player_n_1 = {
            "player_id": i_returning_production_player["player_id"],  
            "team": i_returning_production_player["team"], 
            "season": i_returning_production_player["season"], 
            # passing
            # "returning_passing_yards": i_returning_production_player["passing_yards"], 
            "returning_passing_yards": missing_values_cases("passing_yards"),
            # "returning_passing_touchdowns": i_returning_production_player["passing_touchdowns"],
            "returning_passing_touchdowns": missing_values_cases("passing_touchdowns"),
            "returning_passing_attempts": missing_values_cases("passing_attempts"),
            "returning_passing_completions":missing_values_cases("passing_completions"),
            "returning_passing_interceptions": missing_values_cases("passing_interceptions"),
            # rushing
            "returning_rushing_yards": missing_values_cases("rushing_attempts"), 
            "returning_rushing_touchdowns": missing_values_cases("rushing_touchdowns"), 
            "returning_rushing_attempts": missing_values_cases("rushing_attempts"), 
            # receiving
            "returning_receiving_yards": missing_values_cases("receiving_yards"),
            "returning_receiving_touchdowns": missing_values_cases("receiving_touchdowns"),
            "returning_receiving_receptions": missing_values_cases("receiving_receptions"),
            # tackles , sacks, qb_hurries, passes, assisted
            "returning_tackles": missing_values_cases("tackles"), 
            "returning_solo_tackles": missing_values_cases("solo_tackles"), 
            "returning_assisted_tackles": missing_values_cases("assisted_tackles"), 
            "returning_sacks": missing_values_cases("sacks"), 
            "returning_qb_hurries": missing_values_cases("qb_hurries"),
            "returning_passes_defended": missing_values_cases("passes_defended"), 
            # ftl
            "returning_tackles_for_loss": missing_values_cases("tackles_for_loss"), 
            # fg_made , fg_attempted
            "returning_fg_made": missing_values_cases("fg_made"), 
            "returning_fg_attempted": missing_values_cases("fg_attempted"),
            # xp_made , xp_attempted
            "returning_xp_made": missing_values_cases("xp_made"), 
            "returning_xp_attempted": missing_values_cases("xp_attempted"), 
            # punt
            "returning_punt_yards": missing_values_cases("punt_yards"),
            "returning_punt_long":missing_values_cases("punt_long"),
            "returning_punt_attempts": missing_values_cases("punt_attempts"), 
            # kick
            "returning_kick_returns_yards": missing_values_cases("kick_returns_yards"), 
            "returning_kick_returns_touchdowns": missing_values_cases("kick_returns_touchdowns"), 
            # punt
            "returning_punt_returns_yards": missing_values_cases("punt_returns_yards"), 
            "returning_punt_returns_touchdowns": missing_values_cases("punt_returns_touchdowns")

        }

        list_returning_production_player_n_1.append(dict_returning_production_player_n_1)

    return list_returning_production_player_n_1



# vaslfetch = fetch_returning_production_player_n_1()
# print(parse_returning_production_player_n_1(vaslfetch))