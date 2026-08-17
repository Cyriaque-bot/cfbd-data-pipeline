import sys 
from pathlib import Path 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.season_advanced import fetch_season_advanced

def parse_season_advanced(raw_season_advanced): 
    list_season_advanced =  []
    for i_season_advanced in raw_season_advanced: 
        dict_season_advanced = {
          "team": i_season_advanced["team"], 
          "season": i_season_advanced["season"], 
          "epa_offense": float(i_season_advanced["offense"]["ppa"]),
          "epa_defense": float(i_season_advanced["defense"]["ppa"]), 
          "success_rate_offense": float(i_season_advanced["offense"]["successRate"]), 
          "success_rate_defense": float(i_season_advanced["defense"]["successRate"]), 
          "explosiveness_offense": float(i_season_advanced["offense"]["explosiveness"]), 
          "explosiveness_defense": float(i_season_advanced["defense"]["explosiveness"]), 
          "havoc_offense":  float(i_season_advanced["offense"]["havoc"]["total"]), 
          "havoc_defense":  float(i_season_advanced["defense"]["havoc"]["total"]), 
          "finishing_drives_offense": float(i_season_advanced["offense"]["pointsPerOpportunity"]), 
          "finishing_drives_defense": float(i_season_advanced["defense"]["pointsPerOpportunity"]), 
          "field_position_offense": float(i_season_advanced["offense"]["fieldPosition"]["averageStart"]), 
          "field_position_defense": float(i_season_advanced["defense"]["fieldPosition"]["averageStart"])
        }




        list_season_advanced.append(dict_season_advanced) 

    return list_season_advanced




# valseason = fetch_season_advanced()
# print(parse_season_advanced(valseason))