import os 
import sys


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)


def parse_calendar(rawcalendar): 
    listcalendar = []
    for i in rawcalendar: 
        valdiccalendar = {
        "season": i["season"], 
        "week": i["week"], 
        "season_type": i["season_type"], 
        "start_date": i["start_date"], 
        "end_date": i["end_date"]
    }
        listcalendar.append(valdiccalendar)
    
    return listcalendar

from pipeline.scrapers.calendar import fetch_calendar
valcalendar = fetch_calendar(2023)
print(parse_calendar(valcalendar))