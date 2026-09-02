import sys
from pathlib import Path
import pandas as pd 
import json

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.stats_player_season import fetch_stats_player_season

def parse_stats_player_season(raw_stats_player_season): 
   
    df_stats_player = pd.DataFrame(raw_stats_player_season)

    resul_stat =  df_stats_player["category"] == "defense"
    df_stats_player.loc[resul_stat, "category"] = df_stats_player.loc[resul_stat, "statType"]
    # first groupby in order to sum all the stat
    df_player_season  = pd.pivot_table(
        df_stats_player,
        values = "stat", 
        index = ["season", "playerId", "player", "team"],
        columns = "category",
        fill_value = 0
    ).reset_index()
    df_final_player_season = df_player_season.rename(columns = {"passing": "passing_yards", 
                                                                "rushing": "rushing_yards", "receiving": "receiving_yards",
                                                                "tackles": "tackles", "sacks": "sacks", "pressures": "pressures"})
    # missing columns 
    for i_columns in ["passing_yards", "rushing_yards", "receiving_yards", "sacks", "tackles", "pressures"]: 
           if i_columns not in df_final_player_season.columns:
                df_final_player_season[i_columns] = 0
    # convert nan in 0 before conversion 
    df_final_player_season = df_final_player_season.fillna(0)

    # transformations en json 
    df_final_player_season = df_final_player_season.to_dict(orient = "records")

    
   

    for i in df_final_player_season:
        for key_final_player, val_final_player in i.items(): 
            try: 
                i[key_final_player] =  int(val_final_player)
            except ValueError:
                             i[key_final_player] = val_final_player
     
    return df_final_player_season


# val = fetch_stats_player_season()
# print(parse_stats_player_season(val))