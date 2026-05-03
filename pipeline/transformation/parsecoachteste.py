import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root) 




def parse_teste_coach(testecoachval, testecoacconf, testcoachgames): 
    awayconf = testecoacconf.get(testcoachgames[0]["away_team"])
    homeconf = testecoacconf.get(testcoachgames[0]["home_team"])
# 1 Identifier le coach 
    coach_dict = {}
    for i in testecoachval: 
        coachfullname = i["first_name"] + " " + i["last_name"]
        # on récupère la première saison du coach
        team = i["seasons"][0]["school"]
        coach_dict[coachfullname] = {
            "team": team,  
            "hire_date": i["hire_date"], 
            "season": { s["year"]: [] for s in i["seasons"]}
        }
        

# 2 Parcourir les matchs et pour chaque macth qui est la hometeam , la away team , les point marqué et la saison 
            
    for k in testcoachgames: 
        home = k["home_team"]
        away = k["away_team"]
        season = k["season"]
   
        game_home = {
            "game_id": k["id"], 
            "week": k["week"],
            "opponent": away, 
            "conference_opponent": awayconf, 
            "result": "W" if k["home_points"] > k["away_points"] else "L", 
            "points_for": k["home_points"], 
            "points_against": k["away_points"]
            
        }   

        game_away = {
            "game_id": k["id"], 
            "week": k["week"],
            "opponent": home, 
            "conference_opponent": homeconf, 
            "result": "W" if k["away_points"] > k["home_points"] else "L", 
            "points_for": k["home_points"], 
            "points_against": k["away_points"]     
        }   



# 3 Assigner le bon coach au bon jeux 
       
        for coachfullname , info in coach_dict.items():    
        
        # # si le coach dirige l'équipe à domicile 
            if info["team"] == home and season in info["season"]: 
                info["season"][season].append(game_home)

        # # si le coach dirige l'équipe à l'extérieur 
            if info["team"] == away and season in info["season"]:
               info["season"][season].append(game_away)



# 5 construction de la sortie finale 
    resultfinal = []
    for coachfullname, info in coach_dict.items():
        for season, games in info["season"].items(): 
            resultfinal.append({
                "coach": coachfullname, 
                "team": info["team"],
                "hire_date": info["hire_date"], 
                "season": season,
                "games": games
            })

    return resultfinal









from pipeline.scrapers.games import fetch_games
from pipeline.scrapers.conference import fetch_conference
from pipeline.scrapers.coaches import fetch_coaches
valgame = fetch_games(2023)
valconfe = fetch_conference(2023)
valcoaches = fetch_coaches(2023)
print(parse_teste_coach(valcoaches, valconfe, valgame))
