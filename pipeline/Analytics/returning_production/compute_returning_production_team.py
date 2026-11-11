import sys 
from pathlib import Path
import pandas as pd 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.returning_production_player_n_1 import fetch_returning_production_player_n_1
from pipeline.scrapers.derived.returning_production_player_n import fetch_returning_production_player_n
from pipeline.scrapers.cfbd.teams import fetch_teams

from pipeline.transformation.derived.parse_returning_production_player_n_1 import parse_returning_production_player_n_1
from pipeline.transformation.derived.parse_returning_production_player_n import parse_returning_production_player_n
from pipeline.transformation.cfbd.parse_teams import parse_teams


def compute_returning_production_team(raw_returning_production_player_n_1, raw_returning_production_player_n, raw_teams): 
    df_return_team_n_1 = pd.DataFrame(raw_returning_production_player_n_1) 
    df_return_team_n = pd.DataFrame(raw_returning_production_player_n)
    df_team = pd.DataFrame(raw_teams) 
    
    # first merge in order to take the id_team
    df_return_team_n_1 = df_return_team_n_1.merge(
        df_team[["school", "team_id"]], 
        left_on = "team", 
        right_on = "school"
        )

    df_return_team_n = df_return_team_n.merge(
        df_team[["school", "team_id"]], 
        left_on = "team", 
        right_on = "school"
        )


    # sum for N + 1
    df_returning_sum_n_1  = (
                       df_return_team_n_1.groupby(["team_id","team", "season"])
                       .agg({ 
                           # passing
                           "returning_passing_yards": "sum", 
                           "returning_passing_touchdowns": "sum", 
                           "returning_passing_attempts": "sum", 
                           "returning_passing_completions": "sum", 
                           "returning_passing_interceptions": "sum", 
                           # rushing
                           "returning_rushing_yards": "sum", 
                           "returning_rushing_touchdowns": "sum", 
                           "returning_rushing_attempts": "sum", 
                           # receiving
                           "returning_receiving_yards": "sum", 
                           "returning_receiving_touchdowns": "sum", 
                           "returning_receiving_receptions": "sum", 
                           # tackles , sacks, qb_hurries, passes, assisted
                           "returning_tackles": "sum", 
                           "returning_solo_tackles": "sum", 
                           "returning_assisted_tackles": "sum", 
                           "returning_sacks": "sum", 
                           "returning_qb_hurries": "sum", 
                           "returning_passes_defended": "sum", 
                           # tfl 
                           "returning_tackles_for_loss": "sum", 
                           # fg_made , fg_attempted
                           "returning_fg_made": "sum", 
                           "returning_fg_attempted": "sum", 
                           # xp_made , xp_attempted
                           "returning_xp_made": "sum", 
                           "returning_xp_attempted": "sum", 
                           # punt
                           "returning_punt_yards": "sum", 
                           "returning_punt_long": "sum", 
                           "returning_punt_attempts": "sum", 
                           # kick
                           "returning_kick_returns_yards": "sum", 
                           "returning_kick_returns_touchdowns": "sum", 
                           # punt
                           "returning_punt_returns_yards": "sum", 
                           "returning_punt_returns_touchdowns": "sum"
                       }
                      )).reset_index()

    # sum for N 
    df_returning_sum_n  = (
                       df_return_team_n.groupby(["team_id","team", "season"])
                       .agg({ 
                           # passing
                           "returning_passing_yards": "sum", 
                           "returning_passing_touchdowns": "sum", 
                           "returning_passing_attempts": "sum", 
                           "returning_passing_completions": "sum", 
                           "returning_passing_interceptions": "sum", 
                           # rushing
                           "returning_rushing_yards": "sum", 
                           "returning_rushing_touchdowns": "sum", 
                           "returning_rushing_attempts": "sum", 
                           # receiving
                           "returning_receiving_yards": "sum", 
                           "returning_receiving_touchdowns": "sum", 
                           "returning_receiving_receptions": "sum", 
                           # tackles , sacks, qb_hurries, passes, assisted
                           "returning_tackles": "sum", 
                           "returning_solo_tackles": "sum", 
                           "returning_assisted_tackles": "sum", 
                           "returning_sacks": "sum", 
                           "returning_qb_hurries": "sum", 
                           "returning_passes_defended": "sum", 
                           # tfl 
                           "returning_tackles_for_loss": "sum", 
                           # fg_made , fg_attempted
                           "returning_fg_made": "sum", 
                           "returning_fg_attempted": "sum", 
                           # xp_made , xp_attempted
                           "returning_xp_made": "sum", 
                           "returning_xp_attempted": "sum", 
                           # punt
                           "returning_punt_yards": "sum", 
                           "returning_punt_long": "sum", 
                           "returning_punt_attempts": "sum", 
                           # kick
                           "returning_kick_returns_yards": "sum", 
                           "returning_kick_returns_touchdowns": "sum", 
                           # punt
                           "returning_punt_returns_yards": "sum", 
                           "returning_punt_returns_touchdowns": "sum"
                       }
                      )).reset_index()
    
  

    df_return_team_final_n_1 = df_returning_sum_n_1.to_json(orient = "records", indent = 4)

    df_return_team_final_n = df_returning_sum_n.to_json(orient = "records", indent = 4)
    
    # write in derived data 
    with open("data/raw/derived/returning_production_team_n_1_sample.json", "w") as json_returning_production_team_n_1: 
         json_returning_production_team_n_1.write(df_return_team_final_n_1)

    # write in derived data 
       
    with open("data/raw/derived/returning_production_team_n_sample.json", "w") as json_returning_production_team_n: 
         json_returning_production_team_n.write(df_return_team_final_n)

    return f"🤸 your file has been copied succesfully"
  


# valteam = fetch_teams()
# valparseteam = parse_teams(valteam)
# valfetch_n_1 = fetch_returning_production_player_n_1()
# valtparse_n_1 = parse_returning_production_player_n_1(valfetch_n_1)

# valfetch_n = fetch_returning_production_player_n()
# valtparse_n = parse_returning_production_player_n(valfetch_n)
# print(compute_returning_production_team(valtparse_n_1, valtparse_n, valparseteam))