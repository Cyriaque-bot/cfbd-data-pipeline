import sys 
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[4]
sys.path.append(str(project_root))


# scraper 
from pipeline.scrapers.derived.merge_game_havoc_stats import fetch_merge_game_havoc_stats
from pipeline.scrapers.derived.merge_game_advanced_stats import fetch_merge_game_advanced_stats
from pipeline.scrapers.derived.merge_games_team_stats import fetch_merge_games_team_stats

# parser 
from pipeline.transformation.derived.parse_merge_games_advanced_stats import parse_merge_games_advanced_stats
from pipeline.transformation.derived.parse_merge_games_havoc_stats import parse_merge_games_havoc_stats
from pipeline.transformation.derived.parse_merge_games_team_stats import parse_games_team_stats

def merge_team(raw_games_team_stats, raw_games_advanced_stats, raw_games_havoc_stats): 
    df_team_stat = pd.DataFrame(raw_games_team_stats)
    df_advanced_stats = pd.DataFrame(raw_games_advanced_stats)
    df_havoc_stats =  pd.DataFrame(raw_games_havoc_stats)

    df_team = pd.merge(
                        df_team_stat,
                        df_advanced_stats,
                        on = ["game_id", "team"],
                        how = "left"

                       ).merge(
                        df_havoc_stats, 
                        on = ["game_id", "team"],
                        how = "left"  
                      )

    # some final calculations
    df_team["yards_per_play"] = round(df_team["yards_total"] /  df_team["off_plays"], 2)
    # return df_team
   
    df_team = df_team.to_json(orient = "records", indent = 4)
    with open("data/raw/derived/merge_team_sample.json", "w") as json_merge_team: 
         json_merge_team.write(df_team)

    return f" 🤸 your file has been copied successfully"

# valhavoc = fetch_merge_game_havoc_stats()
# valadvan = fetch_merge_game_advanced_stats()
# valteam = fetch_merge_games_team_stats()

# valhavocparse = parse_merge_games_havoc_stats(valhavoc)
# valadvanparse = parse_merge_games_advanced_stats(valadvan)
# valteamparse = parse_games_team_stats(valteam)

# print(merge_team(valteamparse,valadvanparse,valhavocparse))
