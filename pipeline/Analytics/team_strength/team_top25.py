import sys
from pathlib import Path
import pandas as pd 
import json
import numpy as np

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.rankings import fetch_rankings
from pipeline.scrapers.cfbd.teams import fetch_teams

from pipeline.transformation.cfbd.parse_top25 import parse_top25
from pipeline.transformation.cfbd.parse_teams import parse_teams 


def team_top25(list_teams, list_top25): 
    list_team_top25 = []
    df_i_team = pd.DataFrame(list_teams)
    # transform all module in dataframe         
    df_j_top25 = pd.DataFrame(list_top25)

    df_teams_top25 = (df_i_team
    .merge(
            df_j_top25[["school", "top25_rank", "top25_score"]], 
            on = ["school"],
            how = "left"
        )
      ) 
    
    df_teams_top25.loc[df_teams_top25["top25_rank"].isna(), "top25_score"] = 0.00
    df_teams_top25 = df_teams_top25.replace({np.nan : None})
    df_teams_top25  = df_teams_top25.to_dict(orient = "records")


    # write my file in data final 
    with open("data/raw/derived/team_top25_sample.json", "w") as jsonteamtop25: 
          json.dump(df_teams_top25, jsonteamtop25, indent = 4)


    return f"🤸 the file has been copied succesfully"
    return df_teams_top25



list_teams = fetch_teams(all)
list_ranking = fetch_rankings(all)

vakteam = parse_teams(list_teams)
vaktop25 = parse_top25(list_ranking)

print(team_top25(list_teams, vaktop25))