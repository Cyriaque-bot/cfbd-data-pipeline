import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.returning_production_team_n_1 import fetch_returning_production_team_n_1

def parse_returning_production_team_n_1(raw_returning_production_team): 
    list_returning_production_team_n_1 = []

    for i_returning_production_team_n_1 in raw_returning_production_team: 
        dict_raw_returning_production_team_n_1 = {
            "team_id" : i_returning_production_team_n_1["team_id"], 
            "team": i_returning_production_team_n_1["team"], 
            "season": i_returning_production_team_n_1["season"], 
            # passing
            "returning_passing_yards": i_returning_production_team_n_1["returning_passing_yards"], 
            "returning_passing_touchdowns": i_returning_production_team_n_1["returning_passing_touchdowns"], 
            "returning_passing_attempts": i_returning_production_team_n_1["returning_passing_attempts"], 
            "returning_passing_completions": i_returning_production_team_n_1["returning_passing_completions"], 
            "returning_passing_interceptions": i_returning_production_team_n_1["returning_passing_interceptions"], 
            # rushing
            "returning_rushing_yards": i_returning_production_team_n_1["returning_rushing_yards"], 
            "returning_rushing_touchdowns": i_returning_production_team_n_1["returning_rushing_touchdowns"], 
            "returning_rushing_attempts": i_returning_production_team_n_1["returning_rushing_attempts"], 
            # receiving
            "returning_receiving_yards": i_returning_production_team_n_1["returning_receiving_yards"], 
            "returning_receiving_touchdowns": i_returning_production_team_n_1["returning_receiving_touchdowns"], 
            "returning_receiving_receptions": i_returning_production_team_n_1["returning_receiving_receptions"], 
            # tackles, sacks , qb_hurries, defended
            "returning_tackles": i_returning_production_team_n_1["returning_tackles"], 
            "returning_solo_tackles": i_returning_production_team_n_1["returning_solo_tackles"], 
            "returning_assisted_tackles": i_returning_production_team_n_1["returning_assisted_tackles"], 
            "returning_sacks": i_returning_production_team_n_1["returning_sacks"], 
            "returning_qb_hurries": i_returning_production_team_n_1["returning_qb_hurries"], 
            "returning_passes_defended": i_returning_production_team_n_1["returning_passes_defended"], 
            "returning_tackles_for_loss": i_returning_production_team_n_1["returning_tackles_for_loss"],
            # fg
            "returning_fg_made": i_returning_production_team_n_1["returning_fg_made"],
            "returning_fg_attempted": i_returning_production_team_n_1["returning_fg_attempted"],
            # xp
            "returning_xp_made": i_returning_production_team_n_1["returning_xp_made"],
            "returning_xp_attempted": i_returning_production_team_n_1["returning_xp_attempted"],
            # punt, long, attempts
            "returning_punt_yards": i_returning_production_team_n_1["returning_punt_yards"],
            "returning_punt_long": i_returning_production_team_n_1["returning_punt_long"],
            "returning_punt_attempts": i_returning_production_team_n_1["returning_punt_attempts"],
            # kick
            "returning_kick_returns_yards": i_returning_production_team_n_1["returning_kick_returns_yards"],
            "returning_kick_returns_touchdowns": i_returning_production_team_n_1["returning_kick_returns_touchdowns"],
            # punt
            "returning_punt_returns_yards": i_returning_production_team_n_1["returning_punt_returns_yards"],
            "returning_punt_returns_touchdowns": i_returning_production_team_n_1["returning_punt_returns_touchdowns"],
        } 
        list_returning_production_team_n_1.append(dict_raw_returning_production_team_n_1)

    return list_returning_production_team_n_1