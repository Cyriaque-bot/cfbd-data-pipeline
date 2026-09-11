import os 
import sys 

import pandas as pd 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

def parse_games(games_raws): 
    listgames = []
    for i_games in games_raws: 
        gamedict = {
                    "game_id": int(i_games["id"]), 
                    "season": int(i_games["season"]), 
                    "week": int(i_games["week"]), 
                    "season_type": i_games["seasonType"], 
                    "start_date": i_games["startDate"],
                    "completed": i_games["completed"], 
                    "neutral_site": i_games["neutralSite"],
                    "conference_game":i_games["conferenceGame"], 

                    # venue & attendance
                    "venue_id": int(i_games["venueId"]),
                    "venue": i_games["venue"],
                    "attendance": int(i_games["attendance"]),


                    #  home team
                    "home_id": int(i_games["homeId"]),
                    "home_team" : i_games["homeTeam"],
                    "home_conference": i_games["homeConference"],
                    "home_classification": i_games["homeClassification"],
                    "home_points": int(i_games["homePoints"]),
                    "home_line_scores": i_games["homeLineScores"], 
                    "home_pregame_elo": int(i_games["homePregameElo"]), 
                    "home_postgame_elo": int(i_games["homePostgameElo"]),
                    "home_win_prob_postgame": float(i_games["homePostgameWinProbability"]), 

                    # away_team
                  
                    "away_id": int(i_games["awayId"]),
                    "away_team": i_games["awayTeam"],
                    "away_conference": i_games["awayConference"], 
                    "away_classification": i_games["awayClassification"],
                    "away_points": int(i_games["awayPoints"]),  
                    "away_line_scores": i_games["awayLineScores"], 
                    "away_pregame_elo": int(i_games["awayPregameElo"]), 
                    "away_postgame_elo": int(i_games["awayPostgameElo"]),
                    "away_win_prob_postgame": float(i_games["awayPostgameWinProbability"]),
                   
                    # extra metadata
                    
                    "excitement_index": float(i_games["excitementIndex"]), 
                    "highlights": i_games["highlights"],
                    "notes":i_games.get("notes"), 
                    "playoff": i_games.get("playoff")
              }
        listgames.append(gamedict)
    return listgames


# def parse_games(games_raw): 
#     df = pd.DataFrame(games_raw)
   
#     # Normalisation des noms de colonnes 
#     df = df.rename(columns = {
#         "id"
#     })
# from pipeline.scrapers.games import fetch_games
# valgames = fetch_games(2023)
# print(parse_games(valgames))