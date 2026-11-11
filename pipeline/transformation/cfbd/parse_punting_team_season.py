import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.punting_team_season import fetch_punting_team_season

def parse_punting_team_season(raw_punting_team_season): 
    list_punting_team_season = []
    for i_punting_team_season in raw_punting_team_season: 
        dict_punting_team_season = {
            "season": int(i_punting_team_season["season"]), 
            "team": i_punting_team_season["team"], 
            "conference": i_punting_team_season["conference"], 

            # attempts ,yards
            "punt_attempts": int(i_punting_team_season["punting"]["punts"]), 
            "punt_yards": int(i_punting_team_season["punting"]["puntYards"]), 
            "yards_per_punt": float(i_punting_team_season["punting"]["yardsPerPunt"]),
            # long, 50
            "punt_long": int(i_punting_team_season["punting"]["longestPunt"]),
            "punt_50_plus": int(i_punting_team_season["punting"]["punts50Plus"]),
            # net 
            "net_punt_yards": int(i_punting_team_season["punting"]["netPuntYards"]),
            "net_yards_per_punt": float(i_punting_team_season["punting"]["netYardsPerPunt"]),
            # touch fair out
            "punt_touchbacks": int(i_punting_team_season["punting"]["touchbacks"]),
            "punt_fair_catches": int(i_punting_team_season["punting"]["fairCatches"]),
            "punt_out_of_bounds": int(i_punting_team_season["punting"]["outOfBounds"]),
            # inside , blocked
            "punt_inside_20": int(i_punting_team_season["punting"]["inside20"]),
            "punt_blocked": int(i_punting_team_season["punting"]["blocked"]),
            # return
            "punt_returns": int(i_punting_team_season["returning"]["returns"]),
            "punt_returns_yards": int(i_punting_team_season["returning"]["returnYards"]),
            "yards_per_return": float(i_punting_team_season["returning"]["yardsPerReturn"]),
            # long, 20
            "punt_returns_long": int(i_punting_team_season["returning"]["longestReturn"]),
            "punt_returns_20_plus": int(i_punting_team_season["returning"]["returns20Plus"]),
            # touch_downs, muffs
            "punt_returns_touchdowns": int(i_punting_team_season["returning"]["returnTouchdowns"]),
            "punt_return_muffs": int(i_punting_team_season["returning"]["muffs"])
        } 

        list_punting_team_season.append(dict_punting_team_season) 


    return list_punting_team_season


val = fetch_punting_team_season()
print(parse_punting_team_season(val))
