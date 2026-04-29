import sys 
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)



def parse_team_matchup(rawteammactup): 
    valistreammactup = []
    for i in rawteammactup: 
        daldictteammatchup = {
            "season": i["season"], 
            "week": i["week"], 
            "season_type": i["season_type"], 
            "date": i["date"], 
            "winner": i["winner"], 
            "loser": i["loser"], 
            "winner_points": i["winner_points"], 
            "loser_points": i["loser_points"]
        }
        valistreammactup.append(daldictteammatchup)
    
    return valistreammactup

# from pipeline.scrapers.teams_matchups import fetch_load_team

# vallteammatcup = fetch_load_team(2023)
# print(parse_team_macthup(vallteammatcup))