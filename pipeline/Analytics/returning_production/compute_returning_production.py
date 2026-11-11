import sys 
from pathlib import Path 
import pandas as pd 

project_root =  Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.returning_production_team_n import fetch_returning_production_team_n
from pipeline.scrapers.derived.returning_production_team_n_1 import fetch_returning_production_team_n_1


from pipeline.transformation.derived.parse_returning_production_team_n import parse_returning_production_team_n
from pipeline.transformation.derived.parse_returning_production_team_n_1 import parse_returning_production_team_n_1

def compute_returning_production(raw_production_team_n , raw_production_player_n_1): 
    df_raw_production_team_n = pd.DataFrame(raw_production_team_n)
    df_raw_production_player_n_1 = pd.DataFrame(raw_production_player_n_1)

    # small safe function
    def safe_ratio(df, nume_col, denom_col): 
        return(
            df[nume_col]
            .div(df[denom_col].replace(0, pd.NA))
            .fillna(0)
            .round(2)
        )
   
    # merge in order calculate
    df_ratios_production_teams = df_raw_production_team_n.merge(
        df_raw_production_player_n_1, 
        on = ["team_id", "season"], 
        how = "inner"
    )
    df_ratios_production_teams = df_ratios_production_teams.drop(columns = {"team_x", "team_y"})


                            # ratios calculation  
    # passing
       # passing_yards_ratio
    df_ratios_production_teams["passing_yards_ratio"] = safe_ratio(df_ratios_production_teams, "returning_passing_yards", "total_passing_yards")
       # passing_td_ratio
    df_ratios_production_teams["passing_td_ratio"] = safe_ratio(df_ratios_production_teams, "returning_passing_touchdowns", "total_passing_touchdowns")
       # passing attempt
    df_ratios_production_teams["passing_att_ratio"] = safe_ratio(df_ratios_production_teams, "returning_passing_attempts", "total_passing_attempts")
       # passing_comp_ratio
    df_ratios_production_teams["passing_comp_ratio"] = safe_ratio(df_ratios_production_teams, "returning_passing_completions", "total_passing_completions")
       # passing_inter_ratio
    df_ratios_production_teams["passing_inter_ratio"] = safe_ratio(df_ratios_production_teams, "returning_passing_interceptions", "total_passing_interceptions")

    # rushing 
      # rushing_yards_ratio
    df_ratios_production_teams["rushing_yards_ratio"] = safe_ratio(df_ratios_production_teams, "returning_rushing_yards", "total_rushing_yards")
      # rushing_td_ratio
    df_ratios_production_teams["rushing_td_ratio"] = safe_ratio(df_ratios_production_teams, "returning_rushing_touchdowns", "total_rushing_touchdowns")
      # rushing_att_ratio
    df_ratios_production_teams["rushing_att_ratio"] = safe_ratio(df_ratios_production_teams, "returning_rushing_attempts", "total_rushing_attempts")

    # receiving
       # receiving_yards_ratio
    df_ratios_production_teams["receiving_yards_ratio"] = safe_ratio(df_ratios_production_teams, "returning_receiving_yards", "total_receiving_yards")
       # receiving_td_ratio
    df_ratios_production_teams["receiving_td_ratio"] = safe_ratio(df_ratios_production_teams, "returning_receiving_touchdowns", "total_receiving_touchdowns")
       # receiving_recpt_ratio
    df_ratios_production_teams["receiving_recpt_ratio"] = safe_ratio(df_ratios_production_teams, "returning_receiving_receptions", "total_receiving_receptions")

    # tackles , sacks , qb_hurries, defended
    df_ratios_production_teams["tackles_ratio"] = safe_ratio(df_ratios_production_teams, "returning_tackles", "total_tackles")
    df_ratios_production_teams["solo_tackles_ratio"] = safe_ratio(df_ratios_production_teams, "returning_solo_tackles","total_solo_tackles")
    df_ratios_production_teams["assisted_tackles_ratio"] = safe_ratio(df_ratios_production_teams, "returning_assisted_tackles", "total_assisted_tackles")
    df_ratios_production_teams["sacks_ratio"] = safe_ratio(df_ratios_production_teams, "returning_sacks",  "total_sacks")
    df_ratios_production_teams["qb_hurries_ratio"] = safe_ratio(df_ratios_production_teams, "returning_qb_hurries", "total_qb_hurries")
    df_ratios_production_teams["passes_defended_ratio"] = safe_ratio(df_ratios_production_teams, "returning_passes_defended", "total_passes_defended")
    df_ratios_production_teams["tackles_for_loss_ratio"] = safe_ratio(df_ratios_production_teams, "returning_tackles_for_loss", "total_tackles_for_loss")
    # fg 
    df_ratios_production_teams["fg_made_ratio"] = safe_ratio(df_ratios_production_teams,"returning_fg_made", "total_fg_made")
    df_ratios_production_teams["fg_attempted_ratio"] = safe_ratio(df_ratios_production_teams,"returning_fg_attempted", "total_fg_attempted")
    # xp
    df_ratios_production_teams["xp_made_ratio"] = safe_ratio(df_ratios_production_teams,"returning_xp_made", "total_xp_made")
    df_ratios_production_teams["xp_attempted_ratio"] = safe_ratio(df_ratios_production_teams,"returning_xp_attempted", "total_xp_attempted")
    # punt, long, attempts
    df_ratios_production_teams["punt_yard_ratio"] = safe_ratio(df_ratios_production_teams,"returning_punt_yards", "total_punt_yards")
    df_ratios_production_teams["punt_long_ratio"] = safe_ratio(df_ratios_production_teams,"returning_punt_long", "total_punt_long")
    df_ratios_production_teams["punt_attempts_ratio"] = safe_ratio(df_ratios_production_teams,"returning_punt_attempts", "total_punt_attempts")
    # kick
    df_ratios_production_teams["kick_returns_yards_ratio"] = safe_ratio(df_ratios_production_teams,"returning_kick_returns_yards", "total_kick_returns_yards")
    df_ratios_production_teams["kick_returns_td_ratio"] = safe_ratio(df_ratios_production_teams,"returning_kick_returns_touchdowns", "total_kick_returns_touchdowns")
    # punt
    df_ratios_production_teams["punt_returns_yards_ratio"] = safe_ratio(df_ratios_production_teams,"returning_punt_returns_yards","total_punt_returns_yards")
    df_ratios_production_teams["punt_returns_td_ratio"] = safe_ratio(df_ratios_production_teams, "returning_punt_returns_touchdowns", "total_punt_returns_touchdowns")

    # offense
                        # retrieving passing 
    df_ratios_production_teams_passing = df_ratios_production_teams[[
                                                    "team_id", "season", "passing_yards_ratio",
                                                    "passing_td_ratio", "passing_att_ratio", "passing_comp_ratio", 
                                                    "passing_inter_ratio"]]
    
    df_ratios_production_teams_passing["passing_score"] = df_ratios_production_teams_passing[[
                                                       "passing_yards_ratio","passing_td_ratio", "passing_att_ratio",
                                                       "passing_comp_ratio", "passing_inter_ratio"
                                                       ]].mean(axis = 1)


                        # retrieving rushing 
    df_ratios_production_teams_rushing = df_ratios_production_teams[[
                                                    "team_id", "season", "rushing_yards_ratio",
                                                    "rushing_td_ratio", "rushing_att_ratio"]]

    df_ratios_production_teams_rushing["rushing_score"] = df_ratios_production_teams_rushing[[
                                                            "rushing_yards_ratio","rushing_td_ratio", "rushing_att_ratio"
                                                      ]].mean(axis = 1)
    
                        #  retrieving receiving
    df_ratios_production_teams_receiving = df_ratios_production_teams[[
                                                    "team_id", "season", "receiving_yards_ratio",
                                                    "receiving_td_ratio", "receiving_recpt_ratio"
                                                   ]]

    df_ratios_production_teams_receiving["receiving_score"] = df_ratios_production_teams[[
                                                    "receiving_yards_ratio", "receiving_td_ratio", "receiving_recpt_ratio"
                                                   ]].mean(axis = 1)

    # another dataframe reduction
    df_ratios_production_teams_passing = df_ratios_production_teams_passing[["team_id", "season", "passing_score"]]
    df_ratios_production_teams_rushing = df_ratios_production_teams_rushing[["team_id", "season", "rushing_score"]]
    df_ratios_production_teams_receiving = df_ratios_production_teams_receiving[["team_id", "season", "receiving_score"]]
           # final offense calculation 
    df_ratios_offense = df_ratios_production_teams_passing.merge(
        df_ratios_production_teams_rushing, 
        on = ["team_id", "season"], 
        how = "inner"
    )             
    df_ratios_offense = df_ratios_offense.merge(
        df_ratios_production_teams_receiving, 
        on = ["team_id", "season"], 
        how = "inner"
    )

    # final_offense 
    df_ratios_offense["offense_score"] = df_ratios_offense[["passing_score", "rushing_score", "receiving_score"]].mean(axis = 1)


    # defense 
    df_ratios_defense = df_ratios_production_teams[[
                                                    "team_id", "season", "tackles_ratio",
                                                    "solo_tackles_ratio", "assisted_tackles_ratio","sacks_ratio",
                                                    "qb_hurries_ratio", "passes_defended_ratio","tackles_for_loss_ratio" 
                                                   ]]

    df_ratios_defense["defense_score"]  = df_ratios_production_teams[[
                                                    "tackles_ratio",
                                                    "solo_tackles_ratio", "assisted_tackles_ratio","sacks_ratio",
                                                    "qb_hurries_ratio", "passes_defended_ratio","tackles_for_loss_ratio" 
                                                   ]].mean(axis = 1)
    
   

    # special team 

    df_ratios_production_teams_field_goal = df_ratios_production_teams[[
                                                        "team_id", "season", "fg_made_ratio", "fg_attempted_ratio"
                                                       ]]
    # field goald
    df_ratios_production_teams_field_goal["score_field_goal"] = df_ratios_production_teams_field_goal[["fg_made_ratio", "fg_attempted_ratio"]].mean(axis =  1)
    # extra point
    df_ratios_production_teams_extra_point = df_ratios_production_teams[[
                                                        "team_id", "season", "xp_made_ratio", "xp_attempted_ratio"
                                                       ]]
    
    df_ratios_production_teams_extra_point["score_extra_point"] = df_ratios_production_teams_extra_point[["xp_made_ratio", "xp_attempted_ratio"]].mean(axis = 1)
     
    # punting
    df_ratios_production_teams_punting = df_ratios_production_teams[[
                                                        "team_id", "season", "punt_yard_ratio", "punt_long_ratio", "punt_attempts_ratio"
                                                       ]]

    df_ratios_production_teams_punting["score_punting"] = df_ratios_production_teams_punting[["punt_yard_ratio", "punt_long_ratio", "punt_attempts_ratio"]].mean(axis = 1)
    # kick
    df_ratios_production_teams_kick = df_ratios_production_teams[[
                                                        "team_id", "season", "kick_returns_yards_ratio", "kick_returns_td_ratio"
                                                       ]]
    
    df_ratios_production_teams_kick["kick_return_score"] = df_ratios_production_teams_kick[["kick_returns_yards_ratio", "kick_returns_td_ratio"]].mean(axis = 1)
    # punt_returns

    df_ratios_production_teams_punt_return = df_ratios_production_teams[[
                                                         "team_id", "season", "punt_returns_yards_ratio", "punt_returns_td_ratio"
                                                       ]]

    df_ratios_production_teams_punt_return["punt_return_score"] = df_ratios_production_teams_punt_return[["punt_returns_yards_ratio", "punt_returns_td_ratio"]].mean(axis = 1)

    # merge in order to take all the ratio  for special team 
    df_ratio_special_team = df_ratios_production_teams_field_goal[["team_id", "season","score_field_goal"]].merge(
        df_ratios_production_teams_extra_point[["team_id", "season", "score_extra_point"]], 
        on = ["team_id", "season"], 
        how = "inner"
    ).merge(
        df_ratios_production_teams_punting[["team_id", "season", "score_punting"]], 
        on = ["team_id", "season"], 
        how = "inner"
    ).merge(
        df_ratios_production_teams_kick[["team_id", "season", "kick_return_score"]], 
        on = ["team_id", "season"], 
        how = "inner"
    ).merge(
        df_ratios_production_teams_punt_return[["team_id", "season", "punt_return_score"]], 
        on = ["team_id", "season"],
        how = "inner"
    )

    df_ratio_special_team["special_team"] = df_ratio_special_team[["score_field_goal", "score_extra_point", "score_punting", "kick_return_score", "punt_return_score"]].mean(axis = 1)

    # reducing the number of column 
    df_ratios_offense = df_ratios_offense[["team_id", "season", "offense_score"]]
    df_ratios_defense = df_ratios_defense[["team_id", "season", "defense_score"]]
    df_ratio_special_team = df_ratio_special_team[["team_id", "season", "special_team"]]

    # last merge for returnning production
    df_returning_production =  df_ratios_offense.merge(
        df_ratios_defense, 
        on = ["team_id", "season"], 
        how = "inner"
    ).merge(
        df_ratio_special_team, 
        on = ["team_id", "season"], 
        how = "inner"
    )

    df_returning_production["returning_production_score"] = df_returning_production[["offense_score", "defense_score", "special_team"]].mean(axis = 1)


    # transform in json 
    df_returning_production = df_returning_production.to_json(orient = "records", indent = 4)

    # write the result in "raw"
    with open("data/raw/derived/returning_production_sample.json", "w") as json_returning_production: 
        json_returning_production.write(df_returning_production)
    
    return f"🤸 the file has been copied successfully"





val_fetch_team_n = fetch_returning_production_team_n()
val_fetch_team_n_1 = fetch_returning_production_team_n_1()
parse_team_n = parse_returning_production_team_n(val_fetch_team_n)
parse_team_n_1 = parse_returning_production_team_n_1(val_fetch_team_n_1)

print(compute_returning_production(parse_team_n, parse_team_n_1))