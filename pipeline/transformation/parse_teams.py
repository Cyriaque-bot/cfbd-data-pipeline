import sys 
import os 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


def parse_teams(rawteam): 
    listeam = []
    for i in rawteam: 
        vallistetaems =  {
          "team_id": i["id"], 
          "school": i["school"], 
          "mascot": i["mascot"],
          "abbreviation": i["abbreviation"], 
          "conference": i["conference"],
          "division": i["division"],
          "city": i["location"]["city"], 
          "state": i["location"]["state"], 
          "latitude": i["location"]["latitude"], 
          "longitude": i["location"]["longitude"]
            }
        listeam.append(vallistetaems)

    return listeam

from pipeline.scrapers.teams import fetch_teams
valteams = fetch_teams(2023)
parsed = parse_teams(valteams)
print(parsed)