import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root) 

def parse_coaches(raws_coaches): 
    valintercoachesone = {}
    vallistcoach = []

    # first intermediate values 
    for i in raws_coaches: 
        basecoaches =  {
                               "coach_id": i["id"], 
                               "first_name": i["first_name"], 
                               "last_name": i["last_name"], 
                               "hire_date": i["hire_date"]     
                      }
    # Second intermediate values that is  a good methode 
        for j in i["seasons"]:
            valintercoachesone = { 
              **basecoaches,
               "season": j["year"], 
               "school": j["school"], 
               "position": j["position"]
            }
             
   
        vallistcoach.append(valintercoachesone)
    return vallistcoach
        


    # return valintercoachesone

from pipeline.scrapers.coaches import fetch_coaches
varcoache = fetch_coaches(2023)
print(parse_coaches(varcoache))