import sys 
from pathlib import Path 

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.conference_resilisation import fetch_conference_affiliation

def parse_conference_affiliation(raw_conference_affiliation): 
    
    list_conference_affiliation = []

    for i_conference_affiliation in raw_conference_affiliation : 

        def end_year(): 
            try: 
                if int(i_conference_affiliation["endYear"]):
                   return int(i_conference_affiliation["endYear"])
            except: 
                   return None
        
        dict_conference_affiliation = {
            "team_id" : int(i_conference_affiliation["teamId"]), 
            "team_name": i_conference_affiliation["team"], 
            "conference_id": int(i_conference_affiliation["conferenceId"]), 
            "conference_short": i_conference_affiliation["conferenceAbbreviation"], 
            "conference_classification": i_conference_affiliation["classification"], 
            "conference_division": i_conference_affiliation["conferenceDivision"], 
            "conference_start_year": int(i_conference_affiliation["startYear"]), 
            "conference_end_year": end_year(),
            "still_in_conference": True if end_year() == None else False
        }
        list_conference_affiliation.append(dict_conference_affiliation)
    
    return list_conference_affiliation



# val = fetch_conference_affiliation()
# print(parse_conference_affiliation(val))