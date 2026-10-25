import sys
from pathlib import Path 
import pandas as pd


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.merge_team import fetch_merge_team
from pipeline.scrapers.cfbd.conference_affiliation import fetch_conference_affiliation
from pipeline.scrapers.derived.conference_strength_cfbd import fetch_conference_strength_cfbd
from pipeline.scrapers.derived.conference_margin_from_matches import fetch_conference_margin


from pipeline.transformation.derived.parse_merge_team import parse_merge_team
from pipeline.transformation.cfbd.parse_conference_affiliation import parse_conference_affiliation
from pipeline.transformation.derived.parse_conference_strength_cfbd import parse_conference_strength_cfbd
from pipeline.transformation.derived.parse_conference_margin_from_matches import parse_conference_margin


def add_opponent_conference_strength(raw_merge_team, raw_conference_affiliation, raw_conference_strength_cfbd, raw_conference_margin): 
    df_team = pd.DataFrame(raw_merge_team)
    df_conference_affiliation = pd.DataFrame(raw_conference_affiliation)
    df_raw_merge_conference_strenght_cfbd = pd.DataFrame(raw_conference_strength_cfbd)
    df_raw_conference_margin = pd.DataFrame(raw_conference_margin)

    #  merge in order to take team_conference_id 
       # team_conference_id
    df_take_team_conf_id = (
        df_team[["game_id", "season", "week", "team_id", "team","opponent_id",
                 "opponent", "team_points", "opponent_points"]]
        .merge(
                 df_conference_affiliation[["team_id", "conference_id"]].rename(columns = {
                     "conference_id": "team_conference_id"
                 }), 
                 on = "team_id", 
                 how = "left"
              )
    ) 
        # opponent_conference_id
    
    df_take_opponent_conf_id = (
        df_take_team_conf_id
        .merge(
                 df_conference_affiliation[["team_id", "conference_id"]].rename(columns = {
                     "conference_id": "opponent_conference_id"
                 }), 
                 left_on = "opponent_id", 
                 right_on = "team_id"  
              )
    ) 
    df_take_opponent_conf_id = df_take_opponent_conf_id.drop(columns = {"team_id_y"})
    df_take_opponent_conf_id = df_take_opponent_conf_id.rename(columns = {"team_id_x": "team_id"})

   
    # merge in order to get opponent_conference_id
   
    # seconde merge once i get conference_id is to take win_rate, raw, norm for team
    df_take_conf_team = df_take_opponent_conf_id.merge(
        df_raw_merge_conference_strenght_cfbd[["conference_id", "conference_avg_win_rate", "conference_strength_raw", "conference_strength_norm"]]
                                .rename(
                                    columns = {
                                        "conference_avg_win_rate" : "team_conference_avg_win_rate", 
                                        "conference_strength_raw": "team_conference_strength_raw", 
                                        "conference_strength_norm": "team_conference_strength_norm"
                                               }),
        left_on = "team_conference_id", 
        right_on = "conference_id"                        
    )

    
     # seconde merge once i get conference_id is to take win_rate, raw, norm for opponent
    df_take_conf_opponent = df_take_conf_team.merge(
        df_raw_merge_conference_strenght_cfbd[["conference_id", "conference_avg_win_rate", "conference_strength_raw", "conference_strength_norm"]]
                                .rename(
                                    columns = {
                                        "conference_avg_win_rate" : "opponent_conference_avg_win_rate", 
                                        "conference_strength_raw" : "opponent_conference_strength_raw", 
                                        "conference_strength_norm" : "opponent_conference_strength_norm"
                                               }),
        left_on = "opponent_conference_id", 
        right_on = "conference_id"
                                
    )
    df_take_conf_opponent = df_take_conf_opponent.drop(columns = {"conference_id_y"})
    df_take_conf_opponent = df_take_conf_opponent.rename(columns = {"conference_id_x": "conference_id"})
 
    # last merge in order to insert the margin for the team
    df_final_team = df_take_conf_opponent.merge(
        df_raw_conference_margin[["team_conference_id", "opponent_margin"]].rename(columns = { 
            "opponent_margin": "team_conference_avg_opponent_margin"
        }), 
        on = "team_conference_id", 
        how = "left"
    ).fillna(0)

    # team normalizing 
    min_team_conference_avg_opponent_margin = min(df_final_team["team_conference_avg_opponent_margin"])
    max_team_conference_avg_opponent_margin = max(df_final_team["team_conference_avg_opponent_margin"])

    df_final_team["team_conference_avg_opponent_margin_norm"] = (
                                       (df_final_team["team_conference_avg_opponent_margin"] 
                                       - min_team_conference_avg_opponent_margin)
                                       /(max_team_conference_avg_opponent_margin
                                       - min_team_conference_avg_opponent_margin)
    )

    
    # last merge in order to insert the margin for the opponent
    df_final = df_final_team.merge(
        df_raw_conference_margin[["team_conference_id", "opponent_margin"]].rename(columns = {
            "opponent_margin": "opponent_conference_avg_opponent_margin"
        }), 
        left_on = "opponent_conference_id", 
        right_on = "team_conference_id"
    ).fillna(0)

    df_final = df_final.drop(columns = {"team_conference_id_y"})
    df_final = df_final.rename(columns = {"team_conference_id_x": "team_conference_id"})

    # opponent normalizing 
    min_opponent_conference_avg_opponent_margin = min(df_final["opponent_conference_avg_opponent_margin"])
    max_opponent_conference_avg_opponent_margin = max(df_final["opponent_conference_avg_opponent_margin"])

    
    df_final["opponent_conference_avg_opponent_margin_norm"] = (
                                       (df_final["opponent_conference_avg_opponent_margin"] 
                                       - min_opponent_conference_avg_opponent_margin)
                                       /(max_opponent_conference_avg_opponent_margin
                                       - min_opponent_conference_avg_opponent_margin)
    )

    # return df_final.columns


    # transform all of them in list
    df_final = df_final.to_json(orient = "records",  indent = 4)

    with open("data/raw/derived/add_opponent_conference_strength_sample.json", "w")as json_add_opponent_conference_strength: 
       json_add_opponent_conference_strength.write(df_final)

    return "🤸 the file has been copied succesfully"

     
 





# valscrape_merge_team = fetch_merge_team()
# valscrape_confe_team = fetch_conference_margin()
# valscrapr_confe_stren = fetch_conference_strength_cfbd()
# valscrp_conf_aff = fetch_conference_affiliation()

# valparse_merge_team = parse_merge_team(valscrape_merge_team)
# valparse_confer_team = parse_conference_margin(valscrape_confe_team)
# valparse_confer_stren = parse_conference_strength_cfbd(valscrapr_confe_stren)
# valparse_conf_affiliat = parse_conference_affiliation(valscrp_conf_aff)


# print(add_opponent_conference_strength(valparse_merge_team, valparse_conf_affiliat, valparse_confer_stren, valparse_confer_team))