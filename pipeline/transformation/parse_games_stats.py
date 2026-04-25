import sys
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)

def parse_games_stats(rawgamesstat): 
    games_statlist = []
    for i in rawgamesstat: 
        gamestatdictone = {
            "game_id": i["id"], 
            "season": i["season"], 
            "week": i["week"], 
            "team": i["team"], 
            "home_away": i["home_away"], 
            "points": i["points"]
        }
        for j in i["categories"]: 
            gamestatdictwo = {
                **gamestatdictone, 
                "category": j["name"]
            }
            for k in j["types"]: 
                gamestatdicthree = {
                    **gamestatdictwo, 
                    "stat_type": k["name"],
                    "stat_value": k["stat"]
                }

                # Add all my data in my list 
                games_statlist.append(gamestatdicthree)


    return games_statlist
 
from pipeline.scrapers.games_stats import fecth_all_game_team_stat
vallresult = fecth_all_game_team_stat(2023)
print(parse_games_stats(vallresult))