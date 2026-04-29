import os
import sys 

# add project_root to the sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)



def parse_conference_matchup (raw_games, team_to_conf): 
    listrawval = []

    for i in raw_games: 
        #1 retrieve all teams 
        home = i["home_team"]
        away = i["away_team"]

        #2 retrieve all conferences
        home_conf = team_to_conf.get(home)
        away_conf = team_to_conf.get(away)

        # if a conference is unknown , we ignore the game 
        if home_conf is None or away_conf is None:
            continue

        #filtered an keep the game coming from differents conference
        if home_conf == away_conf: 
            continue
        #4 Determined winner/loser 
        if i["home_points"] > i["away_points"]:
            winnerconf = home_conf
            loserconf = away_conf
        else: 
            winnerconf = away_conf
            loserconf = home_conf

        #5 Derived Fields 
        margin = abs(i["home_points"] - i["away_points"])
        notes = i.get("notes", "")

        is_playoff_game = (
            i["season_type"] == "postseason"
            and isinstance(notes, str) and "CFP" in notes
        )
   
        is_bowl_game = (
            i["season_type"] == "postseason"
            and not is_playoff_game
        )

        #6 building the lastobject
        valdictrawvalone = {
            "season": i["season"], 
            "week": i["week"],
            "season_type": i["season_type"],
            "game_id": i["id"], 
            "home_team": home, 
            "away_team": away, 
            "home_conference": home_conf, 
            "away_conference": away_conf,
            "home_point": i["home_points"], 
            "away_point": i["away_points"], 
            "winner_conference": winnerconf, 
            "loser_conference": loserconf, 
            "margin": margin,
            "neutral_site": i["neutral_site"],
            "is_playoff_game": is_playoff_game, 
            "is_bowl_game": is_bowl_game
        }
        listrawval.append(valdictrawvalone)
                
    return listrawval

from pipeline.scrapers.conference import fetch_conference
from pipeline.scrapers.games import fetch_games

valresultone = fetch_games(2023)
valresulttwo = fetch_conference(2023)
print(parse_conference_matchup(valresultone, valresulttwo))