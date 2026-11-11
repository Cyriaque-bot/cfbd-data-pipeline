import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.rushing_team_season import fetch_rushing_team_season

def parse_rushing_team_season(raw_rushing_team_season): 
    list_rushing_team_season = []
    for i_rushing_team_season in raw_rushing_team_season: 
        dict_rushing_team_season = {
            "season": int(i_rushing_team_season["season"]), 
            "team": i_rushing_team_season["team"], 
            "conference": i_rushing_team_season["conference"], 
            # attempts , yards
            "rushing_attempts": int(i_rushing_team_season["offense"]["attempts"]), 
            "rushing_yards": int(i_rushing_team_season["offense"]["totalRushingYards"]), 
            # touchdowns
            "rushing_touchdowns": int(i_rushing_team_season["offense"]["rushingTouchdowns"]), 
            # yards 
            "yards_per_carry": float(i_rushing_team_season["offense"]["yardsPerCarry"]), 
            # sacs 
            "rushing_sacks": int(i_rushing_team_season["offense"]["sacks"]), 
            # lineYards
            "line_yards": float(i_rushing_team_season["offense"]["lineYards"]), 
            "line_yards_total": int(i_rushing_team_season["offense"]["lineYardsTotal"]),
            # level
            "second_level_yards": float(i_rushing_team_season["offense"]["secondLevelYards"]),
            "second_level_yards_total": int(i_rushing_team_season["offense"]["secondLevelYardsTotal"]),
            # fields
            "open_field_yards": float(i_rushing_team_season["offense"]["openFieldYards"]),
            "open_field_yards_total": int(i_rushing_team_season["offense"]["openFieldYardsTotal"]),
            # rate , success
            "stuff_rate": float(i_rushing_team_season["offense"]["stuffRate"]),
            "power_success": float(i_rushing_team_season["offense"]["powerSuccess"]),
            # rushing_explosiveness
            "rushing_explosiveness": float(i_rushing_team_season["offense"]["explosiveness"])
        }

        list_rushing_team_season.append(dict_rushing_team_season) 


    return list_rushing_team_season

val = fetch_rushing_team_season()
print(parse_rushing_team_season(val))