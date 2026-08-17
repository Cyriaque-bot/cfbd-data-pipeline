import sys 
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.ppa_team import fetch_ppa_team

def parse_ppa_team(raw_ppa_team): 
    list_raw_ppa_team = []
    for i_list_raw_ppa_team in raw_ppa_team: 
        dict_raw_ppa_team = {
            "school": i_list_raw_ppa_team["team"], 
            "conference": i_list_raw_ppa_team["conference"], 
            "season": int(i_list_raw_ppa_team["season"]), 

            "ppa_overall_offense": float(i_list_raw_ppa_team["offense"]["cumulative"]["total"]), 
            "ppa_passing_offense": float(i_list_raw_ppa_team["offense"]["cumulative"]["passing"]), 
            "ppa_rushing_offense": float(i_list_raw_ppa_team["offense"]["cumulative"]["rushing"]),    

            "ppa_overall_defense": float(i_list_raw_ppa_team["defense"]["cumulative"]["total"]), 
            "ppa_passing_defense": float(i_list_raw_ppa_team["defense"]["cumulative"]["passing"]), 
            "ppa_rushing_defense": float(i_list_raw_ppa_team["defense"]["cumulative"]["rushing"]),                                         
        }
        list_raw_ppa_team.append(dict_raw_ppa_team)
    return list_raw_ppa_team


# vallfetch = fetch_ppa_team()
# print(parse_ppa_team(vallfetch))