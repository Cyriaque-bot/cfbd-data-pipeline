import sys
from pathlib import Path
import pandas as pd 
import re


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.cfbd.team_roster import fetch_team_roster
from pipeline.scrapers.cfbd.stats_player_season import fetch_stats_player_season


from pipeline.transformation.cfbd.parse_team_roster import parse_team_roster
from pipeline.transformation.cfbd.parse_stats_player_season import parse_stats_player_season

def compute_returning_production_player(raw_parse_stats_player_season, raw_parse_team_roster): 
    df_stat_player = pd.DataFrame(raw_parse_stats_player_season)
    df_stat_roster  = pd.DataFrame(raw_parse_team_roster)

   
    # taking team_roster totall and team_roster with filter returnin = True
    
    # team_roster_totall 
    df_stat_roster_n = df_stat_roster[["player_id" , "team", "position"]]
    # filter on year for  N + 1 
    df_stat_roster_n_1 = df_stat_roster.loc[df_stat_roster["returning"] == True, ["player_id", "team", "position"]]

    # N + 1 
    df_stat_player_int_n_1 = df_stat_player.merge(
        df_stat_roster_n_1[["player_id", "team", "position"]].rename(columns = {"team": "team_roster", "position": "position_roster"}), 
        on = "player_id", 
        how = "inner"
    )
    # N 
    df_stat_player_int_n = df_stat_player.merge(
        df_stat_roster_n[["player_id", "team", "position"]].rename(columns = {"team": "team_roster", "position": "position_roster"}), 
        on = "player_id", 
        how = "inner"
    )
    
    # retrieving a part of df_stat_player_int_n_1 
    df_stat_player_int_part  = df_stat_player_int_n_1[["player_id", "category", "stat_type", "stat"]]

    # retrieving a part of df_stat_player_int_n 
    # df_stat_player_int_part_n  = df_stat_player_int_n[["player_id", "category", "stat_type", "stat"]]

    # return df_stat_player_int_part
    # initialising my new column
    
                                # condition offense
    condition_offense = ( 
                    (df_stat_player_int_part["category"].isin(["passing","rushing","receiving"]))
                    & 
                    (df_stat_player_int_part["stat_type"].isin(["yards","touchdowns","attempts","completions", "interceptions", 
                                                                "touchdowns", "attempts", "receptions"]))         
               )
    df_stat_player_int_part["val_offense"] = None

    df_stat_player_int_part.loc[condition_offense, "val_offense"] = (
        df_stat_player_int_part["category"] + "_" + df_stat_player_int_part["stat_type"]
    )

                                # condition defense 

    condition_defense  = (
        (df_stat_player_int_part["category"].isin(["defense", "interceptions", "fumbles"]))
        &
        (df_stat_player_int_part["stat_type"].isin(["tackles", "soloTackles", "assistedTackles", 
                                                   "sacks", "qbHurries", "passesDefended", "tfl"]))
    )
    # filtrate the dataFrame 
    def transformer_stat_defense(val_defense):
        if any(c.isupper()for c in val_defense):
            # if uppercase we add "_" and we change in lower case
            return re.sub(r'(?<!^)(?=[A-Z])', '_', val_defense).lower()
        elif val_defense == "tfl": 
            return "tackles_for_loss"
        else: 
            return val_defense
    df_stat_player_int_part["result_defense"] = None
    # apply the transfomer only in line that fully complete the transformation 
    df_stat_player_int_part.loc[condition_defense, "result_defense"] = (
        df_stat_player_int_part.loc[condition_defense, "stat_type"].apply(transformer_stat_defense)
    )

                            # conditition special team

    condition_special_teams = (
        df_stat_player_int_part["category"].isin(["kicking", "punting", "kickReturns", "puntReturns"])
        &
        df_stat_player_int_part["stat_type"].isin(["fgMade", "fgAttempted", "xpMade", "xpAttempted", "punts", "yards", "long", "yards", "touchdowns"])
    )
    
    def transformer_special_team(row):
        
        val_special_team_cat  = row["category"]
        val_special_team_stat = row["stat_type"] 

        
        if any(c.isupper() for c in val_special_team_stat): 
            return re.sub(r'(?<!^)(?=[A-Z])', "_", val_special_team_stat).lower()
        elif val_special_team_cat == "punting" and val_special_team_stat in ("yards", "long"): 
            return val_special_team_cat[0:4] + "_" + val_special_team_stat
        elif val_special_team_cat == "punting" and val_special_team_stat == "punts": 
            return "punt_attempts"
        elif val_special_team_cat in ("kickReturns", "puntReturns") and val_special_team_stat in ("yards", "touchdowns"): 
            return re.sub(r'(?<!^)(?=[A-Z])', "_", val_special_team_cat).lower() + "_" + val_special_team_stat
        else: 
            return val_special_team_stat



    df_stat_player_int_part["result_special_team"] =  None

    df_stat_player_int_part.loc[condition_special_teams, "result_special_team"] = (
        df_stat_player_int_part.loc[condition_special_teams, ["stat_type", "category"]].apply(transformer_special_team, axis = 1 )
    )
    # a forme of merge of the columns val_offense, result_defense, result_special_team
    df_stat_player_int_part["stat_player"] = (
                                             df_stat_player_int_part["val_offense"]
                                             .fillna(df_stat_player_int_part["result_defense"])
                                             .fillna(df_stat_player_int_part["result_special_team"])
                                             ) 

    # drop column val_offense
    df_stat_player_int_part = df_stat_player_int_part.drop(columns = {"val_offense", "result_defense", "result_special_team"})
    
    #new df_stat_player_int_part
   
    df_stat_player_int_part = df_stat_player_int_part[["player_id", "stat", "stat_player"]]

#     duplicates = df_stat_player_int_part[
#     df_stat_player_int_part.duplicated(
#         subset=["player_id", "stat_player"],
#         keep=False
#     )
# ]

#     print(duplicates)

    # pivoting

    df_stat_player_int_part = df_stat_player_int_part.pivot(index = "player_id", columns = "stat_player", values = "stat").reset_index()


    # print(df_stat_player_int_part)
    # print(len(df_stat_player_int_part))
    # print(df_stat_player_int_part["player_id"].nunique())  

    
    # jusqu'ici il n'ya pas de problème 
    # retrieving strict minimum from df_stat_player_int
    df_stat_player_int_n_1 = df_stat_player_int_n_1[["player_id", "team", "season"]]
    # retrieving strict minimum from df_stat_player_int
    df_stat_player_int_n = df_stat_player_int_n[["player_id", "team", "season"]]

    
    # drop duplicate for both df_stat_player_int_n, df_stat_player_int_n_1
    df_stat_player_int_n = df_stat_player_int_n[["player_id", "team", "season"]].drop_duplicates()
    df_stat_player_int_n_1 = df_stat_player_int_n_1[["player_id", "team", "season"]].drop_duplicates()

    
    # print(
    # df_stat_player_int_n[
    #     df_stat_player_int_n["player_id"] == 10101
    # ]
    # )

    # make my join between df_stat_player_int and df_stat_player_int_part
    df_stat_player_final_n_1  = df_stat_player_int_n_1.merge(
      df_stat_player_int_part, 
      on = "player_id", 
      how = "left"
    ).fillna(0)

    # make my join between df_stat_player_int and df_stat_player_int_part
    df_stat_player_final_n  = df_stat_player_int_n.merge(
      df_stat_player_int_part, 
      on = "player_id", 
      how = "left"
    ).fillna(0)

    # print("N")
    # print(df_stat_player_final_n["player_id"].unique())
  
    # print("N+1")
    # print(df_stat_player_final_n_1["player_id"].unique())
  

    # transforme all of them in json
    df_stat_player_final_n_1 = df_stat_player_final_n_1.to_json(orient = "records",  indent = 4)
    df_stat_player_final_n = df_stat_player_final_n.to_json(orient = "records",  indent = 4)

    with open("data/raw/derived/returning_production_player_n_1_sample.json", "w") as json_returning_production_player_n_1: 
         json_returning_production_player_n_1.write(df_stat_player_final_n_1)

    with open("data/raw/derived/returning_production_player_n_sample.json", "w") as json_returning_production_player_n: 
         json_returning_production_player_n.write(df_stat_player_final_n)
    
    
    return f"🤸 congratulation you file has been copied succesfully"


# valplyares = fetch_stats_player_season()
# valroster = fetch_team_roster()
# parse_stats_player = parse_stats_player_season(valplyares)
# parse_teamv_roster = parse_team_roster(valroster)
# print(compute_returning_production_player(parse_stats_player, parse_teamv_roster))