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
        team = coach["school"]
        season = coach["season"]
    

        coach_index[fullname] =  {
            "team": team, 
            "hire_date": coach["hire_date"], 
            "season":season,
            "games": []
        }
    #3 route of games
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
            "result": "W" if g["home_points"] > g["away_points"] else "L", 
            "points_for": g["home_points"],
            "points_against": g["away_points"], 
            "location": "home"
        }

        # away side 

        match_away = {
            "game_id" : g["id"], 
            "week": g["week"],
            "opponent": home,
            "opponent_conference": conf_index.get(home),
            "result": "w" if g["away_points"] > g["home_points"] else "L", 
            "points_for": g["away_points"],
            "points_against": g["home_points"], 
            "location": "away"
        }

    #4 assign the good coach to the good game  
        for coach_name, info in coach_index.items(): 

        # The coach can only coach his own season.
            if season != info["season"]:
                continue

        # if the coach lead the home team 
            if info["team"] == home:
               info["games"].append(match_home)

        # if the coach lead the home team 
            if info["team"] == away:
               info["games"].append(match_away)

    #5) Construire la sortie finale 
    output = []
    for coach_name, info in coach_index.items(): 
       
            output.append({
                "coach": coach_name, 
                "team": info["team"], 
                "hire_date": info["hire_date"], 
                "season": info["season"], 
                "games": info["games"]
            })


    return output

# from pipeline.scrapers.coaches import fetch_coaches
# from pipeline.scrapers.games import fetch_games
# from pipeline.scrapers.conference import fetch_conference
# valcachmatchupcoach = fetch_coaches(2023)
# valcachmatchupgames = fetch_games(2023)
# valcachmatchupconf = fetch_conference(2023)
# print(parse_coach_matchup(valcachmatchupcoach, valcachmatchupgames, valcachmatchupconf))


