import os 
import sys 

import pandas as pd 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

def parse_games(games_raws): 
    listgames = []
    for g in games_raws: 
        gamedict = {
                    "game_id": g["id"], 
                    "season": g["season"], 
                    "week": g["week"], 
                    "season_type": g["season_type"], 
                    "date": g["start_date"], 

                    # Information de lieu 
                    "neutral_site": g["neutral_site"], 
                    "conference_game":g["conference_game"], 
                    "venue": g["venue"], 

                    # Home / Away
                    "home_team": g["home_team"], 
                    "away_team": g["away_team"], 
                    "home_points": g["home_points"], 
                    "away_points": g["away_points"]
              }
        listgames.append(gamedict)

    # Conversion en DataFrame
    df = pd.DataFrame(listgames)

    # Normalisation des types 
    df["season"] = df["season"].astype(int)
    df["week"] = df["week"].astype(int)
    df["season_type"] = df["season_type"].astype(str)

    return df
    

# def parse_games(games_raw): 
#     df = pd.DataFrame(games_raw)
   
#     # Normalisation des noms de colonnes 
#     df = df.rename(columns = {
#         "id"
#     })
# from pipeline.scrapers.games import fetch_games
# valgames = fetch_games(2023)
# print(parse_games(valgames))