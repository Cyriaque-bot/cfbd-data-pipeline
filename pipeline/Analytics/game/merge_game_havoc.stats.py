import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.games import fetch_games
from pipeline.scrapers.cfbd.game_havoc import fetch_game_havoc

from pipeline.transformation.cfbd.parse_games import parse_games
from pipeline.transformation.cfbd.parse_games_havoc import parse_game_havoc
 


def merge_game_havoc(raw_parse_game, raw_parse_havoc): 

    df_game = pd.DataFrame(raw_parse_game)
    df_game_havoc = pd.DataFrame(raw_parse_havoc)

    # retrieve team by game with contenation
    df_game = pd.concat([df_game.rename(columns = {"home_team": "team", 
                                                 "away_team": "opponent"}), 
                        df_game.rename(columns = {"away_team": "team", 
                                                 "team": "opponent"})
                    ])

    # rename column now to avoid value like _x
    df_game_havoc = df_game_havoc.rename(columns = {"season": "season_havoc", "week": "week_havoc", "opponent": "opponent_havoc"})

    df_game_havoc_final = (df_game
                          .merge(
                          df_game_havoc, 
                          on = ["game_id", "team"], 
                          how = "left"
    )
    )

    # transform in json
    df_game_havoc_final = df_game_havoc_final.to_json(orient = "records", indent = 4)
     
    # copy now the text
    with open("data/raw/derived/merge_game_havoc_stats_sample.json", "w") as json_merge_havoc_stats: 
         json_merge_havoc_stats.write(df_game_havoc_final)
    
    return f"🤸 the file has been copied successfully"

# valfetc_game  = fetch_games()
# valfetchavoc = fetch_game_havoc()
# parsegame = parse_games(valfetc_game)
# parsehavoc = parse_game_havoc(valfetchavoc)
# print(merge_game_havoc(parsegame, parsehavoc))