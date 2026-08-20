import sys 
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


def parse_teams(rawteam): 
    listeam = []
    for i_team in rawteam: 
        dict_teams =  {
          "team_id": int(i_team["id"]), 
          "school": i_team["school"], 
          "mascot": i_team["mascot"],
          "abbreviation": i_team["abbreviation"], 
          "alternatenames": i_team["alternateNames"], 
          "conference": i_team["conference"],
          "division": i_team["division"],
          "classification": i_team["classification"], 
          "color": i_team["color"], 
          "alternatecolor": i_team["alternateColor"], 
          "logos": i_team["logos"], 
          "twitter": i_team["twitter"],
          "location": {
              "id" : i_team["location"]["id"], 
              "name" : i_team["location"]["name"], 
              "city": i_team["location"]["city"], 
              "state": i_team["location"]["state"],
              "zip": i_team["location"]["zip"],
              "country_code": i_team["location"]["countryCode"], 
              "timezone":  i_team["location"]["timezone"], 
              "latitude": float(i_team["location"]["latitude"]), 
              "longitude": float(i_team["location"]["longitude"]), 
              "elevation":  i_team["location"]["elevation"], 
              "capacity": int(i_team["location"]["capacity"]), 
              "construction_year": int(i_team["location"]["constructionYear"]), 
              "grass": i_team["location"]["grass"], 
              "dome": i_team["location"]["dome"]
          }
 
            }
        listeam.append(dict_teams)

    return listeam

# from pipeline.scrapers.cfbd.teams import fetch_teams
# valteams = fetch_teams(2023)
# print(parse_teams(valteams))