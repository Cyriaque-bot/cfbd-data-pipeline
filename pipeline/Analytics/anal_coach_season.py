import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
   sys.path.insert(0,project_root) 


def analyze_coach_season(coach_season_data): 
    games = coach_season_data["games"]
                         
# Overall summary 

    wins = sum(1 for g in games if g["result"] == "W")
    losses = sum(1 for g in games if g["result"] == "L")
    games_played = len(games)

    points_for_totals = sum(g["points_for"] for g in games)
    points_against_totals = sum(g["points_against"] for g in games)

    points_for_avg = points_for_totals/games_played if games_played else 0
    points_against_avg = points_against_totals/games_played if games_played else 0
    points_diff_avg = points_for_avg - points_against_avg

    # Home / Away 
    record_home = {"W": 0, "L": 0}
    record_away = {"W": 0, "L": 0}

    for g in games: 
        if g["location"] == "home":
            record_home[g["result"]] =  record_home[g["result"]] + 1
        else: 
            record_away[g["result"]] = record_away[g["result"]] + 1

    # Conference 
    record_by_conference = {}
    for g in games : 
        conf = g["opponent_conference"]
        if conf not in record_by_conference: 
            record_by_conference[conf] = {"W": 0, "L": 0}
        record_by_conference[conf][g["result"]] = record_by_conference[conf][g["result"]] + 1

    # Biggest win / loss
    biggest_win = None 
    biggest_loss = None 
    for g in games: 
        diff = g["points_for"] - g["points_against"]

        if diff > 0 : 
            if biggest_win is None or diff > biggest_win["diff"]: 
               biggest_win = {**g, "diff": diff}
           
        if diff < 0: 
            if biggest_loss is None or diff < biggest_loss["diff"]: 
                biggest_loss = {**g, "diff": diff}
     

    # opponent summary 
    opponents_summary = {}
    for g in games: 
        opp = g["opponent"]
        if opp not in opponents_summary: 
           opponents_summary[opp] = {"W": 0, "L": 0}
        opponents_summary[opp][g["result"]] = opponents_summary[opp][g["result"]] + 1
    
    return {
        "coach": coach_season_data["coach"], 
        "team": coach_season_data["team"], 
        "season": coach_season_data["season"], 

        "games_played": games_played, 
        "wins": wins, 
        "losses": losses, 
        "win_rate": wins/games_played if games_played else 0, 

        "points_for_totals": points_for_totals, 
        "points_against_totals": points_against_totals, 
        "points_for_avg": points_for_avg, 
        "points_against_avg": points_against_avg, 
        "points_diff_avg": points_diff_avg, 

        "record_home": record_home, 
        "record_away": record_away, 

        "record_by_conference": record_by_conference, 

        "biggest_win": biggest_win, 
        "biggest_loss": biggest_loss, 

        "opponents_summary": opponents_summary

    }
from pipeline.loaders.load_coaches import loads_coaches
from pipeline.loaders.load_games import load_games
from pipeline.loaders.load_conference import load_conference
rawmachupcoach = loads_coaches()
rawmachupgames = load_games()
rawmachupconf = load_conference()
from pipeline.transformation.parse_coach_matchup import parse_coach_matchup
parsed = parse_coach_matchup(rawmachupcoach, rawmachupgames, rawmachupconf)
# print(parsed)
for season_data in parsed : 
    print(analyze_coach_season(season_data))
