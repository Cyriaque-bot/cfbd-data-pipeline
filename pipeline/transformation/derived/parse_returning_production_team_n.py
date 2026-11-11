import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.returning_production_team_n import fetch_returning_production_team_n

def parse_returning_production_team_n(raw_returning_production_team_n): 
    list_returning_production_team_n = []

    for i_returning_production_team_n in raw_returning_production_team_n: 
        dict_raw_returning_production_team_n = {
            "team_id" : i_returning_production_team_n["team_id"], 
            "team": i_returning_production_team_n["team"], 
            "season": i_returning_production_team_n["season"], 
            # passing
            "total_passing_yards": i_returning_production_team_n["returning_passing_yards"], 
            "total_passing_touchdowns": i_returning_production_team_n["returning_passing_touchdowns"], 
            "total_passing_attempts": i_returning_production_team_n["returning_passing_attempts"], 
            "total_passing_completions": i_returning_production_team_n["returning_passing_completions"], 
            "total_passing_interceptions": i_returning_production_team_n["returning_passing_interceptions"], 
            # rushing
            "total_rushing_yards": i_returning_production_team_n["returning_rushing_yards"], 
            "total_rushing_touchdowns": i_returning_production_team_n["returning_rushing_touchdowns"], 
            "total_rushing_attempts": i_returning_production_team_n["returning_rushing_attempts"], 
            # receiving
            "total_receiving_yards": i_returning_production_team_n["returning_receiving_yards"], 
            "total_receiving_touchdowns": i_returning_production_team_n["returning_receiving_touchdowns"], 
            "total_receiving_receptions": i_returning_production_team_n["returning_receiving_receptions"], 
            # tackles, sacks , qb_hurries, defended
            "total_tackles": i_returning_production_team_n["returning_tackles"], 
            "total_solo_tackles": i_returning_production_team_n["returning_solo_tackles"], 
            "total_assisted_tackles": i_returning_production_team_n["returning_assisted_tackles"], 
            "total_sacks": i_returning_production_team_n["returning_sacks"], 
            "total_qb_hurries": i_returning_production_team_n["returning_qb_hurries"], 
            "total_passes_defended": i_returning_production_team_n["returning_passes_defended"], 
            "total_tackles_for_loss": i_returning_production_team_n["returning_tackles_for_loss"],
            # fg
            "total_fg_made": i_returning_production_team_n["returning_fg_made"],
            "total_fg_attempted": i_returning_production_team_n["returning_fg_attempted"],
            # xp
            "total_xp_made": i_returning_production_team_n["returning_xp_made"],
            "total_xp_attempted": i_returning_production_team_n["returning_xp_attempted"],
            # punt, long, attempts
            "total_punt_yards": i_returning_production_team_n["returning_punt_yards"],
            "total_punt_long": i_returning_production_team_n["returning_punt_long"],
            "total_punt_attempts": i_returning_production_team_n["returning_punt_attempts"],
            # kick
            "total_kick_returns_yards": i_returning_production_team_n["returning_kick_returns_yards"],
            "total_kick_returns_touchdowns": i_returning_production_team_n["returning_kick_returns_touchdowns"],
            # punt
            "total_punt_returns_yards": i_returning_production_team_n["returning_punt_returns_yards"],
            "total_punt_returns_touchdowns": i_returning_production_team_n["returning_punt_returns_touchdowns"],
        } 
        list_returning_production_team_n.append(dict_raw_returning_production_team_n)

    return list_returning_production_team_n

# van = fetch_returning_production_team_n()
# print(parse_returning_production_team_n(van))