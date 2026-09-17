import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

# the scrapers
from pipeline.scrapers.cfbd.games import fetch_games
from pipeline.scrapers.cfbd.game_advanced import fetch_game_advanced 
# the parsers

from  pipeline.transformation.cfbd.parse_games import parse_games
from  pipeline.transformation.cfbd.parse_games_advanced import parse_game_advanced

def merge_game_advanced_stats(raw_parse_games, raw_parse_game_advanced): 
  
    df_games = pd.DataFrame(raw_parse_games) 
    df_games_advanced = pd.DataFrame(raw_parse_game_advanced)

    # retrieve from  my game two team
    df_games_team = pd.concat([
        df_games.rename(columns = {
            "home_team": "team", 
            "away_team" : "opponent"
            }), 

        df_games.rename(columns = {
            "away_team": "team", 
            "home_team": "opponent"
            }), 
    ])

    # rename column now to avoid value like _x
    df_games_advanced = df_games_advanced.rename(columns = {"season": "season_advanced", "week": "week_advanced", "opponent": "opponent_advanced"})

    # merge game advanced_stats

    df_games_advanced_final = df_games_team.merge(
        df_games_advanced, 
        left_on = ["game_id", "team"], 
        right_on = ["game_id", "team"],
        how = "left"
    )

    # transform ou dataframe to json

    df_games_advanced_final = df_games_advanced_final.to_json(orient = "records", indent = 4)

    #write the file in data/raw/derived
    with open("data/raw/derived/merge_game_advanced_stats_sample.json", "w") as merge_game_advenced_stats_json: 
         merge_game_advenced_stats_json.write(df_games_advanced_final)
    return  f"🤸 the file has been copied with success"
 

# val_game = fetch_games()
# val_advanced = fetch_game_advanced()
# vaparsegame = parse_games(val_game)
# valparseadvance = parse_game_advanced(val_advanced)
# print(merge_game_advanced_stats(vaparsegame,valparseadvance))