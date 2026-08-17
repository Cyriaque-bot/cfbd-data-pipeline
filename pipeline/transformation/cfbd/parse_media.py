import sys 
from pathlib import Path
from datetime import datetime
from datetime import time


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))


from pipeline.scrapers.cfbd.media import fetch_media 
def parse_media(raw_media): 
    list_media = []
    prime_time_start = time(19, 0)
    prime_time_end = time(22, 0)

    for i_media  in raw_media: 
        # conversion in dateteime for taking the prime_time 
        valdatetime = datetime.fromisoformat(i_media["startTime"].replace("Z", "+00:00")) 
        # extraction  in format text "HH:MM"
        prime_time_final = valdatetime.time()
   
        
        dict_media = {
            "game_id": int(i_media["id"]), 
            "season": int(i_media["season"]), 
            "week": int(i_media["week"]), 
            "home_team": i_media["homeTeam"], 
            "away_team": i_media["awayTeam"], 
            "network": i_media["outlet"], 
            "start_time": i_media["startTime"], 
            "prime_time": prime_time_start <= prime_time_final <= prime_time_end, 
            "national_broadcast" : True if i_media["outlet"] in ("FOX", "CBS", "ESPN", "ESPN2", "ESPNU", "ABC", 
                                                                 "NBC", "FS1", "SEC Network","Big Ten Network") else False
        }

        list_media.append(dict_media)

    return list_media


# val = fetch_media()
# print(parse_media(val))