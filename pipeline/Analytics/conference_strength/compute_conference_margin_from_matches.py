import sys 
from pathlib import Path
import pandas as pd 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.scrapers.derived.merge_team import fetch_merge_team
from pipeline.scrapers.cfbd.conference_affiliation import fetch_conference_affiliation

from pipeline.transformation.derived.parse_merge_team import parse_merge_team
from pipeline.transformation.cfbd.parse_conference_affiliation import parse_conference_affiliation

def compute_conference_margin(raw_conference_affiliation, raw_merge_team): 
    df_conference_affiliation = pd.DataFrame(raw_conference_affiliation)
    df_merge_team = pd.DataFrame(raw_merge_team)
    # first merge to add team_conference_id and opponent_conference_id
    # team_conference_id
    df_conf_margin_team = df_merge_team.merge(
        df_conference_affiliation[["team_id","conference_id", "conference_name"]].rename(columns = {
               "team_id": "team_id_conf_aff", 
               "conference_id": "team_conference_id", 
               "conference_name": "team_conference_name"}), 
        left_on = "team_id",
        right_on = "team_id_conf_aff" 
    )
    # opponent_conference_id
    df_conf_margin = df_conf_margin_team.merge(
        df_conference_affiliation[["team_id","conference_id", "conference_name"]].rename(columns = {
               "team_id": "opponent_id_conf_aff", 
               "conference_id": "opponent_conference_id", 
               "conference_name": "opponent_conference_name"}), 
        left_on = "opponent_id",
        right_on = "opponent_id_conf_aff" 
    )

    # retrieve all the interconference game 
    df_conf_margin = df_conf_margin[df_conf_margin["team_conference_id"] != df_conf_margin["opponent_conference_id"]]
    
    df_conf_margin["opponent_margin"]  = df_conf_margin["opponent_points"] - df_conf_margin["team_points"]

    # injection in our df_conf_margin 
    df_margin = ( 
        df_conf_margin
        .groupby("team_conference_id")["opponent_margin"]
        .mean()
        .reset_index()
    )

    df_margin = df_margin.rename({
                                  "team_conference_id" : "conference_id", 
                                  "opponent_margin": "conference_avg_opponent_margin"
                                  })

    df_margin = df_margin.to_json(orient = "records", indent = 4)

    # insert create a new file to stock all inside

    with open("data/raw/derived/conference_margin_from_matches_sample.json", "w") as json_conference_margin_from_matches: 
        json_conference_margin_from_matches.write(df_margin)

    return "🤸 you succesfully write file"

  



# valscrap = fetch_merge_team()
# valparse  = parse_merge_team(valscrap)

# valscrp = fetch_conference_affiliation()
# vaslfetch = parse_conference_affiliation(valscrp)


# print(compute_conference_margin(vaslfetch, valparse))

