import sys
from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.transformation.cfbd.parse_games import parse_games
from pipeline.transformation.cfbd.parse_game_team_stats import parse_game_team_stats 

from pipeline.scrapers.cfbd.games import fetch_games
from pipeline.scrapers.cfbd.game_team_stat import fetch_game_team_stats


def merge_games_team_stats(raw_parse_game, raw_parse_game_stats): 
    # transform into DataFrame 
    df_games = pd.DataFrame(raw_parse_game)
    df_games_stats = pd.DataFrame(raw_parse_game_stats)

    # create away and point_away  column  
    df_games["away"] = df_games["away_team"]
    df_games["points_away"] = df_games["away_points"]
    df_games["conference_away"] = df_games["away_conference"]
    df_games["id_away"] = df_games["away_id"]
     # merge in home 
    df_games_int_home = df_games.merge(
        df_games_stats, 
        left_on = ["game_id", "home_id", "home_team", "home_conference"],
        right_on = ["game_id", "team_id", "team", "conference"],
        how = "left"
    )

    # complete the  column away with home_team and point
    df_games["away"] = df_games["home_team"]
    df_games["points_away"] = df_games["home_points"]
    df_games["conference_away"] = df_games["home_conference"]
    df_games["id_away"] = df_games["home_id"]

    # merge in away 
    df_games_int_away = df_games.merge(
        df_games_stats, 
        left_on = ["game_id", "away_id", "away_team", "away_conference"],
        right_on = ["game_id", "team_id", "team", "conference"],
        how = "left"
    )

   
    # add flag home and away 
    df_games_int_home["team_side"] = "home"
    df_games_int_away["team_side"] = "away"
    
    # print(df_games_int_away.info())
    # concat all the merge in order to have the final one
    df_games_final = pd.concat([df_games_int_home, df_games_int_away])

    # # return df_games_final.columns
    # return df_games_final[["game_id", "season", "week", "team", "team_id", "home_id", "conference", "points", "away", "id_away", "away_id","conference_away",
    #                         "points_away", "home_points","home_team","home_conference", "away_team", "away_conference", "away_points",
    #                         "home_line_scores", "away_line_scores", "team_side"]]
    # transform in json format
    
    # df_games_final.info()
    df_games_final = df_games_final.to_json(orient = "records",  indent = 4)
    
    # write in my data/raw/derived/
    with open("data/raw/derived/merge_game_team_stats_sample.json", "w")as jsonmerge_games_team_stats : 
         jsonmerge_games_team_stats.write(df_games_final)
   

    return f"🤸 the file has been copied succesfully"
  
# print(df_games_int_away.info())

# valfetchgame  = fetch_games()
# vallfetcgame_team = fetch_game_team_stats()
# val_parse_game = parse_games(valfetchgame)
# vall_parse_game_team = parse_game_team_stats(vallfetcgame_team)
# print(merge_games_team_stats(val_parse_game, vall_parse_game_team))
