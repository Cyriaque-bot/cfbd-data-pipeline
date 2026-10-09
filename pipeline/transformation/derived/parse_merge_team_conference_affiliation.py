import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.derived.merge_team_conference_affiliation import fetch_merge_team_conference_affiliation


def parse_merge_team_conference_affiliation(raw_merge_team_conference_affiliation):
    list_merge_team_conference_affiliation = []
    for i_merge_team_conference_affiliation in raw_merge_team_conference_affiliation: 
        dict_merge_team_conference_affiliation = {

            # team 
            "team_id" : i_merge_team_conference_affiliation["team_id"], 
            "team" : i_merge_team_conference_affiliation["team"], 
            "season": i_merge_team_conference_affiliation["season"], 

            # conference
            "conference_id" : i_merge_team_conference_affiliation["conference_id"], 
            "conference_name": i_merge_team_conference_affiliation["conference_name"], 
            "conference_short_name": i_merge_team_conference_affiliation["conference_short_name"], 
            "conference_classification": i_merge_team_conference_affiliation["conference_classification"], 
            "conference_division": i_merge_team_conference_affiliation["conference_division"], 
            "conference_start_year": i_merge_team_conference_affiliation["conference_start_year"], 
            "conference_end_year": i_merge_team_conference_affiliation["conference_end_year"], 
            "conference_member_count": i_merge_team_conference_affiliation["conference_member_count"], 

            # record
            "games": i_merge_team_conference_affiliation["games"], 
            "wins": i_merge_team_conference_affiliation["wins"], 
            "losses": i_merge_team_conference_affiliation["losses"],
            "ties": i_merge_team_conference_affiliation["ties"], 

            # rating SP+
            "sp_offense": i_merge_team_conference_affiliation["sp_offense"], 
            "sp_defense": i_merge_team_conference_affiliation["sp_defense"], 
            "sp_special": i_merge_team_conference_affiliation["sp_special"],
            "sp_overall": i_merge_team_conference_affiliation["sp_overall"],

            # SRS/ ELO
            "srs": i_merge_team_conference_affiliation["srs"], 
            "elo": i_merge_team_conference_affiliation["elo"], 

            # FPI
            "fpi_offense": i_merge_team_conference_affiliation["fpi_offense"],
            "fpi_defense": i_merge_team_conference_affiliation["fpi_defense"],
            "fpi_special": i_merge_team_conference_affiliation["fpi_special"],
            "fpi_overall": i_merge_team_conference_affiliation["fpi_overall"], 

            # Offense
            "off_ppa": i_merge_team_conference_affiliation["off_ppa"],
            "off_success": i_merge_team_conference_affiliation["off_success"],
            "off_explosiveness": i_merge_team_conference_affiliation["off_explosiveness"],
            "off_drives": i_merge_team_conference_affiliation["off_drives"],
            "off_plays":i_merge_team_conference_affiliation["off_plays"],
            "off_ppa_pass": i_merge_team_conference_affiliation["off_ppa_pass"],
            "off_success_pass":i_merge_team_conference_affiliation["off_success_pass"],
            "off_explosiveness_pass":i_merge_team_conference_affiliation["off_explosiveness_pass"],
            "off_ppa_rush": i_merge_team_conference_affiliation["off_ppa_rush"],
            "off_success_rush": i_merge_team_conference_affiliation["off_success_rush"],
            "off_explosiveness_rush":i_merge_team_conference_affiliation["off_explosiveness_rush"],

            # defense
            "def_ppa": i_merge_team_conference_affiliation["def_ppa"],
            "def_success": i_merge_team_conference_affiliation["def_success"],
            "def_explosiveness": i_merge_team_conference_affiliation["def_explosiveness"],
            "def_drives": i_merge_team_conference_affiliation["def_drives"],
            "def_plays":i_merge_team_conference_affiliation["def_plays"],
            "def_ppa_pass": i_merge_team_conference_affiliation["def_ppa_pass"],
            "def_success_pass":i_merge_team_conference_affiliation["def_success_pass"],
            "def_explosiveness_pass":i_merge_team_conference_affiliation["def_explosiveness_pass"],
            "def_ppa_rush": i_merge_team_conference_affiliation["def_ppa_rush"],
            "def_success_rush": i_merge_team_conference_affiliation["def_success_rush"],
            "def_explosiveness_rush":i_merge_team_conference_affiliation["def_explosiveness_rush"],
        }
        list_merge_team_conference_affiliation.append(dict_merge_team_conference_affiliation)

    return list_merge_team_conference_affiliation



# val = fetch_merge_team_conference_affiliation()
# print(parse_merge_team_conference_affiliation(val))