import sys
from pathlib import Path



project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.derived.add_opponent_conference_strength import fetch_add_opponent_conference_strength
def parse_add_opponent_conference_strength(raw_add_opponent_conference_strength):
    list_add_opponent_conference_strength = []
    for i_add_opponent_conference_strength in raw_add_opponent_conference_strength : 
        dict_add_opponent_conference_strength = {
            "game_id": i_add_opponent_conference_strength["game_id"], 
            "season": i_add_opponent_conference_strength["season"], 
            "week": i_add_opponent_conference_strength["week"], 
            "team_id": i_add_opponent_conference_strength["team_id"], 
            "team": i_add_opponent_conference_strength["team"], 
            "opponent_id": i_add_opponent_conference_strength["opponent_id"], 
            "opponent": i_add_opponent_conference_strength["opponent"], 
            "team_points": i_add_opponent_conference_strength["team_points"], 
            "opponent_points": i_add_opponent_conference_strength["opponent_points"], 
            "team_conference_id": i_add_opponent_conference_strength["team_conference_id"], 
            "opponent_conference_id": i_add_opponent_conference_strength["opponent_conference_id"], 
            "conference_id": i_add_opponent_conference_strength["conference_id"], 

            "team_conference_avg_win_rate": i_add_opponent_conference_strength["team_conference_avg_win_rate"], 
            "team_conference_strength_raw": i_add_opponent_conference_strength["team_conference_strength_raw"], 
            "team_conference_strength_norm": i_add_opponent_conference_strength["team_conference_strength_norm"], 
            "team_conference_avg_opponent_margin": i_add_opponent_conference_strength["team_conference_avg_opponent_margin"], 
            "team_conference_avg_opponent_margin_norm": i_add_opponent_conference_strength["team_conference_avg_opponent_margin_norm"], 

            "opponent_conference_avg_win_rate": i_add_opponent_conference_strength["opponent_conference_avg_win_rate"], 
            "opponent_conference_strength_raw": i_add_opponent_conference_strength["opponent_conference_strength_raw"], 
            "opponent_conference_strength_norm": i_add_opponent_conference_strength["opponent_conference_strength_norm"], 
            "opponent_conference_avg_opponent_margin": i_add_opponent_conference_strength["opponent_conference_avg_opponent_margin"], 
            "opponent_conference_avg_opponent_margin_norm": i_add_opponent_conference_strength["opponent_conference_avg_opponent_margin_norm"],
        }

        list_add_opponent_conference_strength.append(dict_add_opponent_conference_strength)
    return list_add_opponent_conference_strength


# val = fetch_add_opponent_conference_strength()
# print(parse_add_opponent_conference_strength(val))