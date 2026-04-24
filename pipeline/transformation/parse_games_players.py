import os 
import sys 
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root)


def parse_games_players_stats(raws_value, season, week): 
    vallistefinal = []
    game_id = raws_value["id"]
    
    #loop on each teams
    for team in raws_value["teams"]:
        # print(team)
        team_name = team["team"] 
        conference = team["conference"]
        home_away = team["homeAway"]
        points = team["points"]
        # loop on categories 
        for category in team["categories"]: 
            category_name = category["name"] 
        # Loop on types
            for state_type in category["types"]: 
                state_type_name = state_type["name"]
                # loop on athlete
                for athlete in state_type["athletes"]: 
                    rowdict = {
                        "game_id": game_id,
                        "team": team_name, 
                        "conference":conference, 
                        "home_away": home_away, 
                        "points":points, 
                        "category":category_name, 
                        "stat_type":state_type_name,
                        "player_id":athlete["id"], 
                        "player_name":athlete["name"], 
                        "stat_value": athlete["stat"], 

                    }
                    rowdict["season"] = season
                    rowdict["week"] = week 
                    vallistefinal.append(rowdict)
    return vallistefinal
        

from pipeline.loaders.load_games_players_stats import load_games_players

raw = load_games_players()
parsed = parse_games_players_stats(raw, season = 2023, week = 1)
print(parsed)