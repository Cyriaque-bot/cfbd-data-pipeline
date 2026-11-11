import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.passing_team_season import fetch_passing_team_season

def parse_passing_team_season(raw_passing_team_season): 
    list_passing_team_season = []
    for i_passing_team_season in raw_passing_team_season: 
        dict_passing_team_season = {
            "season": int(i_passing_team_season["season"]), 
            "team": i_passing_team_season["team"], 
            "conference": i_passing_team_season["conference"], 
            # attempts , completion, incompletion, interceptions
            "passing_attempts": int(i_passing_team_season["offense"]["attempts"]), 
            "passing_completions":  int(i_passing_team_season["offense"]["completions"]), 
            "passing_incompletions": int(i_passing_team_season["offense"]["incompletions"]), 
            "passing_interceptions": int(i_passing_team_season["offense"]["interceptions"]), 
            # rate 
            "passing_completion_rate": float(i_passing_team_season["offense"]["completionRate"]), 
            # yards
            "passing_air_yards": int(i_passing_team_season["offense"]["totalAirYards"]), 
            "passing_yards": int(i_passing_team_season["offense"]["totalYards"]), 
            "passing_yards_after_catch": int(i_passing_team_season["offense"]["totalYardsAfterCatch"]), 
            # success, ppa
            "passing_success_rate": float(i_passing_team_season["offense"]["successRate"]),
            "passing_ppa": float(i_passing_team_season["offense"]["ppa"]),
            "passing_total_ppa": float(i_passing_team_season["offense"]["totalPpa"]),
            # explosiveness, attempts
            "passing_explosiveness": float(i_passing_team_season["offense"]["explosiveness"]),
            "passing_successful_attempts": int(i_passing_team_season["offense"]["successfulAttempts"]),
            # cpoe
            "passing_cpoe": float(i_passing_team_season["offense"]["cpoe"])
        }

        list_passing_team_season.append(dict_passing_team_season) 


    return list_passing_team_season

val = fetch_passing_team_season()
print(parse_passing_team_season(val))