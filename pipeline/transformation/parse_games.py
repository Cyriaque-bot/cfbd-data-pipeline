import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

def parse_games(gamesraws): 
    listgames = []
    for i in gamesraws: 
        gamedict = {
                    "game_id": i["id"], 
                    "season": i["season"], 
                    "week": i["week"], 
                    "season_type": i["season_type"], 
                    "start_date": i["start_date"], 
                    "neutral_site": i["neutral_site"], 
                    "conference_game":i["conference_game"], 
                    "venue": i["venue"], 
                    "home_team": i["home_team"], 
                    "home_points": i["home_points"], 
                    "away_team": i["away_team"], 
                    "away_points": i["away_points"]
              }
        listgames.append(gamedict)

    return listgames

# from pipeline.scrapers.games import fetch_games
# valgames = fecth_games(2023)
# print(parse_games(valgames))