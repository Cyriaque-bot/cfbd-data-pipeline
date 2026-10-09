import sys
from pathlib import Path 
import pandas as pd 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root)) 



from pipeline.scrapers.cfbd.team_season_overview import fetch_team_season_overview
from pipeline.scrapers.cfbd.conferences import fetch_conference
from pipeline.scrapers.cfbd.conference_resilisation import fetch_conference_affiliation

from pipeline.transformation.cfbd.parse_team_season_overview import parse_team_season_overview
from pipeline.transformation.cfbd.parse_conference_affiliation import parse_conference_affiliation
from pipeline.transformation.cfbd.parse_conference import parse_conference

def merge_team_conference_affiliation(raw_parse_game_team_stats, raw_parse_conference_affiliation,raw_parse_conference ): 
    df_conference  = pd.DataFrame(raw_parse_conference)
    df_conference_affiliation  = pd.DataFrame(raw_parse_conference_affiliation)
    df_team_stats_overview = pd.DataFrame(raw_parse_game_team_stats)
  
    # return only df_conference_affiliation if still_in_conference == True 
    df_conference_affiliation = df_conference_affiliation.loc[df_conference_affiliation["still_in_conference"] == True] 

    df_team_merge_conf_aff = df_team_stats_overview.merge(
        df_conference_affiliation[["team_id", "conference_id", "conference_division", "conference_start_year", "conference_end_year"]], 
        on = "team_id", 
        how = "left"
    )

    df_team_merge_conf_aff_final = df_team_merge_conf_aff.merge(
        df_conference[["conference_id", "conference_name", "conference_short_name", "conference_classification", "conference_member_count"]], 
        on = "conference_id",
        how = "left"
    )

    # transformin json 
    df_team_merge_conf_aff_final = df_team_merge_conf_aff_final.to_json(orient = "records", indent = 4)

    with open("data/raw/derived/merge_team_conference_affiliation_sample.json", "w") as json_merge_team_conference_affiliation:
         json_merge_team_conference_affiliation.write(df_team_merge_conf_aff_final)

    return f"🤸 the file has been copied successuffy"
   

# valfetchconf = fetch_conference()
# valfetchconfaff = fetch_conference_affiliation()
# vallfetchteam = fetch_team_season_overview()

# parsefetchconf = parse_conference(valfetchconf)
# parsefetchconfff = parse_conference_affiliation(valfetchconfaff)
# parsefetchteam = parse_team_season_overview(vallfetchteam)

# print(merge_team_conference_affiliation(parsefetchteam, parsefetchconfff, parsefetchconf))