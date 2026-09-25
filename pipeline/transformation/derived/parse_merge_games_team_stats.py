import sys
from pathlib import Path 


project_root  = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))




from pipeline.scrapers.derived.merge_games_team_stats import fetch_merge_games_team_stats

def parse_games_team_stats(raw_parse_games_team_stats): 
   
    list_fetch_merge_game_team = []
    
    for i_fetch_merge_game_team in raw_parse_games_team_stats: 
        
        # third_down_eff
        def fnct_third_down_eff(): 
            third_down_eff = i_fetch_merge_game_team["third_down_eff"]
            try: 
                result_third_down_eff =  round(int(third_down_eff[:third_down_eff.find("-")]) / int(third_down_eff[third_down_eff.find("-") + 1:]), 2)
                return result_third_down_eff
            except:
                return None

        #  fourth_down_eff
        def fnct_fourth_down_eff(): 
            fourth_down_eff = i_fetch_merge_game_team["fourth_down_eff"]
            try: 
               result_fourth_down_eff_left = round(int(fourth_down_eff[:fourth_down_eff.find("-")]) / int(fourth_down_eff[fourth_down_eff.find("-") + 1:]), 2) 
               return result_fourth_down_eff_left              
            except:
                return None 
        

        dict_fetch_merge_game_team = {
            "game_id" : i_fetch_merge_game_team["game_id"], 
            "season" : i_fetch_merge_game_team["season"], 
            "team": i_fetch_merge_game_team["team"], 
            "team_id": i_fetch_merge_game_team["team_id"], 
            "team_points": i_fetch_merge_game_team["points"],
            "week" : i_fetch_merge_game_team["week"], 

            "opponent": i_fetch_merge_game_team["away"],
            "opponent_id": i_fetch_merge_game_team["id_away"],
            "opponent_points":i_fetch_merge_game_team["points_away"],
            "season_type": i_fetch_merge_game_team["season_type"], 
            "start_date": i_fetch_merge_game_team["start_date"],
            "completed": i_fetch_merge_game_team["completed"], 
            "neutral_site": i_fetch_merge_game_team["neutral_site"], 
            "conference_game": i_fetch_merge_game_team["conference_game"], 
            "venue": i_fetch_merge_game_team["venue"], 

            "yards_total": i_fetch_merge_game_team["total_yards"], 
            "rushing_yards": i_fetch_merge_game_team["rushing_yards"], 
            "passing_yards": i_fetch_merge_game_team["net_passing_yards"], 
            "turnovers": i_fetch_merge_game_team["turnovers"], 
            "team_side": i_fetch_merge_game_team["team_side"],
            "third_down_pct": fnct_third_down_eff(), 
            "fourth_down_pct":fnct_fourth_down_eff()
        }
        list_fetch_merge_game_team.append(dict_fetch_merge_game_team)

    return   list_fetch_merge_game_team


# val = fetch_merge_games_team_stats()
# print(parse_games_team_stats(val))