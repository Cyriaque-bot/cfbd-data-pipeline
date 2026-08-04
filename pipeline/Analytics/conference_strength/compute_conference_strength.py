import sys 
from pathlib import Path
import pandas as pd 
import os 
import glob 

project_root =  Path(__file__).absolute().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_conference import load_conference
from pipeline.scrapers.cfbd.conferences import fetch_conference

def load_conference_data():
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
    
#     return df_conference_final



######### calcul du score composite   ###########

# retrieve epa and transform it in df 
    # path epa 
    path_epa = "data/processed/external/epa_processed.csv" 
    # load epa 
    conf_epa = glob.glob(path_epa)
    df_epa = pd.read_csv(conf_epa[0])

# retrieve coaching  and transform it in df 
    path_coaching = "data/processed/external/coaching_processed.csv" 
    # load coaching
    conf_coaching = glob.glob(path_coaching)
    df_coaching = pd.read_csv(conf_coaching[0])

#  retrieve nfl and transform it in df 
    path_nfl = "data/processed/external/nfl_processed.csv"
    # load nfl 
    conf_nfl = glob.glob(path_nfl)
    df_nfl = pd.read_csv(conf_nfl[0])

#  retrieve recruiting_external and transform it in df 
    path_recruiting_external = "data/processed/external/recruiting_external_processed.csv"
    # load recruiting_external
    conf_recruiting_external = glob.glob(path_recruiting_external)
    df_path_recruiting_external = pd.read_csv(conf_recruiting_external[0])

#  retrieve interconference_processed and transform it in df
    path_interconference = "data/processed/external/interconference_processed.csv"
    # load interconference_processed
    conf_interconference_processed = glob.glob(path_interconference)
    df_interconference = pd.read_csv(conf_interconference_processed[0])

#  retrieve top25 and transform it in df
    path_top25 = "data/processed/external/top25_processed.csv"
    # load top25
    conf_top25 = glob.glob(path_top25)
    df_top25 = pd.read_csv(conf_top25[0])

#  retrieve tv_rating and transform it in df
    path_tv_rating = "data/processed/external/tv_rating_processed.csv"
    # load tv_rating
    conf_tv_rating = glob.glob(path_tv_rating)
    df_tv_rating = pd.read_csv(conf_tv_rating[0])
    
    return df_tv_rating
print(load_conference_data())