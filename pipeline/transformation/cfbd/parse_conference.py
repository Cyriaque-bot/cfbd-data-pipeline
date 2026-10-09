import sys 
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.conferences import fetch_conference
def parse_conference(raw_parse_conference): 
    list_conference = []
    for i_conference in raw_parse_conference: 
        dict_conference  =  {
            "conference_id": int(i_conference["id"]), 
            "conference_name": i_conference["name"], 
            "conference_short_name": i_conference["shortName"], 
            "conference_abbreviation": i_conference["abbreviation"], 
            "conference_classification": i_conference["classification"], 
            "conference_member_count": int(i_conference["memberCount"])
        }
        list_conference.append(dict_conference)

    return list_conference



# val = fetch_conference()
# print(parse_conference(val))