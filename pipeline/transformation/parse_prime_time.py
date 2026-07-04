import os 
import sys 
from pathlib import Path
from datetime import datetime
from datetime import time 

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

def parse_prime_time(raw_data_prime): 
    raw_data_prime_list = []
    startdate = time(19, 0)
    enddate = time(22, 0)
    for key, values in raw_data_prime.items(): 
        for i in values: 

            raw_data_prime_dict =  {
                "game_id" : i["id"], 
                "is_prime_time" : 1 if(startdate <= datetime.fromisoformat(i["start_date"].replace("Z", "+00:00")).time()<= enddate
                 and i["media"][0]["network"] in ("ESPN", "ABC", "FOX", "CBS", "NBC", "ESPN2")) else 0                                      
            }
    
            raw_data_prime_list.append(raw_data_prime_dict)
    return raw_data_prime_list
















# from pipeline.scrapers.prime_time import fetch_prime_time

# valfetchprime = fetch_prime_time()
# print(parse_prime_time(valfetchprime))