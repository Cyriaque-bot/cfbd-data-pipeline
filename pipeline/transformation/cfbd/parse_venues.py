
import os 
import sys 

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path: 
    sys.path.insert(0, project_root)



def parse_venues(raw_venues): 
    valisvenue = []
    for i in raw_venues: 
        valdictvenue = {
           "venue_id": i["id"], 
           "name": i["name"], 
           "capacity": i["capacity"], 
           "city": i["city"], 
           "state": i["state"],
           "zip": i["zip"], 
           "country_code": i["country_code"], 
           "year_constructed": i["year_constructed"],
           "grass": i["grass"],
           "dome": i["dome"]
       }
        valisvenue.append(valdictvenue)
    
    
    return valisvenue


from pipeline.scrapers.venues import fecth_venues
valvenues = fecth_venues(2023)

print(parse_venues(valvenues))