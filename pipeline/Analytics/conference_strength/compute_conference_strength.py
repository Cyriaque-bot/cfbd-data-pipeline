import sys 
from pathlib import Path
import pandas as pd 
import os 
import glob 
import json

project_root =  Path(__file__).absolute().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_conference import load_conference
from pipeline.scrapers.cfbd.conferences import fetch_conference



def load_conference_data():

    # path to write my csv in final folders
    path_conference_strength = "data/final/external/conference_strength.csv"
    # loading all the processed files from data/processed/external
    path_conference_folder = "data/processed/external/*.csv"
    # retrieve all files
    conference_all_file = glob.glob(path_conference_folder)
    # conference file to first avoid 
    to_avoid = "interconference_processed.csv"
    # retrieve all file except interconference_processed
    conference_all_file_execpt = [
    i for i in conference_all_file if os.path.basename(i) != to_avoid
    ]

    # define my key columns 
    key_col_conf = ["team", "season"]

    # initializing column 
    df_conf_init = pd.read_csv(conference_all_file_execpt[0])

    # go through and merge all the other files one by one 
    for i_other in conference_all_file_execpt[1:]:
        df_conf_other = pd.read_csv(i_other)

    # fusion horizontale sur les deux colonnes
        df_conf_init = pd.merge(
                                df_conf_init, 
                                df_conf_other, 
                                on = key_col_conf, 
                                how = "left"
                            )
    # return df_conf_init

    ##### loading our last file interconference 
    # path to retrieved inteconference file 
    path_interconference = "data/processed/external/interconference_processed.csv"
    # load intercoference file 
    load_interconference = glob.glob(path_interconference)
    df_interconference = pd.read_csv(load_interconference[0])

    # make a join with my module conference 
    load_conference_value = load_conference
    val_conf_value = fetch_conference(load_conference_value)
    df_conference = pd.DataFrame(val_conf_value[0].items(), columns = ["team", "conference"])

    # join my df_interconference with my df_conference in order to retrieve the column team 
    df_merge_team_interconference = df_interconference.merge(
                                                             df_conference, 
                                                             on = "conference",
                                                             how = "left"
                                                             )

    # last join in order to have a last values

    df_conference_final = df_conf_init.merge(
         df_merge_team_interconference, 
         on = ["team", "season"], 
         how = "left"
    )

    # return df_conference_final
    # open and read the conference  features 
    with(open("pipeline/config/conference_features.json", "r", encoding = "utf-8"))as conferencejson: 
        config_conference = json.load(conferencejson)
        # mapping columns 
        mapping_columns = {
                           "epa_value": "net_epa", 
                           "recruiting_score": "avg_rating", 
                           "nfl_players": "avg_nfl_rating", 
                           "tv_rating": "avg_viewers", 
                           "weeks_ranked": "weeks_ranked", 
                           "coach_score": "coach_value_score", 
                           "interconf_value_score": "interconf_value_score"
                           }
 
    for key_conference, val_conference  in config_conference.items(): 
        target_fields = val_conference["field"]
        target_agg = val_conference["Aggregation"]

        real_conf_mapp = mapping_columns[target_fields]
                
        df_conference_final[f"{key_conference}_target_agg"] = (
             df_conference_final.groupby("conference")[real_conf_mapp].transform(target_agg)
        )

        # stockage unique dans une table 
        # return df_conference_final[f"{key_conference}_target_agg"]
    with(open("pipeline/config/conference_weights.json", "r"))as jsonconference_weights: 
        conference_weights = json.load(jsonconference_weights)
        mapping_column_weights = {
                                    "epa": "epa_target_agg", 
                                    "recruiting":"recruiting_target_agg", 
                                    "nfl": "nfl_target_agg",
                                    "tv_rating": "tv_rating_target_agg", 
                                    "top25": "top25_target_agg", 
                                    "coaching": "coaching_target_agg", 
                                    "interconference": "interconference_target_agg"
                               }

        df_conference_final["conference_strength_score"] = 0
        
        for key_i_weights, val_i_weights in conference_weights.items(): 

            map_col_weight = mapping_column_weights[key_i_weights]

            df_conference_final["conference_strength_score"] = df_conference_final["conference_strength_score"] + (
                            df_conference_final[map_col_weight] * val_i_weights
            )
 

    df_conference_final = df_conference_final.to_csv(path_conference_strength, index = False, encoding = "utf-8")  

    return f"🤸 our files have been sent succesfuly you can check() on this path {path_conference_strength}"
    
  


print(load_conference_data())


