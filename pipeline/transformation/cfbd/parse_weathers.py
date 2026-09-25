import os 
import sys
from pathlib import Path 
import pandas as pd 


project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))



from pipeline.scrapers.cfbd.weathers import fetch_weather
# retrieve the datacolumns 
def parse_weathers(raw_weathers): 
    list_weather = []

    for i_weather in raw_weathers: 
        dict_weathers = {
            "game_id": int(i_weather["id"]), 
            "season": int(i_weather["season"]), 
            "week": int(i_weather["week"]), 
            "season_type": i_weather["seasonType"], 
            "start_time": i_weather["startTime"], 

            "game_indoors": i_weather["gameIndoors"], 
          
            "home_team": i_weather["homeTeam"], 
            "home_conference": i_weather["homeConference"], 
            "away_team": i_weather["awayTeam"], 
            "away_conference": i_weather["awayConference"], 

            "venue_id": int(i_weather["venueId"]), 
            "venue": i_weather["venue"], 

            "temperature": int(i_weather["temperature"]), 
            "dew_point": int(i_weather["dewPoint"]), 
            "humidity": int(i_weather["humidity"]), 
            "precipitation": int(i_weather["precipitation"]), 
            "snow_fall": int(i_weather["snowfall"]), 
            "wind_speed": int(i_weather["windSpeed"]), 
            "wind_direction": int(i_weather["windDirection"]), 
            "pressure": float(i_weather["pressure"]), 

            "weather_condition_code": int(i_weather["weatherConditionCode"]), 
            "weather_condition" : i_weather["weatherCondition"]
        }

        list_weather.append(dict_weathers)
    
    return list_weather
  
  # convertir mon games en DataFrame
# vall_fetch = fetch_weather()
# print(parse_weathers(vall_fetch))
