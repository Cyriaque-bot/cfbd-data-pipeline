import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root) 



def parse_coach_matchup(rawmachupcoach, rawmachupgames, rawmachupconf):
    
    """construit un tableau coach -> saison -> liste des matches coachés """
    # 1) Index coach -> infos (team ->conference)
    conf_index = rawmachupconf

    # 2) Index coach ->infos (team, hire_date, seasons)
    coach_index = {}
    for coach in rawmachupcoach: 
        fullname = coach["first_name"] + " " + coach["last_name"]

        # On retrieving first season  teams coach 
        team = coach["seasons"][0]["school"]

        coach_index[fullname] =  {
            "team": team, 
            "hire_date": coach["hire_date"], 
            "seasons": {s["year"]: [] for s in coach["seasons"]}
        }
    #3 route of matches
    for g in rawmachupgames: 
        home = g["home_team"]
        away = g["away_team"]
        season = g["season"]

        # home side 
        match_home = {
            "game_id" : g["id"], 
            "week": g["week"],
            "opponent": away,
            "opponent_conference": conf_index.get(away),
            "result": "w" if g["home_points"] > g["away_points"] else "L", 
            "points_for": g["home_points"],
            "ponts_against": g["away_points"]
        }

        # away side 

        match_away = {
            "game_id" : g["id"], 
            "week": g["week"],
            "opponent": home,
            "opponent_conference": conf_index.get(home),
            "result": "w" if g["away_points"] > g["home_points"] else "L", 
            "points_for": g["away_points"],
            "ponts_against": g["home_points"]
        }

    #4 assign the good coach to the good game  
        for coach_name, info in coach_index.items(): 

        # if the coach lead the home team 
            if info["team"] == home and season in info["season"]:
               info["seasons"][season].append(match_home)

        # if the coach lead the home team 
            if info["team"] == away and season in info["season"]:
               info["seasons"][season].append(match_away)

    #5) Construire la sortie finale 
    output = []
    for coach_name, info in coach_index.items(): 
        for season, games in info["seasons"].items():
            output.append({
                "coach": coach_name, 
                "team": info["team"], 
                "hire_date": info["hire_date"], 
                "season": season, 
                "games": games
            })


    return output

from pipeline.scrapers.coaches import fetch_coaches
from pipeline.scrapers.games import fetch_games
from pipeline.scrapers.conference import fetch_conference
valcachmatchupcoach = fetch_coaches(2023)
valcachmatchupgames = fetch_games(2023)
valcachmatchupconf = fetch_conference(2023)

print(parse_coach_matchup(valcachmatchupcoach, valcachmatchupgames, valcachmatchupconf))
# print(valcachmatchupgames[0])

